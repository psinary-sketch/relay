# -*- coding: utf-8 -*-
"""b681_record.py -- THE ACT'S RECORD TOOL, b681 under (R291).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b681's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows can run each reader over one row of each shape before the seal.
### Carried by the Write tool from b680_record.py (the helpers, the guarded landing, the readers, step zero's rowgen and branches routes);
### the later routes are added at their components.
### Every python child is started as `python -X utf8`, no environment mapping passed. Routes: `python tools/b681_record.py <route> [dry]`.
"""
import collections
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
import b681_worklist as K          # noqa: E402

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
    none a number any bank carries; a stand-in run writes no bank. Carried from b680_record.py with b681's names."""
    sk = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
    return {
        'b681_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b681_findings.json': dict(entry_line=99999, title='stand-in'),
        'b681_trail.json': dict(line=99999),
        'b681_act_root.json': dict(root='0' * 64, previous='764d21d6' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
    }


def jl(name):
    try:
        return json.load(io.open(os.path.join(D, name), encoding='utf-8'))
    except Exception:
        return _standins().get(name, {}) if STANDIN else {}


def g(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def _show(repo, rev, path):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b681's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b681_scanfile_%s.md' % tag)
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
    """a row of data/b681_branches.json: a repository, a branch, its tip (40 hex), where it stands (local or remote) and its fate (one of
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
    build-free diff) over the 19 roster tables; each tool's verdict lines banked with its exit. data/b681_rowgen_<stage>.txt."""
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
    L = ['b681 -- %s: ROWGEN DIFF AND CONSTELLATION MODE (b670 rules row 3) (%s)' % (stage.upper(), utc()), '',
         '### the roster: the 19 tables of relay data/b586_corroboration.txt :34 at PLACE-papers HEAD %s ; the instruments: tools/rowgen/rowgen.py '
         '`constellation`, tools/rowgen/diff_rowpin.py (build-free; `rowgen.py diff` runs lean and is not run on this host) ; %d s' % (
             g(PP, 'rev-parse', '--short', 'HEAD').strip(), secs), '',
         '### constellation, exit %d ; its last lines:' % con.returncode] + ['    ' + l for l in tail(co)] + [
         '', '### diff_rowpin, exit %d ; its last lines:' % dif.returncode] + ['    ' + l for l in tail(do)] + [
         '', '### ### **CONSTELLATION EXIT %d ; ROWGEN DIFF EXIT %d ; TABLES 19.**' % (con.returncode, dif.returncode)]
    put_txt('b681_rowgen_%s.txt' % stage, L)
    print(NL.join(L[-14:]))


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R291)(9))
def branches(*a):
    """every branch (R291)(9) names, its tip read before any delete, its fate; any branch under the push-b680 prefix that --merged lists and
    the ruling does not name, reported and KEPT. No remote branch is named this act. data/b681_branches.txt (.json)."""
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
            if x.startswith('push-b680') and (repo, x) not in named:
                extra.append((repo, x))
    for r in rows:
        read_branch_row(r)
    nl = sum(1 for r in rows if r['where'] == 'local')
    L = ['b681 -- STEP ZERO, (R291)(9): THE BRANCHES THE RULING NAMES, EACH TIP READ BEFORE ANY DELETE (%s)' % utc(), '',
         '### rows are branches: repository ; branch ; local ; tip ; listed by `git branch --merged main --list <name>` ; fate. Deleted by name in',
         '### the house form, each delete command naming one branch with no glob in any half, one command per call, in sequence; no branch the',
         '### ruling does not name.']
    L += ['  %-24s %-30s %-6s %s ; merged into main %s ; %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'],
                                                               r['fate']) for r in rows]
    L += ['', '### branches under the push-b680 prefix that --merged lists and the ruling does not name (reported and KEPT): %s' % (
        ', '.join('%s %s' % (os.path.basename(r_), b_) for r_, b_ in extra) or 'NONE')]
    L += ['', '### ### **BRANCHES %d (LOCAL %d, REMOTE %d) ; MERGED %d ; TO BE DELETED %d ; UNNAMED UNDER THE PREFIX %d.**' % (
        len(rows), nl, len(rows) - nl, sum(1 for r in rows if r['merged']), len(rows), len(extra))]
    put_txt('b681_branches.txt', L)
    put_json('b681_branches.json', dict(at=utc(), rows=rows, extra=[list(x) for x in extra]))
    print(NL.join(L[5:]))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R291)(1)-(2)
WH = ('*Appended 2026-10-18 by b681 to b680’s entry (:9078), under `(R291)`(1)-(2) -- b680 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b680_closing.txt), AND ITS ROOT REPAIRED:*')
WB = (' “b680 closed: relay 75898036, PLACE-papers 6d8b953; suite 84 of 88; root 764d21d642c8af80…; 4 prompts answered; 8 defects” '
      '(data/b680_closing.txt :1), the closing pushed at relay 21cb2735 (data/b680_closing_push_out.txt :4). The four failing arms named: '
      'G-ACTROOT-VERIFY on the root defect (h); G-ANSWERS-BANKED, G-ANSWERS-CHECKED and G-DEFECTS-LETTERED on counts fixed at the seal and '
      'raised by the post-seal root prompt (d); 0 negative-control failures, 0 positive controls passing; no pre-push reading (g). The readings '
      'beside b670’s: licensed rows 361 against 372; Correspondence 55 behind against 54, the generator’s claim 0 against 0; orders 38 / 49 / 75 '
      'against 34 / 46 / 69; methods 9 of 12 by b670’s code, 12 with the hand-read cells, against b671’s 11; the ceiling sentence and its '
      'successor byte-equal at their three sites each; NOT COMPARABLE: print banks held by 1 of the 9 kernels, residues 5 sentences, keystone '
      'lag 16 of 19 (largest 244, median 96), the outside-reader test; arms 68, SHAPE 39 and VALUE 29; rules 26 in eight banks, 24 with no arm; '
      'archive-3 HELD at 4565 of 4635 line citations; the faces line through the generator; three figures; the mirror CLEAN with the root '
      'line; N1–N5 and S1–S3 HELD; eight defects (a)–(h), (a) and (e) the navigator’s. The root repaired at b681’s step zero: the four banks '
      'of (h) hashed at 75898036 equal to the hashes the root recorded, so a corrigendum row is appended to relay data/act_roots.txt -- the '
      'root value as recorded, no row edited -- and tools/act_root.py reads it; the chain b624-b680 AGREE, 57 of 57 (relay '
      'data/b681_root_repair.txt). Nothing deposited.')


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + WB + NL)], 'b681_record_lines.json', 'c1', entry=K.B680_ENTRY,
         check=[('FINDINGS.md', K.B680_ENTRY, '## Reading 2 of 2'), ('OPEN_TRAILS.md', K.B680_TRAIL, '### b680')], dry=dry)


