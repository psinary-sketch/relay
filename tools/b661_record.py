# -*- coding: utf-8 -*-
"""b661_record.py -- THE ACT'S RECORD TOOL, b661 under (R271).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b661's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows can run each reader over one row of each shape before the seal.
### Carried by the Write tool from b659_record.py (the landing and its screens, the readers' form, the record lines); the routes of the later
### components are added to this file by the Edit tool before the seal, each run before the face names it.
### Routes: `python tools/b661_record.py <route> [dry]`; each route banks under data/ and prints what it wrote.
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
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf/scratchpad'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from b652_record import conv, append_to, guard_absent, line_of, odd_lines   # noqa: E402,F401  ### the one conversion, imported
import b661_worklist as K          # noqa: E402

STANDIN = bool(os.environ.get('B661_STANDIN'))


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
    sk = ('N1', 'N2', 'N3', 'N4', 'N5', 'H1', 'H2', 'H3', 'H4', 'S1', 'S2', 'S3')
    return {
        'b661_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b661_findings.json': dict(entry_line=99999, title='stand-in'),
        'b661_trail.json': dict(line=99999),
        'b661_act_root.json': dict(root='0' * 64, previous='c147a36e' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
    }


def jl(name):
    try:
        return json.load(io.open(os.path.join(D, name), encoding='utf-8'))
    except Exception:
        return _standins().get(name, {}) if STANDIN else {}


def g(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def _ws(s):
    return ' '.join(s.split())


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b661's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b661_scanfile_%s.md' % tag)
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
    """a scores row: key N1..N5, H1..H4 or S1..S3, value [verdict, text]; returns (key, the whole verdict, text) -- the whole verdict, not its
    first word (b656's defect (e))."""
    if not re.match(r'^(N[1-5]|H[1-4]|S[1-3])$', k) or not isinstance(v, list) or len(v) != 2 or not isinstance(v[0], str) or not v[0].strip():
        raise ValueError('score row of another shape: %r' % (k,))
    return k, v[0], v[1]


def read_head(path, head):
    """a landed head looked up in a ledger through the one conversion; returns its line or raises."""
    ln = line_of(path, head)
    if ln is None:
        raise LookupError('head not found through conv: %s' % head[:60])
    return ln


RUNNER_KEYS = ('kernel', 'branch', 'ref', 'target', 'run_id', 'conclusion', 'artifact_sha256', 'mem_low', 'stopped', 'gate', 'merged', 'tag')


def read_runner_row(r):
    """a row of the runner rows bank (b658's, the kernel's last run) -- every key of RUNNER_KEYS present; returns the row's reading
    (kernel, outcome, merged); raises KeyError on a row of another shape."""
    missing = [k for k in RUNNER_KEYS if k not in r]
    if missing:
        raise KeyError('runner row without %s' % missing)
    if r['stopped']:
        outcome = 'STOPPED BENEATH THE HOLD ON THE RUNNER'
    elif r['conclusion'] != 'success':
        outcome = 'RUN %s' % (r['conclusion'] or 'NOT CONCLUDED')
    else:
        outcome = 'GATE %s' % (r['gate'] or 'UNREAD')
    return dict(kernel=r['kernel'], outcome=outcome, merged=r['merged'], low=r['mem_low'], above_hold=(r['mem_low'] is not None and r['mem_low'] >= 2560))


CELL_FORMS = ('j₀ = ', 'NONE ≤ J_max', 'HYP-UNVERIFIED(')


def read_map_cell(r):
    """a cell of the map bank (data/b661_detection_map.json, rows are cells): sigma and t strings, certs a non-empty list of [name, CERTIFIED or
    NOT CERTIFIED, why], a reading in one of the three forms of (R271)(4); returns (sigma, t, form, j₀ or None, the names certified, the names
    not certified); raises on a row of another shape."""
    if not isinstance(r, dict) or not isinstance(r.get('sigma'), str) or not isinstance(r.get('t'), str):
        raise ValueError('map cell of another shape')
    cs = r.get('certs')
    if not isinstance(cs, list) or not cs or not all(isinstance(c, list) and len(c) == 3 and c[1] in ('CERTIFIED', 'NOT CERTIFIED') for c in cs):
        raise ValueError('map cell without its certifications: (%s, %s)' % (r.get('sigma'), r.get('t')))
    rd_ = r.get('reading')
    form = [f for f in CELL_FORMS if isinstance(rd_, str) and rd_.startswith(f)]
    if len(form) != 1:
        raise ValueError('map cell reading of another form: %r' % (rd_,))
    j0 = r.get('j0') if form[0] == 'j₀ = ' else None
    if form[0] == 'j₀ = ' and not isinstance(j0, int):
        raise ValueError('map cell with an index and no j0')
    return (r['sigma'], r['t'], form[0].strip(' =(') if form[0] != 'j₀ = ' else 'j₀', j0, [c[0] for c in cs if c[1] == 'CERTIFIED'],
            [c[0] for c in cs if c[1] == 'NOT CERTIFIED'])


READERS = ('read_score_row', 'read_head', 'read_runner_row', 'read_map_cell')


# ================================================================================ COMPONENT 1: THE RECORD LINE, (R271)(1)
WH = ('*Appended 2026-10-13 by b661 to b660’s entry (:8461), under `(R271)`(1) -- b660 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b660_closing.txt):*')


def _weight():
    return ('\n' + WH + ' the ten acts b650–b659 read as one (relay data/b660_ten_acts.txt) -- 63 defects, the seat’s 48 in 11 kinds with 9 '
            'recurring, CONVERSION closed by rule and 8 recurring kinds OPEN, TEXT and ROUTE closed; the navigator’s 14 of one kind, both seats’ '
            'sentences banked side by side; the lanes (relay data/b660_lanes.txt) -- 4 kernels merged covering 205 of 266 OVERREACHES, 15 '
            'remaining with 61, SIDE-lv-conservation’s 13 UNRESOLVED rows and its cell refreshes owed, 14 work-orders and items at 3 DISCHARGED, '
            '2 ACTED, 9 PRICED; the author’s word -- Q1 and Q5 RETIRED, Q2 and Q3 STAYS, Q4 WORK-ORDER standing, W-ORD-CITATION-CHECK a gate '
            'step at b662, W-ORD-VERDICT-INSTRUMENT and W-ORD-PLAIN-COMMENT-ARM DISCHARGED, the research order Epstein, Keiper, χ-Li after b661, '
            'the Project loop CLOSED; relay 2e439312, PLACE-papers 2e07a61, FINDINGS :8459 and :8461, OPEN_TRAILS :14092, the root c147a36e… '
            'over 18 banks; the suite 72 of 77, the four act-shaped failures and the carried row declared; three defects the seat’s, (c) outside '
            'the root in the closing. No tool file changed. Nothing deposited.\n')


def c1(*a):
    items = [('FINDINGS.md', WH, _weight())]
    land(items, 'b661_record_lines.json', 'c1', entry=K.B660_ENTRY,
         check=[('FINDINGS.md', K.B660_ENTRY, '## The reading act: ten acts b650–b659'),
                ('OPEN_TRAILS.md', K.B660_TRAIL, '### b660 — lane three, act eighty-seven')],
         dry='dry' in a)


# ================================================================================ THE AUTHOR'S ANSWERS (b659's route, carried)
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID


def _session_rows():
    start = None
    for i, raw in enumerate(io.open(SESSION, encoding='utf-8', errors='replace'), 1):
        try:
            o = json.loads(raw)
        except ValueError:
            continue
        if start is None and K.ANCHOR in raw and o.get('type') == 'user' and not o.get('isCompactSummary'):
            start = i
        if start is not None:
            yield i, o, start


def answers(*a):
    """data/b661_author_answers.txt: every prompt put by the seat in this act, with its options and the answer; and every word of the author
    delivered between BEGIN and END after the ruling, and the author's plain messages, verbatim."""
    calls, results, words, plain_, start = [], {}, [], [], None
    for i, o, st in _session_rows():
        start = st
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
                    plain_.append((i, t.strip()))
        for t in texts:
            for mm in re.finditer(r'(?ms)^BEGIN\s*\n(.*?)\nEND\s*$', t or ''):
                if K.ANCHOR not in mm.group(1):
                    words.append((i, mm.group(1)))
        for c in cs if isinstance(cs, list) else []:
            if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') == 'AskUserQuestion':
                calls.append((i, c['id'], c['input'], o.get('timestamp')))
            if isinstance(c, dict) and c.get('type') == 'tool_result':
                t = c.get('content')
                results[c.get('tool_use_id')] = (i, ''.join(x.get('text', '') for x in t) if isinstance(t, list) else t, o.get('timestamp'))
    if start is None:
        sys.exit('### THE ANCHOR IS NOT A USER LINE OF THIS SESSION -- NOTHING WRITTEN')
    L, n = [], 0
    for i, cid, inp, ts in calls:
        L.append('### CALL tool-use id %s (session %s, transcript line %d, %s)' % (cid, K.SESSION_ID, i, ts))
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
        W += ['### THE AUTHOR`S WORD (transcript line %d), BEGIN to END, verbatim:' % i] + w.replace('\r', '').split(NL) + ['']
    for i, t in plain_:
        W += ['### THE AUTHOR`S MESSAGE (transcript line %d), verbatim: %s' % (i, t.replace('\r', '').replace(NL, ' ')), '']
    nw = len([x for x in W if x.startswith('### THE AUTHOR`S WORD')])
    head = ['### b661 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d).' % (
                n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start), '']
    put_txt('b661_author_answers.txt', [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    put_json('b661_author_answers.json', dict(at=utc(), calls=[dict(line=i, id=cid, ts=ts, result_ts=(results.get(cid) or (None, None, None))[2])
                                                               for i, cid, _inp, ts in calls]))
    print('  prompts banked: %d ; words banked: %d' % (n, nw))


# ================================================================================ THE LATE ROUTES (b659's, carried; every row read through READERS)
import collections                 # noqa: E402
import b633_record as R3           # noqa: E402
import edit_route as ER            # noqa: E402
RELAY = ROOT
SUBAGENTS = 'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % K.SESSION_ID
R3.SP, R3.SESSION, R3.SESSION_ID = SP, SESSION, K.SESSION_ID


def _show(repo, rev, path):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


def capture():
    rows = ER.capture(SESSION, K.ANCHOR, SUBAGENTS)
    for i, r in enumerate(rows):
        r['n'] = i + 1
    return rows


LOCAL_LEAN = re.compile(r'(^|[;&|(]\s*|\s)(lake|lean)(\.exe)?\s+(build|env|exe|update|\S+\.lean)')
QUOTED = re.compile(r'"(?:[^"\\]|\\.)*"|\'[^\']*\'')


def local_lean(cmd):
    """a command runs lean or lake on this host: the pattern read outside quoted strings and outside a gh workflow call (the hosted runner's)."""
    return 'gh workflow' not in cmd and LOCAL_LEAN.search(QUOTED.sub('""', cmd)) is not None


def commands(*a):
    rows = capture()
    if not rows:
        sys.exit('### THE COMMAND CAPTURE READ NO COMMAND -- NOTHING WRITTEN')
    hits = ER.scan(rows)
    lean = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and local_lean(r['cmd'])]
    L = ['b661 -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING AND THE LOCAL LEAN READING (N1) (%s)' % utc(), '',
         '### the source: the seat`s session %s from its first user line carrying %r, and its subagents` transcripts' % (K.SESSION_ID, K.ANCHOR),
         '### commands read: %d' % len(rows), '', '### THE OFFENDING COMMANDS, EACH PRINTED WHOLE (%d):' % len(hits)]
    for r, o in hits:
        L += ['  #%d %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not hits:
        L.append('  NONE')
    L += ['', '### THE COMMANDS THAT RUN lean OR lake ON THIS HOST (%d):' % len(lean)] + (['  #%d %s' % (r['n'], r['cmd'][:200]) for r in lean] or ['  NONE'])
    L += ['', '### EVERY COMMAND (n | time | source | tool | first line, 160 characters):']
    L += ['  #%d | %s | %s | %s | %s' % (r['n'], r['ts'], r['src'], r['tool'], r['cmd'].split(NL)[0][:160]) for r in rows]
    L += ['', '### ### **COMMANDS %d ; G-EDIT-ROUTE OFFENCES %d ; LOCAL lean OR lake COMMANDS %d.**' % (len(rows), len(hits), len(lean))]
    put_txt('b661_commands.txt', [l.replace('\r', '') for l in L])
    put_json('b661_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                        local_lean=[r['n'] for r in lean]))
    print(L[-1])


# ================================================================================ COMPONENT 4-5: THE FACE`S BANKS, THE ROOT, THE SCORES, THE RECORD
def kernels(*a):
    import b641_record as R41
    put_json('b661_kernels_face.json', dict(at=utc(), kernels=R3.kern_state(list(R41.KERNS_READ))))
    print('  kernels read: %d' % len(R41.KERNS_READ))


def _defect_short():
    return [re.match(r'^\(([a-z])\) ([^.]*)\.', l.strip()).group(0)[:-1] for l in rdn('b661_defects.txt').split(NL)
            if re.match(r'^    \([a-z]\) [^.]*\.', l)]


def defects(*a):
    t = rdn('b661_defects.txt')
    ds = [l.strip() for l in t.split(NL) if re.match(r'^    \([a-z]\) ', l)]
    put_json('b661_defects.json', dict(at=utc(), defects=ds, short=_defect_short()))
    print('  defects %d' % len(ds))


def seal_hashes():
    import hashlib
    rec_ = jl('b661_seal_hashes.json').get('tools') or {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


ROOT_EXCLUDE = re.compile(r'^b661_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|closing.*|mirror.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|commands)\.(txt|json|md)$')


def root_banks():
    return sorted('data/' + f for f in os.listdir(D) if f.startswith('b661_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f))


def root(*a):
    banks = root_banks()
    crlf = [b for b in banks if b'\r\n' in open(os.path.join(ROOT, *b.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/b661_seal_hashes.json' in banks, crlf or 'none'))
    if crlf:
        sys.exit('### A BANK THE ROOT WOULD NAME IS CR LF -- NOTHING WRITTEN')
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b661'] + banks + ([] if 'dry' in a else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import tempfile
    import act_root as AR
    J = jl('b661_act_root.json')
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/')][0]
    with tempfile.TemporaryDirectory(prefix='b661_ra_') as tmp:
        cp = os.path.join(tmp, os.path.basename(bank_))
        b = bytearray(open(os.path.join(ROOT, *bank_.split('/')), 'rb').read())
        b[0] ^= 0x01
        open(cp, 'wb').write(bytes(b))
        items2 = [('%s %s' % (bank_, AR.sha256_file(cp)) if it.split()[0] == bank_ else it) for it in J['items']]
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
    L = ['b661 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '?')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b661_root_arm.txt', L)
    put_json('b661_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
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
    L = ['b661 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (utc(), r.returncode, g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b661_table_final.txt', L)
    put_json('b661_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


NK = ('N1', 'N2', 'N3', 'N4', 'N5')
HK = ('H1', 'H2', 'H3', 'H4')
SK = ('S1', 'S2', 'S3')
SCORE_KEYS = NK + HK + SK
N5_RELAY_DATA = ('act_roots.txt', 'b660_closing_push_out.txt')
N5_PP = ('FINDINGS.md', 'OPEN_TRAILS.md')
WIDTHS = ('33' + '.19', '38' + '.96')
WIDTH_EXEMPT = ('b661_ferry.txt', 'b661_author_answers.txt')   # ### the ruling's and the author's own words, verbatim
FACE = os.path.join(D, 'b661_registration_2026-10-13.txt')
BINDERS = (':135 H : PWSetup', ':136 Q :', ':136 B :', ':136 D :', ':137-:138 hQtie', ':139 hQb', ':140 θ', ':141-:142 hθ', ':143 A₀',
           ':144 j', ':145-:147 hrate', ':148 THE CONCLUSION')
CERT_NAMES = ('H.hev', 'H.hsm', 'H.hs', 'H.hL', 'H.hM', 'H.hdom', 'tieSet', 'killSet', 'hA', 'hQtie', 'hQb', 'hθ0', 'hθ')


def TRAIL_HEAD():
    return ('### b661 — lane two, act eighty-eight, the research act under (R271): b660 at its weight; the binding re-read at v0.28; the '
            'detection-index map at Z₁ with every hypothesis certified per cell')


def _iso(s):
    import calendar
    try:
        return calendar.timegm(time.strptime((s or '')[:19], '%Y-%m-%dT%H:%M:%S'))
    except Exception:
        return None


def _ct(repo, *a):
    s = g(repo, 'log', '-1', '--format=%ct', *a).strip()
    return int(s) if s.isdigit() else None


def _cells():
    """the map's cells, each through read_map_cell; returns [(sigma, t, form, j0, certified, not certified)]."""
    return [read_map_cell(r) for r in jl('b661_detection_map.json').get('cells') or []]


def _map_text():
    return rdn('b661_detection_map.txt')


def _map_header_epoch():
    m = re.search(r'UNDER \(R271\)\(4\)-\(5\) \((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\)', _map_text())
    return _iso(m.group(1)) if m else None


NUMBER_RUN = re.compile(r'b661_proto|b661_map(\.py|_run\.sh)')


def _first_number_epoch():
    """the first command of the act's capture that ran a computation of the map's numbers -- a scratch prototype or the map itself (the
    script or its detached driver): the act's first number."""
    ts = [_iso(r['ts']) for r in capture() if r['tool'] in ('Bash', 'PowerShell') and NUMBER_RUN.search(r['cmd'])
          and not r['cmd'].lstrip().startswith(('cat ', 'head ', 'grep '))]
    ts = [t for t in ts if t]
    return min(ts) if ts else _map_header_epoch()


def _counts():
    cs = _cells()
    return len(cs), sum(1 for c in cs if c[2] == 'j₀'), sum(1 for c in cs if c[2] == 'NONE ≤ J_max'), sum(1 for c in cs if c[2] == 'HYP-UNVERIFIED')


def _hline(k):
    m = re.search(r'^  %s (.*)$' % k, _map_text(), re.M)
    return m.group(1) if m else ''


def _cert_blocks():
    """per cell block of the map bank: the line numbers of each certification name, of the first hrate line and of the reading; returns
    [(cell, ok, why)] -- ok when every certification name prints before the first hrate line and the reading, and no index prints in a
    block with a NOT CERTIFIED line."""
    out = []
    t = _map_text().split(NL)
    starts = [i for i, l in enumerate(t) if l.startswith('== CELL ')]
    for n, s in enumerate(starts):
        e = starts[n + 1] if n + 1 < len(starts) else len(t)
        blk = t[s:e]
        cell = blk[0]
        hr = [i for i, l in enumerate(blk) if l.startswith('    hrate j = ')]
        rdg = [i for i, l in enumerate(blk) if l.startswith('  READING ')]
        nc = [l for l in blk if ' NOT CERTIFIED -- ' in l]
        pos = dict((nm, min([i for i, l in enumerate(blk) if re.match(r'^  %s\s+(CERTIFIED|NOT CERTIFIED) -- ' % re.escape(nm), l)] or [10 ** 6]))
                   for nm in CERT_NAMES)
        first = min(hr + rdg) if (hr + rdg) else 10 ** 6
        if nc:
            ok = not any('j₀ = ' in blk[i] for i in rdg)
            why = 'a NOT CERTIFIED line and no index'
        else:
            ok = all(pos[nm] < first for nm in CERT_NAMES)
            why = 'all %d names before the first hrate line' % len(CERT_NAMES)
        out.append((cell, ok, why))
    return out


def _n2():
    b = rdn('b661_e1cfg_binding.txt')
    files = g(RELAY, 'show', '--name-only', '--pretty=format:', K.BINDING_COMMIT).split()
    aj = jl('b661_author_answers.json').get('calls') or []
    ask = _iso(aj[0]['ts']) if aj and aj[0].get('ts') else None
    last_ans = max((_iso(c.get('result_ts')) or 0) for c in aj) if aj else None
    ct = _ct(RELAY, K.BINDING_COMMIT)
    first_num = _first_number_epoch()
    binders = [x for x in BINDERS if x not in b]
    ok = files == ['data/b661_e1cfg_binding.txt'] and ask and ct and ct < ask and not binders and 'No quantity is unbindable' in b \
        and last_ans and first_num and last_ans < first_num
    return ('HELD' if ok else 'REFUTED'), (
        'every binder of zeroSide_neg_at_rate_cfg bound by file and line (relay data/b661_e1cfg_binding.txt, binders missing %s, none '
        'unbindable), committed alone at %s (%s) before the one prompt (%s); the author`s last word %s before the map`s first number (%s)' % (
            binders or 'NONE', K.BINDING_COMMIT, time.strftime('%H:%M:%SZ', time.gmtime(ct)) if ct else '?',
            time.strftime('%H:%M:%SZ', time.gmtime(ask)) if ask else '?', time.strftime('%H:%M:%SZ', time.gmtime(last_ans)) if last_ans else '?',
            time.strftime('%H:%M:%SZ', time.gmtime(first_num)) if first_num else '?'))


def _n3():
    cb = _cert_blocks()
    bad = [c for c, ok, _w in cb if not ok]
    ok = len(cb) == K.MAP_CELLS and not bad
    return ('HELD' if ok else 'REFUTED'), (
        'cells read %d of %d; in each, every one of the %d certifications printed by name before its first hrate line and its reading, and no '
        'index beside an uncertified hypothesis: %s' % (len(cb), K.MAP_CELLS, len(CERT_NAMES), 'ALL' if not bad else 'NOT %s' % bad))


def _n4():
    c, ni, nn, nu = _counts()
    h3 = _hline('H3')
    if ni == 0:
        return ('HELD, VACUOUS', 'VACUOUS: no cell of the map printed an index (%d cells: %d NONE ≤ J_max, %d HYP-UNVERIFIED), so no cell is one '
                'where H3 must hold; the map`s H3 line: %s; the control beside the map (relay data/b661_map_control.txt, not a reading) read '
                'H3`s cell past J_max: %s' % (c, nn, nu, h3, _control_line()))
    held = h3.startswith('HELD')
    return ('HELD' if held else 'REFUTED'), 'the map`s H3 line: %s' % h3


def _control_line():
    m = re.search(r'^  CONTROL \((.*)$', rdn('b661_map_control.txt'), re.M)
    return '(' + m.group(1) if m else '### UNREAD'


def _widths():
    hits = []
    for f in sorted(os.listdir(D)):
        if f.startswith(('b661_', 'audit_b661_')) and f not in WIDTH_EXEMPT and os.path.isfile(os.path.join(D, f)):
            if any(w in rd(os.path.join(D, f)) for w in WIDTHS):
                hits.append(f)
    return hits


def _n5():
    face = jl('b661_kernels_face.json').get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    kern_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in N5_PP]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b661_|audit_b661_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('data/') and x[5:] in N5_RELAY_DATA))]
    km = g(K.KD, 'rev-parse', '--short=7', 'main').strip()
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    import b661_checks as CH
    new_arms = sorted(set(a[0] for a in CH.ARMS) - set(CH.STANDING) - set(K.ACT_ARMS))
    wh = _widths()
    ok = kern_ok and not pp_beyond and not kinds_beyond and not differ and km == K.K_MAIN and not new_arms and not wh
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unsubmitted); no kernel main written (SIDE-explicit-formula main %s, '
            'v0.28, as the act began); every kernel as the face read it %s; standing arms added: %s (the act`s arms over its own banks %d); sealed '
            'tools not agreeing %s; PLACE-papers beyond FINDINGS and OPEN_TRAILS: %s; relay files of a kind beyond the banks, the tools (the map '
            'script among them) and the root list: %s; the plateau family`s widths (the bench`s, as the author read N5) in the act`s banks %s, '
            'the ferry and the answers bank exempt as the ruling`s and the author`s own words; no identifier of the author in any outbound '
            'request (git pushes and remote reads alone)' % (
                K.DRAFT, km, kern_ok, new_arms or 'NONE', len(K.ACT_ARMS), differ or 'NONE', pp_beyond or 'NONE', kinds_beyond or 'NONE',
                wh or 'NONE'))


def _h(k):
    line = _hline(k)
    w = line.split(' -- ')[0].strip()
    if w.startswith('VACUOUS'):
        w = 'HELD, VACUOUS'
    return (w or '### UNREAD'), ('the map`s line (relay data/b661_detection_map.txt): %s %s' % (k, line))


def scores(*a):
    TF, RA = jl('b661_table_final.json'), jl('b661_root_arm.json')
    _r, _n, sh = seal_hashes()
    cm = jl('b661_commands.json')
    S = {
        'N1': (('HELD' if cm and not cm.get('local_lean') else 'REFUTED'),
               'commands of this act that run lean or lake on this host: %s (relay data/b661_commands.txt); no kernel file written (N5)' % (
                   cm.get('local_lean') if cm else '### UNREAD')),
        'N2': _n2(), 'N3': _n3(), 'N4': _n4(), 'N5': _n5(),
        'H1': _h('H1'), 'H2': _h('H2'), 'H3': _h('H3'), 'H4': _h('H4'),
        'S1': (('HELD' if not TF.get('gone') and not TF.get('grade_moved') else 'REFUTED') if TF else 'PENDING',
               'the table at the end against relay HEAD`s: moved %s, gone %s, added %s, grade moved %s' % (
                   len(TF.get('moved') or []), len(TF.get('gone') or []), len(TF.get('added') or []), len(TF.get('grade_moved') or []))),
        'S2': (('HELD' if RA.get('root_recomputed') == RA.get('root') and RA.get('root_copy') != RA.get('root') and not RA.get('late') else 'REFUTED')
               if RA else 'PENDING', 'the root recomputed equal, the one-byte control moving it, the root order holding locally'),
        'S3': ('HELD' if sh and all(v == 'agree' for _t, v in sh) else 'REFUTED', 'the sealed tools` hashes %s' % dict(collections.Counter(v for _t, v in sh))),
    }
    for k2 in SCORE_KEYS:
        read_score_row(k2, list(S[k2]))
    put_json('b661_scores.json', dict((k2, list(v)) for k2, v in S.items()))
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:500]))


NEXT_LINE = ('b662, per `(R271)`(8), the re-cut act on SIDE-carrier-spec (9) under `(R265)`’s form, W-ORD-CITATION-CHECK a gate step at its '
             'step zero; b663 the research act W-ORD-EPSTEIN-ZQ')


def _sv(S, k):
    return read_score_row(k, S.get(k) or ['?', ''])[1] if S.get(k) else '?'


def _word(k):
    S = jl('b661_scores.json')
    v = _sv(S, k)
    if v.startswith('HELD'):
        return 'held vacuously' if 'VACUOUS' in v else 'held'
    return 'refuted' if v.startswith('REFUTED') else v.lower()


def _nt():
    m = re.search(r'N\((\d+)\) = (\d+) by arb\.zeta_nzeros', _map_text())
    return (m.group(1), m.group(2)) if m else ('?', '?')


def _by_t(key):
    """the map's per-t values of a cell field, one per t in the grid's order when every σ agrees, else the list per t."""
    cs = jl('b661_detection_map.json').get('cells') or []
    out = []
    for tt in ('14.1', '29.6', '50.0', '100.0'):
        vs = sorted(set(r.get(key) for r in cs if r.get('t') == tt))
        out.append(str(vs[0]) if len(vs) == 1 else str(vs))
    return ', '.join(out)


def _theta_off_one():
    """the largest 1 - θ over the cells, from the map json's θ balls (their midpoints), as a check of the entry's sentence."""
    vals = []
    for r in jl('b661_detection_map.json').get('cells') or []:
        m = re.match(r'\[?([0-9.]+)', r.get('theta') or '')
        if m:
            vals.append(1 - float(m.group(1)))
    return max(vals) if vals else None


def _rungs():
    return sum(1 for r in jl('b661_detection_map.json').get('cells') or [] if r.get('first'))


def _title():
    c, ni, nn, nu = _counts()
    return ('## The detection-index map at Z₁ over %d cells: %d with an index, %d NONE ≤ J_max, %d HYP-UNVERIFIED; H1 %s, H2 %s, H3 %s, '
            'H4 %s; the binding at v0.28' % (c, ni, nn, nu, _word('H1'), _word('H2'), _word('H3'), _word('H4')))


def _finding_text():
    S, rl, J = jl('b661_scores.json'), jl('b661_record_lines.json'), jl('b661_act_root.json')
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b661_author_answers.txt'), re.M))
    ls = (rl.get('lines') or []) + [{}]
    c, ni, nn, nu = _counts()
    off = _theta_off_one()
    if off is None or off >= 1e-3:
        sys.exit('### THE ENTRY`S θ SENTENCE IS NOT THE BANK`S (largest 1 - θ %s) -- NOTHING COMPOSED' % off)
    e = ['', _title(), '',
         '*Filed at b661 on the author’s ruling `(R271)` and the author’s word (%d questions in two calls). Banks: relay `data/b661_e1cfg_binding.txt`, '
         '`data/b661_detection_map.txt`, `data/b661_map_control.txt`, `data/b661_author_answers.txt`, `data/b661_act_root.txt`.*' % n_ans, '',
         '**The binding** (`(R271)`(3)): b656’s binding re-read against SIDE-explicit-formula v0.28 quantity by quantity, each re-bound to a '
         'binder of zeroSide_neg_at_rate_cfg (Schema/RateIndexCfg.lean :135-:148) by file and line, hA and A₀ binders now; O-2 discharged by '
         'b658, O-1 and O-3 standing at zetaZeroConfig. hQtie and hQb quantify over every index, so they are certified by coeffs_exist’s argument '
         '(PowerLimit.lean :686-:731) with their inputs in balls and a control at each index read; B and D read from its witness (:683). No '
         'quantity unbound; raised as one prompt before any number. N2 %s.' % _sv(S, 'N2'), '',
         '**The map** (`(R271)`(4)-(5)): Z₁(σ, t), the orbit of four and ζ’s %s zeros of height at most %s from Arb’s zero list, over '
         'σ ∈ {0.55, 0.6, 0.7, 0.8, 0.9} and t ∈ {14.1, 29.6, 50.0, 100.0}, Arb balls at 200 bits with one rung to 400 on the author’s word, '
         'J_max = D + 8 per cell. Every hypothesis other than hrate certified by name before any index in every cell; %d cells: %d with an index, '
         '%d NONE ≤ J_max, %d HYP-UNVERIFIED, cells re-read at the rung %d. The kill set grows with t (%s ordinates), D with it (%s), and θ '
         'stays within 10⁻³ of 1 -- the next genuine ordinate above t nearly ties the hypothetical zero’s score -- so hrate’s left side stays '
         'above its right at every index up to J_max. N3 %s; H1 %s, H2 %s, H3 %s, H4 %s.' % (
             _nt()[1], '{:,}'.format(int(_nt()[0])) if _nt()[0].isdigit() else '?', c, ni, nn, nu, _rungs(), _by_t('card_Xr'), _by_t('D'),
             _sv(S, 'N3'), _sv(S, 'H1'), _sv(S, 'H2'), _sv(S, 'H3'), _sv(S, 'H4')), '',
         '**The control** (not a reading): at H3’s cell (0.8, 29.6), the same certifications and hrate read past J_max, it first holds at '
         'j = 31, and the zero side there, computed term by term, lies below 0 at minus the tie terms’ sum: the computation binds to the kernel’s '
         'objects where an index exists. H3 stays NOT SCORABLE at the map’s J_max. N4 %s.' % _sv(S, 'N4'), '',
         '**The record line** (`(R271)`(1)): b660 at its weight (FINDINGS :%s).' % ls[0].get('line'), '',
         '**The root.** b661 over %d repositories, %d tags and %d banks, the last step of the act’s banks; its chain read at commit inside the suite.' % (
             len((J.get('reads') or {}).get('heads') or []), len((J.get('reads') or {}).get('tags') or []), len((J.get('reads') or {}).get('banks') or [])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): this map re-reads b656’s binding (relay `data/b656_e1_binding.txt`) and b658’s '
         'statement (relay `data/b658_e1cfg_statement.txt`), and finds the rate inequality unmet at every index up to J_max = D + 8 on the whole '
         'grid, at coeffs_exist’s B and D and the least θ the finite configuration admits -- the inequality is sufficient for the theorem’s '
         'conclusion, not necessary, so no cell says the zero side is not negative there; it is read by W-ORD-CLOSE-PAIR-BENCH when its turn '
         'comes and by the next reading act. It strengthens the programme’s offering of statements a reader can check: at each grid cell the '
         'rate inequality’s two sides are printed at every index read, the theorem’s other hypotheses certified by name in balls.', '',
         '**Next.** %s.' % NEXT_LINE, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero; the map states what a compiled theorem says of a finite '
         'configuration Z₁, which is not ζ’s, and nothing of ζ.*', '']
    return _title(), NL.join(e)


FOR_AUTHOR = ('(1) hQtie and hQb certified by coeffs_exist’s argument at the unique interpolant, the per-index controls checks on the binding; '
              '(2) Aw enclosed through ∫|s′′′′| on the ramp, its sign pieces exact and its unresolved pieces bounded; (3) the control at H3’s cell '
              'past J_max banked beside the map as not a reading; (4) A₀ an upper value, an ordinate whose ball meets a step’s edge counted on both '
              'sides; (5) the map run twice, the second by the final script, the two banks equal but for the clock')


def _trail_text():
    S, fj, rl, J = (jl(n_) for n_ in ('b661_scores.json', 'b661_findings.json', 'b661_record_lines.json', 'b661_act_root.json'))
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b661_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    ls = (rl.get('lines') or []) + [{}]
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R271) ratified.** (1) b660 at its weight. (2) The object: Z₁(σ, t) and zeroSide_neg_at_rate_cfg. (3) The binding re-read, one '
             'prompt before any number. (4) The certification per cell. (5) H1–H4, fixed before any number. (6) No kernel edit. (7) The draft held '
             'at v5. (8) The act after: b662; b663 W-ORD-EPSTEIN-ZQ.', '',
             '**Entered:** FINDINGS.md:%s (b660’s weight), :%s (the entry); this record.' % (ls[0].get('line'), fj.get('entry_line')), '',
             '**Act root:** b661 `%s` (previous `%s`, b660’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF.' % (
                 J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d questions in two calls (relay data/b661_author_answers.txt): the one prompt of `(R271)`(3), four '
             'questions, before any number, and one question on the precision rung the author’s word named and no bank carried; none after the '
             'root.' % n_ans, '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b661_defects.txt): %s.' % ('; '.join(_defect_short()) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.**', '',
             '**Next:** %s.' % NEXT_LINE, '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b661_scores.json')
    L = ['=' * 104, 'b661 -- THE DESK.', '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in SCORE_KEYS]
    L += [''] + rdn('b661_defects.txt').rstrip(NL).split(NL)
    put_txt('b661_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl, J = (jl(n_) for n_ in ('b661_scores.json', 'b661_findings.json', 'b661_trail.json', 'b661_record_lines.json', 'b661_act_root.json'))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    ls = (rl.get('lines') or []) + [{}]
    c, ni, nn, nu = _counts()
    L = ['b661 -- THE COMPONENTS, BANKED UNDER (R271).', '',
         '### COMPONENT 0 : step zero (data/b661_ferry.txt, data/b661_stepzero.txt, data/b661_tests_stepzero.txt) ; push-out relay %s' % K.STEPZERO,
         '### COMPONENT 1 : the read-first (data/b661_readfirst.txt) ; b660`s weight FINDINGS :%s' % ls[0].get('line'),
         '### COMPONENT 2 : the binding (data/b661_e1cfg_binding.txt, relay %s) ; the prompt and the rung (data/b661_author_answers.txt) ; N2 %s' % (
             K.BINDING_COMMIT, S['N2'][0]),
         '### COMPONENT 3 : the map (data/b661_detection_map.txt, relay %s) ; cells %d: %d j₀, %d NONE, %d HYP-UNVERIFIED ; the control '
         '(data/b661_map_control.txt) ; N3 %s ; N4 %s ; H1 %s ; H2 %s ; H3 %s ; H4 %s' % (K.MAP_COMMIT, c, ni, nn, nu, S['N3'][0], S['N4'][0],
                                                                                          S['H1'][0], S['H2'][0], S['H3'][0], S['H4'][0]),
         '### COMPONENT 4 : the dry-run step (data/b661_reg_gate.txt), the seal (data/b661_seal_hashes.json), the suite ; S3 %s' % S['S3'][0],
         '### COMPONENT 5 : the root %s ; FINDINGS :%s ; OPEN_TRAILS :%s ; N1 %s ; N5 %s' % ((J.get('root') or '')[:16], fj.get('entry_line'),
                                                                                        tj.get('line'), S['N1'][0], S['N5'][0])]
    put_txt('b661_components.txt', L)
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
    ln = _land_one(FIND, t, e, 'b661_findings.json', dict(title=t))
    j = jl('b661_findings.json')
    j['entry_line'] = ln
    put_json('b661_findings.json', j)
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
    ln = _land_one(OT, TRAIL_HEAD(), e, 'b661_trail.json', {})
    print('  OPEN_TRAILS record :%s' % ln)


def _face_needles(face_text, which):
    m = re.search(r'^### THE DRY-RUN NEEDLES -- %s: (.*)$' % which, face_text, re.M)
    return re.findall(r'"([^"]+)"', m.group(1)) if m else []


def drycheck(*a):
    """(R267)(2), STANDING FROM b657: the FINDINGS entry and the trail record composed as the record tool composes them -- under stand-ins
    for the banks not yet written (B661_STANDIN) -- converted by conv and run through the screens their landing runs, the needles the face
    names read in each; prints DRY-RUN STEP : CLEAN and exits 0 only when both screens are quiet and every needle is found. Writes no bank."""
    face = rd(a[0] if a else FACE)
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


if __name__ == '__main__':
    fn = globals().get(sys.argv[1] if len(sys.argv) > 1 else '')
    if not callable(fn) or sys.argv[1].startswith('_') or sys.argv[1].startswith('read_'):
        print('usage: b661_record.py <route> [dry]')
        sys.exit(2)
    fn(*sys.argv[2:])