# ================================================================================ (R291)(4): THE ROOT'S BANKS COMMITTED, THE READING BEFORE THE ROOT
def root_banks_state(banks, rev='HEAD'):
    """(R291)(4), G-ROOT-BANKS-COMMITTED's reading: for every bank the root names, its git status (clean or not), whether HEAD carries it and
    whether HEAD's blob equals the working file; HEAD against the remote main (one ls-remote). Returns a dict the arm and the route read."""
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


# ================================================================================ COMPONENT 4: THE LANDING, (R291)(8)
ORDERS = 'b670_work_orders.txt'
LH1 = ('*Appended 2026-10-18 by b681 beneath b680’s trail record (:14682), under `(R291)`(8) -- `W-ORD-EPSTEIN-BALL-WIDTH` DISCHARGED:*')
LB1 = (' the 163 certified zeros of Q0 narrowed from b671’s half-width 1e-24 to 1e-30 -- the measured h_tol(64) = 3.162e-28 of the map in '
       'the angle form (relay data/b677_tolerance.txt :90) less two decimal orders -- 163 of 163, each by the certification form b671 used '
       'for it (146 by the sign change of Λ_Q on the line, 17 by the quarter count, no (4a) offset needed), in 68 resumable foreground parts, '
       '27,693 s, the longest 471 s, the Bessel bar 2^-200 met at every evaluation; C1 (ten ζ zeros) narrowed and inside, C2 refused (relay '
       'data/b681_narrow.txt, data/b681_narrow_controls.txt, data/b681_hypotheses.txt). Pin: relay data/b681_epstein_zeros_narrowed.json.gz '
       'with data/b681_epstein_zeros_narrowed_hashes.txt, chaining from b671’s bank, which stands as it is beside it. Status DISCHARGED.')
LH2 = ('*Appended 2026-10-18 by b681 beneath it, under `(R291)`(8) -- `W-ORD-MAP-ANGLE-FORM`’s TRIGGER REACHED, SO ENTERED:*')
LB2 = (' its trigger “after W-ORD-EPSTEIN-BALL-WIDTH” (OPEN_TRAILS :14588) is reached by the discharge above; the map in the angle form '
       '(relay tools/b677_epstein_map_angle.py) over the narrowed balls is the candidate of b683, the research act, on the author’s placement, '
       'W-ORD-EPSTEIN-COUNT the alternative; priced at one foreground part (b677’s part 1, 46 s), a copy whose one changed line is the bank’s '
       'name. Status OPEN, trigger: b683, on the author’s placement.')


def c4(*a):
    """(R291)(8): the two lines on OPEN_TRAILS beneath b680's trail record, then their rows appended to the orders bank additively ((R254)(2))."""
    dry = 'dry' in a
    land([('OPEN_TRAILS.md', LH1, NL + LH1 + LB1 + NL), ('OPEN_TRAILS.md', LH2, NL + LH2 + LB2 + NL)], 'b681_record_lines_c4.json', 'c4',
         check=[('OPEN_TRAILS.md', K.B680_TRAIL, '### b680')], dry=dry)
    if dry:
        return
    ls = [x['line'] for x in jl('b681_record_lines_c4.json')['lines']]
    rows = ['### Appended 2026-10-18 by b681 under (R291)(8) (additive, (R254)(2)): W-ORD-EPSTEIN-BALL-WIDTH DISCHARGED, its pin the narrowed bank; '
            'W-ORD-MAP-ANGLE-FORM`s trigger reached, so entered; each Status cell filled and its line its pin.',
            '  %-44s :%d  %s   %-5d %-16s :%d  %s [:%d]' % ('W-ORD-EPSTEIN-BALL-WIDTH', 14264, 'b667', 14, 'DISCHARGED', ls[0],
                                                            'pinned by data/b681_epstein_zeros_narrowed.json.gz', ls[0]),
            '  %-44s :%d  %s   %-5d %-16s :%d  %s [:%d]' % ('W-ORD-MAP-ANGLE-FORM', 14398, 'b671', 10, 'OPEN', ls[1],
                                                            'b683, on the author`s placement', ls[1])]
    p = os.path.join(D, ORDERS)
    old = open(p, 'rb').read()
    sep = NL if old.endswith(b'\n') else NL + NL
    new = old + (sep + NL.join(rows) + NL).encode('utf-8')
    if not new.startswith(old):
        sys.exit('### THE ORDERS BANK APPEND IS NOT ADDITIVE -- NOTHING WRITTEN')
    open(p + '.tmp', 'wb').write(new)
    os.replace(p + '.tmp', p)
    print('  data/%s appended (%d bytes before, %d after)' % (ORDERS, len(old), len(new)))


# ================================================================================ THE ANSWERS BANK (b680's route, carried)
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
    """data/b681_author_answers.txt: every prompt put by the seat in this act (from its ruling's line on), with its options and the answer;
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
    head = ['### b681 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d).' % (
                n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start), '']
    if 'dry' in a:
        print('  prompts: %d ; words: %d (dry: nothing written)' % (n, nw))
        return
    put_txt('b681_author_answers.txt', [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    put_json('b681_author_answers.json', dict(at=utc(), calls=[dict(line=i, id=cid, ts=ts, result_ts=(results.get(cid) or (None, None, None))[2])
                                                               for i, cid, _inp, ts in calls]))
    print('  prompts banked: %d ; words banked: %d' % (n, nw))


# ================================================================================ THE LATE ROUTES (b680's, carried; every row read through READERS)
import b633_record as R3           # noqa: E402
import edit_route as ER            # noqa: E402
RELAY = ROOT
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID
SUBAGENTS = 'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % K.SESSION_ID
R3.SP, R3.SESSION, R3.SESSION_ID = SP, SESSION, K.SESSION_ID
ORDER_ROW = re.compile(r'^  (W-ORD-[A-Z0-9-]+)\s+:(\d+)\s+(b\d+)\s+(\d+)\s+(OPEN|DISCHARGED|ACTED|NOT STATED|CLOSED)\s+:(\d+)\s+(.+?) \[:(\d+)\]$')


def read_order_row(line):
    """a row of data/b670_work_orders.txt: the order, its entry line, its act, its age, its Status, its status line and its trigger or pin;
    returns (order, status, trigger)."""
    m = ORDER_ROW.match(line or '')
    if not m:
        raise ValueError('order row of another shape: %r' % ((line or '')[:120],))
    return m.group(1), m.group(5), m.group(7)


PROGRESS_ROW = re.compile(r'^(POINT|CONTROL|PART) (\{.*\})$')


def read_progress_row(line):
    """a row of data/b681_narrow_progress.txt: its tag and its JSON object; a POINT row carries a kind, an index, a half-width and a reading;
    returns (tag, object)."""
    m = PROGRESS_ROW.match(line or '')
    if not m:
        raise ValueError('progress row of another shape: %r' % ((line or '')[:120],))
    o = json.loads(m.group(2))
    if m.group(1) == 'POINT' and not (o.get('kind') in ('ON', 'OFF') and isinstance(o.get('idx'), int) and o.get('h') and o.get('reading')):
        raise ValueError('a POINT row without its kind, index, half-width or reading')
    return m.group(1), o


READERS += ['read_order_row', 'read_progress_row']


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
    """(R291)(9): a delete command names one branch and carries no glob in any half: (the branches it deletes, any glob character)."""
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
    L = ['b681 -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING, THE LOCAL LEAN READING (N1), THE DETACHED RUNS (N3), THE MOVES AND DELETES (%s)' % utc(), '',
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
    L += ['', '### THE BRANCH DELETES BY SHAPE ((R291)(9): one branch per command, no glob in any half): ' + '; '.join(
        '#%d deletes %s, globs %s' % (n, d, gl or 'none') for n, d, gl in shapes)]
    L += ['', '### EVERY COMMAND (n | time | source | tool | first line, 160 characters):']
    L += ['  #%d | %s | %s | %s | %s' % (r['n'], r['ts'], r['src'], r['tool'], r['cmd'].split(NL)[0][:160]) for r in rows]
    L += ['', '### ### **COMMANDS %d ; G-EDIT-ROUTE OFFENCES %d ; LOCAL lean OR lake COMMANDS %d ; DISPATCHES %d ; DETACHED RUNS %d ; MOVE OR DELETE '
              'COMMANDS %d ; BRANCH DELETES OF ONE BRANCH AND NO GLOB %d OF %d.**' % (len(rows), len(hits), len(lean), len(disp), len(detach), len(mv),
                                                                                   sum(1 for _n, d, gl in shapes if len(d) == 1 and not gl), len(shapes))]
    put_txt('b681_commands.txt', [l.replace('\r', '') for l in L])
    put_json('b681_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                        local_lean=[r['n'] for r in lean], dispatches=[r['n'] for r in disp], detached=[r['n'] for r in detach],
                                        moves_deletes=[r['n'] for r in mv], delete_shapes=[dict(n=n, deletes=d, globs=gl) for n, d, gl in shapes]))
    print(L[-1])
    for r, o in hits:
        print('  OFFENCE #%d %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))


def _kerns():
    import b641_record as R41
    return list(R41.KERNS_READ) + ['SIDE-window', 'SIDE-trivium', 'SIDE-silence-principle']


def kernels(*a):
    ks = list(_kerns())
    put_json('b681_kernels_face.json', dict(at=utc(), kernels=R3.kern_state(ks)))
    print('  kernels read: %d (SIDE-explicit-formula among them: the narrowing act writes no kernel)' % len(ks))


DEFECT_ROW = re.compile(r"^    \(([a-z]'?)\) ")


def _defect_short():
    out = []
    L = rdn('b681_defects.txt').split(NL)
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
    t = rdn('b681_defects.txt')
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    put_json('b681_defects.json', dict(at=utc(), defects=ds, short=_defect_short()))
    print('  defects %d' % len(ds))


def seal_hashes():
    import hashlib
    rec_ = jl('b681_seal_hashes.json').get('tools') or {} if os.path.isfile(os.path.join(D, 'b681_seal_hashes.json')) else {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


REPAIRS = [
    ('ACT_ROOT READS A CORRIGENDUM ROW (answering b680`s defect (h), under (R291)(2)): tools/act_root.py`s last_root and the chain read past a',
     'row opening `corrigendum`, and verify reads the banks it names at its corrected commit after checking its act, recorded commit, root,',
     'ancestry and banks (data/b681_rules.txt row (1)); the diff against b680`s tree below; sealed with this act`s tools.'),
    ('THE COUNT ARMS READ THEIR COUNTS FROM THE BANKS AT HEAD WITH THE SEALED FIGURE AS A FLOOR (answering b680`s defect (d), under (R291)(3)):',
     'tools/b681_checks.py G-ANSWERS-BANKED, G-ANSWERS-CHECKED and G-DEFECTS-LETTERED; a post-seal prompt named on the face',
     '(data/b681_rules.txt row (2)).'),
    ('G-ROOT-BANKS-COMMITTED, THE ONE STANDING ARM ADDED (under (R291)(4)): tools/b681_checks.py reads the root route`s banked reading',
     '(data/b681_root_banks.json: every named bank clean and equal at HEAD, HEAD the remote main) and every named bank`s blob at the root`s',
     'recorded commit against the hash the root recorded; tools/b681_record.py root refuses before computing where the reading is not',
     'clean (data/b681_rules.txt row (3)).'),
]


def repairs(*a):
    """data/b681_tool_repairs.txt: rows are repairs with the defect they answer. Each tool carried from a sealed b680 copy is read against
    b680's seal hash (relay data/b680_seal_hashes.json) first, and its diff against that copy counted by hunks; act_root.py's diff against
    b680's tree printed whole."""
    import hashlib
    seal = jl('b680_seal_hashes.json').get('tools') or {}
    rows = []
    for t0 in ('b680_citation.py', 'b680_closing.py', 'b680_reg_gate.py', 'b680_regspec.py', 'b680_tests.py', 'b680_worklist.py',
               'b680_record.py', 'b680_checks.py'):
        t1 = t0.replace('b680_', 'b681_')
        old, new = os.path.join(T, t0), os.path.join(T, t1)
        now = hashlib.sha256(open(old, 'rb').read()).hexdigest()
        d = subprocess.run(['git', 'diff', '--no-index', '--unified=0', old, new], capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
        rows.append((t0, t1, now, seal.get(t0), len(re.split(r'(?m)^(?=@@ )', d)[1:])))
    ad = subprocess.run(['git', '-C', ROOT, 'diff', K.PRE_RELAY, '--', 'tools/act_root.py'], capture_output=True, text=True, encoding='utf-8',
                        errors='replace').stdout
    L = ['b681 -- COMPONENT 5, (R291)`S FERRY: THE CARRY-TIME READING OF THE TOOLS, AGAINST b680`S SEALED COPIES (%s)' % utc(), '',
         '### rows are the carried tools: b680`s sealed copy and its seal record; the hunks of the diff to b681`s copy. Every hunk is the act`s own',
         '### text -- its names, its banks, its sections and its predicates over this act`s banks -- save the repairs below, each with the defect',
         '### it answers.', '']
    for t0, t1, now, s, nh in rows:
        L.append('  %-20s -> %-20s b680 sealed %s ; the seal`s record %s ; %s ; hunks %d' % (t0, t1, now[:16], (s or '### NONE')[:16],
                                                                                     'AGREE' if s == now else '### DIFFER', nh))
    L.append('')
    for i, r in enumerate(REPAIRS, 1):
        L += ['  REPAIR %d -- %s' % (i, r[0])] + ['  ' + x for x in r[1:]]
    L += ['', '### tools/act_root.py, its diff against relay %s (b680`s closing), whole:' % K.PRE_RELAY] + ['    ' + x for x in ad.rstrip(NL).split(NL)]
    L += ['', '### ### **REPAIRS %d ; THE SEALED COPIES %s ; TOOLS CARRIED %d ; act_root.py REPAIRED, SEALED WITH THE ACT`S TOOLS.**' % (
        len(REPAIRS), 'AGREE' if all(s == now for _a, _b, now, s, _n in rows) else '### DIFFER', len(rows))]
    put_txt('b681_tool_repairs.txt', L)
    print(L[-1])


ROOT_EXCLUDE = re.compile(r'^b681_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise.*|findings|trail|closing.*|'
                          r'act_root.*|root_arm.*|root_banks.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|'
                          r'commands|mirror.*|narrow_units\.jsonl)\.?(txt|json|md|)$')
BINARY = ('.gz', '.png')


def root_banks():
    return sorted(['data/' + f for f in os.listdir(D) if f.startswith('b681_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f)
                   and not f.endswith(BINARY) and f != 'b681_narrow_units.jsonl'] + list(K.SHARED_APPENDED))


def rootbanks(*a):
    """(R291)(4): G-ROOT-BANKS-COMMITTED's reading, banked before the root: every bank the root route names, its status and its blob at
    HEAD against the working file; HEAD against the remote main. data/b681_root_banks.txt (.json)."""
    banks = root_banks()
    s = root_banks_state(banks)
    L = ['b681 -- (R291)(4): THE ROOT`S BANKS, READ BEFORE THE ROOT (%s): rows are the banks the root route names -- status ; carried by HEAD ;'
         ' HEAD`s blob equal to the file' % utc(), '', '### HEAD %s ; the remote main %s ; equal %s' % (s['head'], s['remote'], s['pushed']), '']
    L += ['  %-52s %-6s at HEAD %-5s equal %s' % (r['bank'], r['status'], r['at_head'], r['equal']) for r in s['rows']]
    L += ['', '### ### **BANKS %d ; CLEAN AND EQUAL AT HEAD %d ; HEAD THE REMOTE MAIN %s ; READY %s.**' % (
        len(s['rows']), sum(1 for r in s['rows'] if r['status'] == 'clean' and r['equal']), s['pushed'], s['clean'] and s['pushed'])]
    put_txt('b681_root_banks.txt', L)
    put_json('b681_root_banks.json', dict(at=utc(), **s))
    print(L[-1])
    return s['clean'] and s['pushed']


def root(*a):
    banks = root_banks()
    crlf = [b_ for b_ in banks if b'\r\n' in open(os.path.join(ROOT, *b_.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/b681_seal_hashes.json' in banks, crlf or 'none'))
    if crlf:
        sys.exit('### A BANK THE ROOT WOULD NAME IS CR LF -- NOTHING WRITTEN')
    if not rootbanks():
        sys.exit('### (R291)(4): A NAMED BANK IS NOT COMMITTED AND PUSHED AT HEAD -- NO ROOT')
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b681'] + banks + ([] if 'dry' in a else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import tempfile
    import act_root as AR
    J = jl('b681_act_root.json')
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/') and not it.split()[0].endswith(BINARY)][0]
    with tempfile.TemporaryDirectory(prefix='b681_ra_') as tmp:
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
    L = ['b681 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '?')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b681_root_arm.txt', L)
    put_json('b681_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
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
    L = ['b681 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (utc(), r.returncode, g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b681_table_final.txt', L)
    put_json('b681_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


FACE_REL = 'data/b681_registration_2026-10-18.txt'
FACE = os.path.join(D, 'b681_registration_2026-10-18.txt')


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
    rc1, t1 = runb([os.path.join(T, 'banned_terms.py'), '--new', FACE_REL], 'b681_reg_termscan.txt')
    rc2, t2 = runb([os.path.join(T, 'b681_regspec.py')], 'b681_regspec_run.txt')
    rc3, t3 = runb([os.path.join(T, 'reg_satisfiable.py'), 'data/b681_satisfiable.json', '--emit', 'b681'], None)
    print('  banned_terms rc %d ; %s' % (rc1, ([l for l in t1.split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    print('  regspec rc %d ; %s' % (rc2, ([l for l in t2.split(NL) if 'PREDICTIONS FOUND' in l] or ['### NONE'])[0].strip()))
    print('  reg_satisfiable rc %d ; %s' % (rc3, ([l for l in rdn('audit_b681_reg_satisfiable.txt').split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    for tool, out in (('b307_handoff_census.py', 'b681_census_stepzero.txt'), ('b327_faces_census.py', 'b681_faces_census_stepzero.txt'),
                      ('b303_pins.py', 'b681_pins_stepzero.txt')):
        rc, t = runb([os.path.join(T, tool), 'b681'], out)
        print('  %s rc %d ; %s' % (out, rc, ([l.strip() for l in t.split(NL) if 'TOTAL MISSING' in l or 'HARD-FAILING' in l] or ['### NONE'])[0][:120]))
    for r in ('data/b681_reg_gate.txt', 'data/b681_reg_termscan.txt', 'data/b681_regspec_run.txt', 'data/audit_b681_reg_satisfiable.txt'):
        ra = os.path.join(ROOT, *r.split('/'))
        print('  stamp %s %s %s' % (r, G.stamp(ra, FACE)[:16], G.matches(ra, FACE)[0]))


# ================================================================================ THE SCORES: (N1)-(N5) OF THE FERRY, THE SEAT'S (S1)-(S3)
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3')
SCORE_KEYS = NK + SK
N5_RELAY_DATA = ('act_roots.txt', 'b680_closing_push_out.txt', 'b670_work_orders.txt')
N5_RELAY_TOOLS = ('act_root.py',)
N5_PP = ('FINDINGS.md', 'OPEN_TRAILS.md')
VL = re.compile(r'### ### \*\*(.*?)\*\*')


def TRAIL_HEAD():
    return ('### b681 — lane two, act one hundred and eight, the narrowing act under (R291): the 163 zeros of Q0 narrowed to 1e-30 in resumable '
            'foreground parts, the b680 root chain repaired by corrigendum, G-ROOT-BANKS-COMMITTED declared')


def _calls():
    return jl('b681_author_answers.json').get('calls') or []


def _ledger_adds():
    d = g(PP, 'diff', '--unified=0', K.PRE_PP, '--', 'FINDINGS.md', 'OPEN_TRAILS.md')
    return NL.join(l[1:] for l in d.split(NL) if l.startswith('+') and not l.startswith('+++'))


def _git_ct(repo, rev):
    t = g(repo, 'log', '-1', '--format=%ct', rev).strip()
    return int(t) if t.isdigit() else None


def _iso(s):
    import calendar
    try:
        return calendar.timegm(time.strptime(s, '%Y-%m-%dT%H:%M:%SZ'))
    except Exception:
        return None


def _progress():
    out = []
    for l in rdn('b681_narrow_progress.txt').split(NL):
        if l.strip():
            out.append(read_progress_row(l))
    return out


def _n1():
    cm = jl('b681_commands.json')
    ok = bool(cm) and not cm.get('local_lean') and not cm.get('dispatches')
    return ('HELD' if ok else 'REFUTED'), (
        'commands of this act that run lean or lake on this host: %s; runner dispatches %d (relay data/b681_commands.txt, %d commands read)' % (
            cm.get('local_lean') if cm else '### UNREAD', len(cm.get('dispatches') or []), len(cm.get('rows') or [])))


def _n2():
    v = rdn('b681_chain_verify_standing-b.txt')
    m = re.search(r'THE ACT-ROOT CHAIN, recomputed: (.*)$', v, re.M)
    rows_ = re.findall(r'(b\d{3}) (AGREE|DISAGREE)', m.group(1)) if m else []
    t_v = re.search(r'run at \(UTC\) : (\S+)', v)
    t_v = _iso(t_v.group(1)) if t_v else None
    t_c = _iso(jl('b681_citation_check.json').get('at') or '')
    rr = rdn('b681_root_repair.txt')
    ok = [a_ for a_, _v in rows_] == ['b%d' % i for i in range(624, 681)] and all(v_ == 'AGREE' for _a, v_ in rows_) and t_v and t_c and t_v < t_c \
        and 'EQUAL AT 75898036 4' in rr and 'corrigendum b680 42d26968' in rdn('act_roots.txt')
    return ('HELD' if ok else 'REFUTED'), (
        'the chain recomputed inside the suite before any bank of this act: %d rows, AGREE %d, b624 to b680 (relay data/b681_chain_verify_standing-b.txt '
        ':10, run before the citation check`s bank); the four banks EQUAL at 75898036 and the corrigendum row appended (relay data/b681_root_repair.txt); '
        'the prompt of (R291)(2)(iii) not reached' % (len(rows_), sum(1 for _a, v_ in rows_ if v_ == 'AGREE')))


def _n3():
    P = _progress()
    plan_ct = _git_ct(RELAY, '1c714457')
    first = min((_iso(o['at']) for t, o in P if o.get('at')), default=None)
    parts = [o for t, o in P if t == 'PART']
    cm = jl('b681_commands.json')
    pl = rdn('b681_narrow_plan.txt')
    ok = plan_ct and first and plan_ct < first and parts and max(p['seconds'] for p in parts) <= 600 and not cm.get('detached') \
        and 'W = 1e-30' in pl and '265,376 process-seconds' in pl
    return ('HELD' if ok else 'REFUTED'), (
        'the plan (relay data/b681_narrow_plan.txt, committed 1c714457) prints the target with its source rows and the price from b671`s run '
        'records before the first point (the plan`s commit before the first progress row %s); %d parts, the longest %d s, summed %d s; detached '
        'runs %s (relay data/b681_commands.txt)' % (bool(plan_ct and first and plan_ct < first), len(parts), max([p['seconds'] for p in parts] or [0]),
                                                   sum(p['seconds'] for p in parts), cm.get('detached') if cm else '### UNREAD'))


def _n4():
    import hashlib
    nt, ct, ht = rdn('b681_narrow.txt'), rdn('b681_narrow_controls.txt'), rdn('b681_epstein_zeros_narrowed_hashes.txt')
    rows_ = re.findall(r'^  (ON|OFF) +\d+ +form (M-on|M-off)', nt, re.M)
    gz = open(os.path.join(D, 'b681_epstein_zeros_narrowed.json.gz'), 'rb').read() if os.path.exists(os.path.join(D, 'b681_epstein_zeros_narrowed.json.gz')) else b''
    ok = len(rows_) == 163 and 'NARROWED TO 1e-30 163 OF 163' in nt and 'FORMS AS b671`S True' in nt and K.NARROW_IN_HASHES[0] in nt \
        and hashlib.sha256(gz).hexdigest() in ht and K.NARROW_IN_HASHES[0] in ht and 'C1 10 OF 10 NARROWED TO 1e-30 AND INSIDE ; C2 REFUSED True' in ct
    return ('HELD' if ok else 'REFUTED'), (
        'every point`s final half-width and form printed: %d rows (relay data/b681_narrow.txt), "%s"; the chain at both ends: b671`s hashes read '
        'before any point, the new .gz`s sha256 in its hashes bank with b671`s named; the controls: "%s" (relay data/b681_narrow_controls.txt)' % (
            len(rows_), (VL.findall(nt) or ['### UNREAD'])[-1][:120], (VL.findall(ct) or ['### UNREAD'])[-1]))


def _n5():
    face = jl('b681_kernels_face.json').get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    k_ok = bool(face) and all(now[k] == list(v) for k, v in face.items()) and g(K.KE, 'rev-parse', '--short=7', 'main').strip() == K.K_MAIN
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in N5_PP]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b681_|audit_b681_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('data/') and x[5:] in N5_RELAY_DATA)
                                                or (x.startswith('tools/') and x[6:] in N5_RELAY_TOOLS))]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    import importlib
    argv, sys.argv = sys.argv, sys.argv[:1]
    try:
        CH = importlib.import_module('b681_checks')
    finally:
        sys.argv = argv
    new_arms = sorted(set(a_[0] for a_ in CH.ARMS) - set(CH.STANDING) - set(K.ACT_ARMS) - set(K.STANDING_ADDED))
    pat = [n for n in ('patent', 'Patent', 'PATENT') if n in _ledger_adds()]
    ok = k_ok and not pp_beyond and not kinds_beyond and not differ and not new_arms and not pat
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unpublished); no kernel main written, every kernel as the face read it '
            '(SIDE-explicit-formula at %s among them) %s; PLACE-papers beyond FINDINGS and OPEN_TRAILS: %s; standing arms added beyond '
            'G-ROOT-BANKS-COMMITTED: %s (the act`s arms over its own banks %d); sealed tools not agreeing %s; relay files of a kind beyond the '
            'narrowing tool, the act`s banks and tools, the table, the root list, b680`s push-out bank, the orders bank`s rows and act_root.py`s '
            'repair: %s; "patent" in the lines written: %s; outbound requests: the seat`s git reads and pushes at github.com, so no identifier of the '
            'author placed in a request; the mirror zip outside every repository' % (K.DRAFT, K.K_MAIN, k_ok, pp_beyond or 'NONE', new_arms or 'NONE',
                                                                                    len(K.ACT_ARMS), differ or 'NONE', kinds_beyond or 'NONE', pat or 'NONE'))


def scores(*a):
    TF, RA = jl('b681_table_final.json'), jl('b681_root_arm.json')
    _r, _n, sh = seal_hashes()
    S = {
        'N1': _n1(), 'N2': _n2(), 'N3': _n3(), 'N4': _n4(), 'N5': _n5(),
        'S1': (('HELD' if not TF.get('gone') and not TF.get('grade_moved') else 'REFUTED') if TF else 'PENDING',
               'the table at the end against relay HEAD`s: moved %s, gone %s, added %s, grade moved %s' % (
                   len(TF.get('moved') or []), len(TF.get('gone') or []), len(TF.get('added') or []), len(TF.get('grade_moved') or []))),
        'S2': (('HELD' if RA.get('root_recomputed') == RA.get('root') and RA.get('root_copy') != RA.get('root') and not RA.get('late') else 'REFUTED')
               if RA else 'PENDING', 'the root recomputed equal, the one-byte control moving it, the root order holding locally'),
        'S3': ('HELD' if sh and all(v == 'agree' for _t, v in sh) else ('PENDING' if all(v == 'absent' for _t, v in sh) else 'REFUTED'),
               'the sealed tools` hashes %s' % dict(collections.Counter(v for _t, v in sh))),
    }
    for k2 in SCORE_KEYS:
        read_score_row(k2, list(S[k2]))
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:700]))
    if 'dry' in a:
        return
    put_json('b681_scores.json', dict((k2, list(v)) for k2, v in S.items()))


def _sv(S, k):
    return read_score_row(k, S.get(k) or ['?', ''])[1] if S.get(k) else 'PENDING'


def _rl_lines(*banks):
    out = []
    for b_ in banks:
        out += [x.get('line') for x in jl(b_).get('lines') or []]
    return out


def _figs():
    nt = rdn('b681_narrow.txt')
    m = re.search(r'NARROWED TO 1e-30 (\d+) OF 163 ; FORMS AS b671`S (\w+) ; PARTS (\d+), (\d+) s ; THE LONGEST PART (\d+) s ; BESSEL BAR MISSES (\d+)', nt)
    return dict(n=m.group(1), forms=m.group(2), parts=m.group(3), secs=m.group(4), longest=m.group(5), miss=m.group(6)) if m else \
        dict(n='?', forms='?', parts='?', secs='?', longest='?', miss='?')


def _title():
    f = _figs()
    return ('## The 163 certified zeros of Q0 narrowed to half-width 1e-30: %(n)s of 163 reached; forms unchanged; %(parts)s foreground parts, '
            '%(secs)s s; the b680 root chain repaired by corrigendum; G-ROOT-BANKS-COMMITTED declared' % f)


def _finding_text():
    S, J = jl('b681_scores.json'), jl('b681_act_root.json')
    f = _figs()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b681_author_answers.txt'), re.M))
    c1 = _rl_lines('b681_record_lines.json') + ['?']
    c4 = _rl_lines('b681_record_lines_c4.json') + ['?', '?']
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    e = ['', _title(), '',
         'Every one of Q0’s 163 certified zeros now sits in a certified ball of half-width 1e-30, a million times finer than b671’s 1e-24, and '
         'two decimal orders under the width the map in the angle form measured it needs at j = 64 (3.162e-28): the 146 on the line by the '
         'certified sign change of the completed function, the 17 off it by the quarter count, each by the form b671 used for it, in %(parts)s '
         'foreground parts that each ended before 600 s and left no process behind. Nothing here proves RH or GRH.' % f, '',
         '*Filed at b681 on the author’s ruling `(R291)`%s. Banks: relay `data/b681_narrow_plan.txt`, `data/b681_narrow.txt`, '
         '`data/b681_narrow_controls.txt`, `data/b681_hypotheses.txt`, `data/b681_epstein_zeros_narrowed_hashes.txt`, `data/b681_root_repair.txt`, '
         '`data/b681_act_root.txt`; the tool `tools/b681_narrow.py`.*' % ((' and the navigator’s answers (%d questions)' % n_ans) if n_ans else ''), '',
         '**The citation check** (the gate step from b662): %s cites checked at HEAD, %s OK, %s missed. b680 at its weight (FINDINGS :%s).' % (
             cc.group(1) if cc else '?', cc.group(2) if cc else '?', cc.group(3) if cc else '?', c1[0]), '',
         '**The root repair** (`(R291)`(2)): the four banks of b680’s defect (h) hashed at 75898036, each equal to the hash b680’s root recorded, so '
         'a corrigendum row is appended to relay data/act_roots.txt, the root value as recorded and no row edited; tools/act_root.py reads it, '
         'and the chain verifies b624 to b680, 57 of 57.', '',
         '**The arm** (`(R291)`(4)): G-ROOT-BANKS-COMMITTED, the one standing arm added -- every bank the root names committed and pushed at the '
         'commit the root records, the reading banked before the root.', '',
         '**The plan and the run** (`(R291)`(6)-(7)): the target 1e-30 from b677’s measured tolerance less two decimal orders; the price read from '
         'b671’s run records, 72 parts; the run took %(parts)s parts and %(secs)s s, the longest %(longest)s s, the unit a segment of a side of a '
         'square so no part waited on a depth; no (4a) offset needed; the Bessel bar 2^-200 met at every evaluation (misses %(miss)s); C1 ten ζ '
         'zeros narrowed and inside, C2 refused; the chain verified from b671’s bank to the new one.' % f, '',
         '**The landing** (`(R291)`(8)): `W-ORD-EPSTEIN-BALL-WIDTH` DISCHARGED (OPEN_TRAILS :%s), its pin the new bank; `W-ORD-MAP-ANGLE-FORM`’s '
         'trigger reached, so entered (OPEN_TRAILS :%s).' % (c4[0], c4[1]), '',
         '**The root.** b681 over %d repositories, %d tags and %d banks, the last step of the act’s banks; its chain read at commit inside the suite.' % (
             len((J.get('reads') or {}).get('heads') or []), len((J.get('reads') or {}).get('tags') or []), len((J.get('reads') or {}).get('banks') or [])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): this act re-reads b671’s narrowing and b677’s tolerance against the consumer, and is '
         're-read by the act that runs the map in the angle form over the new balls. It strengthens the programme’s offerings of a certified '
         'object whose width is set by its consumer’s measured need, and of a root chain that repairs a defect by appending.', '',
         '**Carried to:** the map in the angle form over the narrowed balls (`W-ORD-MAP-ANGLE-FORM`, b683’s candidate); T-COUNT for Q0 '
         '(`W-ORD-EPSTEIN-COUNT`); the 24 rules without arms, for the author’s decision; the draft held at v5.', '',
         '**Next.** %s.' % K.NEXT, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


FOR_AUTHOR = ('(1) the margin read in b671’s own form, two decimal orders under h_tol(64) rounded down to the power of ten, so W = 1e-30; (2) the '
              'resumable unit a segment of a side of a square, so a part never waits on a depth b671 measured at up to 3,407 s; (3) a part that '
              'starts beneath the memory hold refuses and writes nothing; (4) the corrigendum row given its own first token, so no reader of the '
              'chain takes it for an act')


def _trail_text():
    S, J = jl('b681_scores.json'), jl('b681_act_root.json')
    fj = jl('b681_findings.json')
    f = _figs()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b681_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    c1 = _rl_lines('b681_record_lines.json') + ['?']
    c4 = _rl_lines('b681_record_lines_c4.json') + ['?', '?']
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R291) ratified.** (1) b680 at its weight. (2) The root repair. (3) The count arms. (4) The one standing arm. (5) The object. (6) The '
             'plan. (7) The run. (8) The landing. (9) The branches. (10) The read-first bank. (11) The draft held at v5. (12) The acts after.', '',
             '**Entered:** FINDINGS.md:%s (b680’s weight), :%s (the entry); OPEN_TRAILS.md:%s (`W-ORD-EPSTEIN-BALL-WIDTH` DISCHARGED), :%s '
             '(`W-ORD-MAP-ANGLE-FORM`, OPEN, trigger b683); relay data/act_roots.txt the corrigendum row for b680; this record.' % (
                 c1[0], fj.get('entry_line'), c4[0], c4[1]), '',
             '**Act root:** b681 `%s` (previous `%s`, b680’s as recorded; relay data/act_roots.txt), computed after the last bank it names, every one '
             'of them LF and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d questions in %d call%s (relay data/b681_author_answers.txt); none after the root.' % (
                 n_ans, len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The run:** 163 of 163 at 1e-30 (relay data/b681_narrow.txt); %(parts)s parts, %(secs)s s, the longest %(longest)s s; Bessel bar misses '
             '%(miss)s; controls C1 10 of 10, C2 refused (relay data/b681_narrow_controls.txt).' % f, '',
             '**The mirror:** the export made after this root in the b670 form, its name in the closing (relay data/b681_closing.txt).', '',
             '**The open orders:** `W-ORD-MAP-ANGLE-FORM` (b683, on the author’s placement); `W-ORD-EPSTEIN-COUNT` (the alternative); '
             '`W-ORD-CORRESPONDENCE-RUNNER-BANKS` (b682, the re-cut act); `W-ORD-LEDGER-SPLIT-RESOLVER` (on the author’s word); '
             '`W-ORD-CHAIN-PAGE-B638-CASES`; `W-ORD-PRINT-TARGETS`; `W-ORD-ONE-COPY`; `W-ORD-TABLE-SHAPE`; `W-ORD-GRADE-MOVED`; '
             '`W-ORD-ABSENT-DECLARATIONS`; `W-ORD-PROSE-PINS`; `W-ORD-ROOT-BINARY-BANK`.', '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b681_defects.txt): %s.' % ('; '.join(_defect_short()) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.**', '',
             '**Next:** %s.' % K.NEXT, '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b681_scores.json')
    L = ['=' * 104, 'b681 -- THE DESK.', '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in SCORE_KEYS]
    L += [''] + rdn('b681_defects.txt').rstrip(NL).split(NL)
    put_txt('b681_desk_notes.txt', L)


def components(*a):
    S, fj, tj, J = (jl(n_) for n_ in ('b681_scores.json', 'b681_findings.json', 'b681_trail.json', 'b681_act_root.json'))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    c1 = _rl_lines('b681_record_lines.json') + ['?']
    c4 = _rl_lines('b681_record_lines_c4.json') + ['?', '?']
    L = ['b681 -- THE COMPONENTS, BANKED UNDER (R291).', '',
         '### COMPONENT 0 : the root repair (data/b681_root_repair.txt), the citation check (data/b681_citation_check.txt), step zero '
         '(data/b681_ferry.txt, data/b681_readfirst.txt, data/b681_stepzero.txt, data/b681_tests_stepzero.txt, data/b681_rowgen_stepzero.txt, '
         'data/b681_branches.txt) ; N2 %s' % S['N2'][0],
         '### COMPONENT 1 : b680`s weight FINDINGS :%s ; the rules bank (data/b681_rules.txt) ; the count arms and G-ROOT-BANKS-COMMITTED in the suite' % c1[0],
         '### COMPONENT 2 : the plan (data/b681_narrow_plan.txt), tools/b681_narrow.py alone, one prompt ; N3 %s' % S['N3'][0],
         '### COMPONENT 3 : the run (data/b681_narrow_progress.txt, data/b681_narrow.txt, data/b681_narrow_controls.txt, data/b681_hypotheses.txt) ; N1 %s ; N4 %s' % (
             S['N1'][0], S['N4'][0]),
         '### COMPONENT 4 : W-ORD-EPSTEIN-BALL-WIDTH DISCHARGED OPEN_TRAILS :%s ; W-ORD-MAP-ANGLE-FORM entered :%s' % (c4[0], c4[1]),
         '### COMPONENT 5 : the carry-time reading (data/b681_tool_repairs.txt), the dry-run steps (data/b681_reg_gate.txt), the seal '
         '(data/b681_seal_hashes.json), the suite ; S3 %s' % S['S3'][0],
         '### COMPONENT 6 : the root %s ; FINDINGS :%s ; OPEN_TRAILS :%s ; the mirror after the root ; N5 %s' % (
             (J.get('root') or '')[:16], fj.get('entry_line'), tj.get('line'), S['N5'][0])]
    put_txt('b681_components.txt', L)
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
    ln = _land_one(FIND, t, e, 'b681_findings.json', dict(title=t))
    j = jl('b681_findings.json')
    j['entry_line'] = ln
    put_json('b681_findings.json', j)
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
    ln = _land_one(OT, TRAIL_HEAD(), e, 'b681_trail.json', {})
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


# ================================================================================ THE MIRROR, AT THE CLOSE (the b670 form, b680's routes, carried)
import hashlib as _hl              # noqa: E402
MIRROR_TAG = '2026-10-18-b681'
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
    put_json('b681_mirror_build.json', dict(at=utc(), rc=r.returncode, out=r.stdout, err=r.stderr, seconds=int(time.time() - t0), pp_head=loc))
    print(r.stdout[-800:], r.stderr[-400:], 'exit', r.returncode)


def mroot(*a):
    last = [l for l in io.open(os.path.join(D, 'act_roots.txt'), encoding='utf-8').read().split(NL) if l.strip()][-1].split()
    if last[0] != 'b681':
        sys.exit('### THE ROOTS FILE`S LAST LINE IS %s, NOT b681`s -- NOTHING WRITTEN' % last[0])
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
    put_json('b681_mirror_root.json', dict(at=utc(), line=line, bom=bom, zip_sha_before=before, zip_sha_after=after, update_rc=ps.returncode))
    print('  %s ; update rc %d ; zip sha256 %s -> %s' % (line, ps.returncode, before[:16], after[:16]))


def mverify(*a):
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'mirror_verify.py'), ZIP, 'origin', 'main'], cwd=PP,
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    put_txt('b681_mirror_verify.txt', (r.stdout + r.stderr + '### exit %d' % r.returncode).replace(chr(13), '').split(NL))
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
    clean = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in rdn('b681_mirror_verify.txt')
    nd = R6.nd_hits(NL.join(names), R6.nd_sets())[0]
    files_ = [n for n in names if n != 'MANIFEST.md']
    pp_head = g(PP, 'rev-parse', '--short=7', 'HEAD').strip()
    L = ['b681 -- THE MIRROR-REFRESH EXPORT, BUILT AFTER THE ROOT AND THE LAST PLACE-papers PUSH BY THE UNEDITED BUILDER, banked %s' % utc(),
         '### THE ZIP : %s ; %d bytes ; md5 %s ; sha256 %s' % (ZIP, len(zb), _hl.md5(zb).hexdigest(), _hl.sha256(zb).hexdigest()),
         '### THE MANIFEST : md5 %s ; entries in the zip %d (files %d + MANIFEST)' % (_hl.md5(man).hexdigest(), len(names), len(files_)),
         '### PLACE-papers HEAD AT THE BUILD : %s ; the last commit carried in MANIFEST`s rows %s' % (pp_head, pp_head in commits),
         '### THE ROSTER LINE : %s' % (' / '.join(rosterl) or '### NONE'), '### THE ROOT LINE : %s' % (rootl[0] if rootl else '### NONE'),
         '### THE SPAN: every roster and ledger change of b681 (the last export b680`s, D:/MY-DOwnloads/mirror-refresh-2026-10-17-b680.zip)',
         '### THE VERIFICATION : %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
         '### THE NO-DISCLOSURE ARM OVER THE FILE LIST: %s' % dict(nd), '### THE FILE LIST:'] + ['    %s' % n for n in names]
    put_txt('b681_mirror.txt', L)
    put_json('b681_mirror.json', dict(at=utc(), zip=ZIP, zip_md5=_hl.md5(zb).hexdigest(), zip_sha256=_hl.sha256(zb).hexdigest(), bytes=len(zb),
                                      manifest_md5=_hl.md5(man).hexdigest(), entries=len(names), files=len(files_), roster_line=rosterl,
                                      root_line=rootl[0] if rootl else '', clean=clean, nd=dict(nd), pp_head=pp_head, last_commit_in_manifest=pp_head in commits))
    for l in L[:9]:
        print(l[:240])


ROUTES = {'rowgen': rowgen, 'branches': branches, 'c1': c1, 'c4': c4,
          'mbuild': mbuild, 'mroot': mroot, 'mverify': mverify, 'mbank': mbank,
          'answers': answers, 'commands': commands, 'kernels': kernels, 'defects': defects, 'repairs': repairs,
          'rootbanks': rootbanks, 'root': root, 'root_arm': root_arm, 'table_final': table_final, 'gatebanks': gatebanks, 'scores': scores,
          'desk': desk, 'components': components, 'findings': findings, 'trail': trail, 'drycheck': drycheck}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b681_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
