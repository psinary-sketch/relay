# -*- coding: utf-8 -*-
"""b667_record.py -- THE ACT'S RECORD TOOL, b667 under (R277).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b667's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows can run each reader over one row of each shape before the seal.
### Carried by the Write tool from b666_record.py (the helpers, the guarded landing, the score reader, the head reader, the answers); new
### here: the record line of (R277)(1). No kernel is edited and no runner dispatched this act, so b666's kernel routes are not carried. The
### later routes are added by the Edit tool before the seal, each run before the face names it.
### Routes: `python tools/b667_record.py <route> [dry]`; each route banks under data/ and prints what it wrote.
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
import b667_worklist as K          # noqa: E402

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
    none a number any bank carries; a stand-in run writes no bank."""
    sk = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
    return {
        'b667_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b667_findings.json': dict(entry_line=99999, title='stand-in'),
        'b667_trail.json': dict(line=99999),
        'b667_act_root.json': dict(root='0' * 64, previous='d2c4a9d3' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
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


def _ws(s):
    return ' '.join(s.split())


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b667's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b667_scanfile_%s.md' % tag)
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
    """a scores row: key N1..N5 or S1..S3, value [verdict, text]; returns (key, the whole verdict, text) -- the whole verdict, not its first
    word (b656's defect (e))."""
    if not re.match(r'^(N[1-5]|S[1-3])$', k) or not isinstance(v, list) or len(v) != 2 or not isinstance(v[0], str) or not v[0].strip():
        raise ValueError('score row of another shape: %r' % (k,))
    return k, v[0], v[1]


def read_head(path, head):
    """a landed head looked up in a ledger through the one conversion; returns its line or raises."""
    ln = line_of(path, head)
    if ln is None:
        raise LookupError('head not found through conv: %s' % head[:60])
    return ln


CERT_KEYS = ('kind', 'idx', 're', 'im', 'h', 'widened', 'count', 'ball')


def read_cert_row(r):
    """a row of data/b667_epstein_zeros_certified.json -- kind ON, OFF or PARTNER, an integer index, its centre and half-width as strings, a
    count that is an integer; returns (kind, idx, count, widened); raises on a row of another shape."""
    missing = [k for k in CERT_KEYS if k not in r]
    if missing or r['kind'] not in ('ON', 'OFF', 'PARTNER') or not isinstance(r['idx'], int) or not isinstance(r['count'], int) \
            or not isinstance(r['re'], str) or not isinstance(r['im'], str) or r['h'] not in ('1e-12', '1e-9'):
        raise ValueError('certified row of another shape: %r' % (sorted(r) if isinstance(r, dict) else r,))
    return r['kind'], r['idx'], r['count'], bool(r['widened'])


READERS = ['read_score_row', 'read_head', 'read_cert_row']


# ================================================================================ COMPONENT 1: THE RECORD LINE, (R277)(1)
WH = ('*Appended 2026-10-13 by b667 to b666’s entry (:8621), under `(R277)`(1) -- b666 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b666_closing.txt), THE SUITE CLEAN:*')


def _weight():
    return ('\n' + WH + ' SIDE-cosmo -- six blocks in FanoFormation.lean and SteaneExemplar.lean into 14 sentence rows, 11 graded and cut, '
            'the header’s axiom claim removed on b649’s row with nothing composed, the two neighbouring rows on b647’s ACTION span closed by a '
            'period with ", not banked" dropped on b557’s bank; G-AXIOM-CLAIM at 1 before the merge and 0 after; run 38471056772 with 53 '
            'prints, the two banked prints equal and the rest at the standard three or empty, the kernel’s relay print bank opened; the '
            'earlier run 38470740945 NOT DERIVES on a private declaration in the print list, banked beside; merged alone at ca04c8c, tag '
            'v0.3.1; the tie rule at OPEN_TRAILS :14238; relay d43a72f9, PLACE-papers c143bcb, FINDINGS :8619 and :8621, OPEN_TRAILS :14240, '
            'the root d2c4a9d3…, the suite 81 of 81 before and after the push with no declared failure; four defects, all the seat’s, (d) a '
            'sealed scorer reading an axiom-free print as outside the standard three, scored through a scratch driver in b663’s form; '
            'SIDE-cosmo’s main past v0.3 untagged at c5cba30, a census item; the mirror at mirror-refresh-2026-10-13-b666.zip. Nothing '
            'deposited.\n')


def c1(*a):
    items = [('FINDINGS.md', WH, _weight())]
    land(items, 'b667_record_lines.json', 'c1', entry=K.B666_ENTRY,
         check=[('FINDINGS.md', K.B666_ENTRY, '## SIDE-cosmo’s docstrings'), ('OPEN_TRAILS.md', K.B666_TRAIL, '### b666')],
         dry='dry' in a)


# ================================================================================ THE AUTHOR'S ANSWERS (b666's route, carried)
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
    """data/b667_author_answers.txt: every prompt put by the seat in this act, with its options and the answer; and every word of the author
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
    head = ['### b667 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d).' % (
                n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start), '']
    put_txt('b667_author_answers.txt', [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    put_json('b667_author_answers.json', dict(at=utc(), calls=[dict(line=i, id=cid, ts=ts, result_ts=(results.get(cid) or (None, None, None))[2])
                                                               for i, cid, _inp, ts in calls]))
    print('  prompts banked: %d ; words banked: %d' % (n, nw))


# ================================================================================ COMPONENT 5: THE LANDING, (R277)(6)
def _cert():
    j = cert_json()
    rows = [read_cert_row(r) for r in (j.get('rows') or [])]
    return j, rows


def _counts():
    return rdn('b667_epstein_counts.txt')


def _map():
    return rdn('b667_epstein_control_balls.txt')


def _hyp():
    """H1-H5 by printed line: each hypothesis with the bank line it reads, verbatim."""
    c, m = _counts(), _map()
    j, rows = _cert()

    def line(text, pat):
        for l in text.split(NL):
            if re.search(pat, l):
                return l.strip()
        return None
    off = [x for x in rows if x[0] == 'OFF']
    on = [x for x in rows if x[0] == 'ON']
    l1, l2, l3 = line(c, r'^\s*\(H1\) '), line(c, r'^\s*\(H2\) '), line(c, r'^\s*\(H3\) ')
    l5 = line(c, r'^\s*\(H5\) ')
    l4 = line(m, r'^\s*H4 ')
    lj = line(m, r'READING Q0 AT qE0: ')
    lc = line(m, r'THE CONTROL (REPRODUCED|NOT REPRODUCED) \(')
    h1 = bool(l1) and l1.endswith('-> HELD') and len(off) == 17 and all(x[2] == 1 for x in off)
    h2 = bool(l2) and l2.endswith('-> HELD') and len(on) == 146 and all(x[2] == 1 for x in on)
    h3 = bool(l3) and l3.endswith('-> HELD') and j.get('N_R') == 180 and j.get('N_B') == 0
    jm = re.search(r'j₀ = (\d+)', lj or '')
    h4 = bool(l4) and l4.startswith('H4 HELD') and bool(jm) and int(jm.group(1)) == 38 and bool(lc) and 'NOT REPRODUCED' not in lc
    h5 = bool(l5) and l5.endswith('-> HELD')
    return [('H1', h1, l1), ('H2', h2, l2), ('H3', h3, l3), ('H4', h4, '%s ; %s ; %s' % (lj, l4, lc)), ('H5', h5, l5)]


def hypotheses(*a):
    H = _hyp()
    L = ['b667 -- H1-H5 OF (R277)(5), SCORED BY PRINTED LINE (%s): rows are hypotheses -- the verdict and the bank line it reads, verbatim '
         '(relay data/b667_epstein_counts.txt, data/b667_epstein_zeros_certified.json, data/b667_epstein_control_balls.txt).' % utc(), '']
    for k, ok, l in H:
        L.append('  (%s) %s -- %s' % (k, 'HELD' if ok else 'REFUTED', l))
        if k == 'H3':
            L.append('       the list`s size in R by orbit and pair, 146 + 2 × 17 = 180: relay data/b667_epstein_plan.txt section 1 (:7, :19), N(R) '
                     'banked as printed')
    L += ['', '### ### **HELD %d OF 5.**' % sum(1 for _k, ok, _l in H if ok)]
    put_txt('b667_hypotheses.txt', L)
    put_json('b667_hypotheses.json', dict(at=utc(), rows=[dict(h=k, held=ok, line=l) for k, ok, l in H]))
    print(NL.join(L[2:]))


DH = ('*Appended 2026-10-14 by b667 beneath W-ORD-EPSTEIN-CERTIFY (:14158), under `(R277)`(6) -- W-ORD-EPSTEIN-CERTIFY DISCHARGED:*')
KH = ('*Appended 2026-10-14 by b667 beneath W-ORD-EPSTEIN-CERTIFY (:14158), under `(R277)`(6) -- THE KERNEL ITEM FOR P1 AND P2, PLACED:*')


def _discharge():
    j, rows = _cert()
    w = sum(1 for x in rows if x[3])
    return ('\n' + DH + ' Q0’s zeros below 150 isolated in Arb balls by the argument-principle count: the 17 off-line zeros and the 146 '
            'on-line ordinates each counted 1 in a square of half-width 10⁻¹² about its banked double (%s), the 17 reflection partners 1 − conj ρ '
            'likewise; the region [−0.5, 1.5] × [0.5, 150] counted %s, the list’s 146 + 2 × 17, and the band [−0.5, 1.5] × [−0.5, 0.5] %s, so '
            'P2’s data reads certified for every |t| ≤ 150 (σ ≥ 3/2 by the Dirichlet bound, σ ≤ −1/2 by the functional equation); the route '
            'Chowla-Selberg with each term bounded, under (R277)(3a)-(3d); the b663 control re-run on the balls at j₀ = 38, the zero side below '
            'zero. Relay data/b667_epstein_zeros_certified.txt, data/b667_epstein_counts.txt, data/b667_epstein_control_balls.txt; b326’s '
            'banks unedited.\n' % ('%d widened to 10⁻⁹' % w if w else 'none widened', j.get('N_R'), j.get('N_B')))


def _kernel_item():
    return ('\n' + KH + ' the next kernel item: SIDE-explicit-formula’s Schema/EpsteinQ0.lean carries the configuration’s points as decimal '
            'literals (q0OnLine, q0OffLine) under P1 (Q0Listed, banked) and P2 (Q0Complete below 150); the balls of relay '
            'data/b667_epstein_zeros_certified.txt replace the literals by certified intervals and the counts of data/b667_epstein_counts.txt '
            'carry P2’s data, so P1 and P2 can be restated on certified data -- a later act, the kernel untouched at b667.\n')


def landing(*a):
    """Component 5's OPEN_TRAILS lines, after the dated line beneath data/b663_epstein_control.txt (written by the Edit tool) is in place."""
    if 'ball-certified at b667' not in rdn('b663_epstein_control.txt'):
        sys.exit('### THE DATED LINE BENEATH data/b663_epstein_control.txt IS NOT IN PLACE -- NOTHING WRITTEN')
    if not all(ok for _k, ok, _l in _hyp()):
        sys.exit('### H1-H5 DO NOT ALL HOLD -- THE DISCHARGE IS NOT WRITTEN (the finding route instead)')
    items = [('OPEN_TRAILS.md', DH, _discharge()), ('OPEN_TRAILS.md', KH, _kernel_item())]
    land(items, 'b667_landing.json', 'landing', entry=K.ORDER, check=[('OPEN_TRAILS.md', K.ORDER, '### `W-ORD-EPSTEIN-CERTIFY`')],
         dry='dry' in a)


# ================================================================================ THE LATE ROUTES (b666's, carried; every row read through READERS)
import collections                 # noqa: E402
import b633_record as R3           # noqa: E402
import edit_route as ER            # noqa: E402
RELAY = ROOT
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
    """a command runs lean or lake on this host: the pattern read outside quoted strings and outside a gh workflow call (the hosted runner's)."""
    return 'gh workflow' not in cmd and LOCAL_LEAN.search(QUOTED.sub('""', cmd)) is not None


def commands(*a):
    rows = capture()
    if not rows:
        sys.exit('### THE COMMAND CAPTURE READ NO COMMAND -- NOTHING WRITTEN')
    hits = ER.scan(rows)
    lean = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and local_lean(r['cmd'])]
    L = ['b667 -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING AND THE LOCAL LEAN READING (N1) (%s)' % utc(), '',
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
    put_txt('b667_commands.txt', [l.replace('\r', '') for l in L])
    put_json('b667_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                        local_lean=[r['n'] for r in lean]))
    print(L[-1])


def kernels(*a):
    import b641_record as R41
    put_json('b667_kernels_face.json', dict(at=utc(), kernels=R3.kern_state(list(R41.KERNS_READ))))
    print('  kernels read: %d' % len(R41.KERNS_READ))


DEFECT_ROW = re.compile(r'^    \(([a-z])\) ')


def _defect_short():
    out = []
    for l in rdn('b667_defects.txt').split(NL):
        m = re.match(r'^    \(([a-z])\) ([^.]*)\.', l)
        if m:
            out.append(m.group(0).strip()[:-1])
    return out


def defects(*a):
    t = rdn('b667_defects.txt')
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    put_json('b667_defects.json', dict(at=utc(), defects=ds, short=_defect_short()))
    print('  defects %d' % len(ds))


def seal_hashes():
    import hashlib
    rec_ = jl('b667_seal_hashes.json').get('tools') or {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


ROOT_EXCLUDE = re.compile(r'^b667_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|commands)\.(txt|json|md)$')
ROOT_SHARED = ('data/b663_epstein_control.txt', 'data/b627_margin_inputs.txt')   # ### the two banks this act dated a line beneath (reading (v)'s form)


def root_banks():
    return sorted(['data/' + f for f in os.listdir(D) if f.startswith('b667_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f)]
                  + list(ROOT_SHARED))


def root(*a):
    banks = root_banks()
    crlf = [b for b in banks if b'\r\n' in open(os.path.join(ROOT, *b.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/b667_seal_hashes.json' in banks, crlf or 'none'))
    if crlf:
        sys.exit('### A BANK THE ROOT WOULD NAME IS CR LF -- NOTHING WRITTEN')
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b667'] + banks + ([] if 'dry' in a else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import tempfile
    import act_root as AR
    J = jl('b667_act_root.json')
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/')][0]
    with tempfile.TemporaryDirectory(prefix='b667_ra_') as tmp:
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
    L = ['b667 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '?')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b667_root_arm.txt', L)
    put_json('b667_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
    print(L[-1])


def _rows_state(rows):
    return dict(((r['repo'], r['name']), (r.get('grade'), r.get('profile'), r.get('provenance'))) for r in rows)


def table_final(*a):
    before = _rows_state(json.loads(_show(RELAY, 'HEAD', 'data/terminal_table.json'))['rows'])
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(ROOT, 'tools', 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace')
    after = _rows_state(json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))['rows'])
    moved = sorted(k for k in set(before) & set(after) if before[k] != after[k])
    added, gone = sorted(set(after) - set(before)), sorted(set(before) - set(after))
    L = ['b667 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (utc(), r.returncode, g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b667_table_final.txt', L)
    put_json('b667_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


FACE = os.path.join(D, 'b667_registration_2026-10-14.txt')


def gatebanks(*a):
    """the gate's steps between the face and the lock (b666's order), each tool's output banked by this route, never by a shell redirect."""
    import gate_hash as G

    def runb(args, out):
        r = subprocess.run([sys.executable, '-X', 'utf8'] + args, capture_output=True, cwd=ROOT)
        b = (r.stdout + r.stderr).replace(b'\r\n', b'\n')
        if out:
            p = os.path.join(D, out)
            open(p + '.tmp', 'wb').write(b)
            os.replace(p + '.tmp', p)
        return r.returncode, b.decode('utf-8', 'replace')
    face_rel = 'data/b667_registration_2026-10-14.txt'
    rc1, t1 = runb([os.path.join(T, 'banned_terms.py'), '--new', face_rel], 'b667_reg_termscan.txt')
    rc2, t2 = runb([os.path.join(T, 'b667_regspec.py')], 'b667_regspec_run.txt')
    rc3, t3 = runb([os.path.join(T, 'reg_satisfiable.py'), 'data/b667_satisfiable.json', '--emit', 'b667'], None)
    print('  banned_terms rc %d ; %s' % (rc1, ([l for l in t1.split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    print('  regspec rc %d ; %s' % (rc2, ([l for l in t2.split(NL) if 'PREDICTIONS FOUND' in l] or ['### NONE'])[0].strip()))
    print('  reg_satisfiable rc %d ; %s' % (rc3, ([l for l in rdn('audit_b667_reg_satisfiable.txt').split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    for tool, out in (('b307_handoff_census.py', 'b667_census_stepzero.txt'), ('b327_faces_census.py', 'b667_faces_census_stepzero.txt'),
                      ('b303_pins.py', 'b667_pins_stepzero.txt')):
        rc, t = runb([os.path.join(T, tool), 'b667'], out)
        print('  %s rc %d ; %s' % (out, rc, ([l.strip() for l in t.split(NL) if 'TOTAL MISSING' in l or 'HARD-FAILING' in l] or ['### NONE'])[0][:120]))
    fa = os.path.join(ROOT, *face_rel.split('/'))
    for r in ('data/b667_reg_gate.txt', 'data/b667_reg_termscan.txt', 'data/b667_regspec_run.txt', 'data/audit_b667_reg_satisfiable.txt'):
        ra = os.path.join(ROOT, *r.split('/'))
        print('  stamp %s %s %s' % (r, G.stamp(ra, fa)[:16], G.matches(ra, fa)[0]))


NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3')
SCORE_KEYS = NK + SK
N5_RELAY_DATA = ('act_roots.txt', 'b666_closing_push_out.txt', 'b663_epstein_control.txt', 'b627_margin_inputs.txt')
N5_PP = ('FINDINGS.md', 'OPEN_TRAILS.md')


def TRAIL_HEAD():
    return ('### b667 — lane two, act ninety-four, the research act under (R277): b666 at its weight; the evaluation route raised in a plan; Q0’s '
            'zeros below 150 isolated in balls, the list’s completeness counted, the b663 control re-run on the balls')


def _iso(s):
    import calendar
    try:
        return calendar.timegm(time.strptime((s or '')[:19], '%Y-%m-%dT%H:%M:%S'))
    except Exception:
        return None


def _calls():
    return jl('b667_author_answers.json').get('calls') or []


def _run_starts():
    """the certify runs' start times, from their banks (runs 1-3) and the counts bank's head (the run that counted)."""
    out = []
    for n in ('b667_certify_run1.txt', 'b667_certify_run2.txt', 'b667_certify_run3.txt'):
        m = re.search(r'started (\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)', rdn(n))
        out.append(_iso(m.group(1)) if m else None)
    m = re.search(r'THE COUNTS \((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\)', _counts())
    out.append(_iso(m.group(1)) if m else None)
    return out


def _n2():
    calls = _calls()
    ts = [_iso(c.get('result_ts')) for c in calls]
    starts = _run_starts()
    plan_ans = ts[0] if ts else None
    ok = bool(ts) and all(ts) and all(starts) and plan_ans < starts[0] and max(ts) < starts[-1]
    return ('HELD' if ok else 'REFUTED'), (
        'the plan raised and answered (%s) before the first certify run (%s); %d prompts in all, the last answered (%s) before the run that '
        'counted (%s); the two obstructions measured and ruled before any Q0 point -- (3a) the Bessel rung, (3b) the derivative bound for the '
        'enclosure, (3c) the right edge by the tail bound, (3d) T4 restated -- each term`s bound and source in the plan`s sections 2, 11, 14 '
        'and 16; the plan`s first claim that no term was unbounded unmeasured (relay data/b667_defects.txt (b))' % (
            time.strftime('%H:%M:%SZ', time.gmtime(plan_ans)) if plan_ans else '?', time.strftime('%H:%M:%SZ', time.gmtime(starts[0])) if starts[0] else '?',
            len(calls), time.strftime('%H:%M:%SZ', time.gmtime(max(ts))) if ts and all(ts) else '?',
            time.strftime('%H:%M:%SZ', time.gmtime(starts[-1])) if starts[-1] else '?'))


def _n3():
    c = _counts()
    i1, i2, i3 = c.find('C1 READS AS FIXED (1, 1, 1 and 3)'), c.find('-> C2 READS AS FIXED'), c.find('-> C3 READS AS FIXED')
    isq = c.find('== THE SQUARES:')
    ok = min(i1, i2, i3) >= 0 and isq > max(i1, i2, i3)
    return ('HELD' if ok else 'REFUTED'), (
        'relay data/b667_epstein_counts.txt: C1 (ζ`s three squares 1, 1, 1 and its region 3), C2 (the shifted point`s count ball not '
        'containing 1) and C3 (UNLISTED 1 against the list less one) print as fixed, each before the first Q0 square; found %s, %s, %s ; the '
        'squares at %s' % (i1 >= 0, i2 >= 0, i3 >= 0, isq))


def _n4():
    H = dict((k, (ok, l)) for k, ok, l in _hyp())
    ok = H['H1'][0] and H['H2'][0] and H['H4'][0]
    return ('HELD' if ok else 'REFUTED'), 'H1 %s ; H2 %s ; H4 %s (relay data/b667_hypotheses.txt)' % (
        'HELD' if H['H1'][0] else 'REFUTED', 'HELD' if H['H2'][0] else 'REFUTED', H['H4'][1])


def _n5():
    face = jl('b667_kernels_face.json').get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    kern_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in N5_PP]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b667_|audit_b667_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('data/') and x[5:] in N5_RELAY_DATA))]
    b326 = [p for p in K.B326_BANKS if g(RELAY, 'diff', '--name-only', K.PRE_RELAY, '--', p).strip() or g(RELAY, 'diff', '--name-only', '--', p).strip()]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    import b667_checks as CH
    new_arms = sorted(set(a[0] for a in CH.ARMS) - set(CH.STANDING) - set(K.ACT_ARMS))
    ok = kern_ok and not pp_beyond and not kinds_beyond and not differ and not new_arms and not b326
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unsubmitted); every kernel`s main, tags, branches and status as the '
            'face read them %s (no kernel main written); standing arms added: %s (the act`s arms over its own banks %d); sealed tools not '
            'agreeing %s; PLACE-papers beyond FINDINGS and OPEN_TRAILS: %s; relay files of a kind beyond the scripts, the banks, the record '
            'lines` dated lines (b663`s control bank, b627`s precision bank), the root list and b666`s push-out bank: %s; b326`s banks changed: '
            '%s; no identifier of the author in any outbound request (git pushes and remote reads alone)' % (
                K.DRAFT, kern_ok, new_arms or 'NONE', len(K.ACT_ARMS), differ or 'NONE', pp_beyond or 'NONE', kinds_beyond or 'NONE', b326 or 'NONE'))


def scores(*a):
    TF, RA = jl('b667_table_final.json'), jl('b667_root_arm.json')
    _r, _n, sh = seal_hashes()
    cm = jl('b667_commands.json')
    S = {
        'N1': (('HELD' if cm and not cm.get('local_lean') else 'REFUTED'),
               'commands of this act that run lean or lake on this host: %s (relay data/b667_commands.txt); no kernel file written (N5`s kernel '
               'reading)' % (cm.get('local_lean') if cm else '### UNREAD')),
        'N2': _n2(), 'N3': _n3(), 'N4': _n4(), 'N5': _n5(),
        'S1': (('HELD' if not TF.get('gone') and not TF.get('grade_moved') else 'REFUTED') if TF else 'PENDING',
               'the table at the end against relay HEAD`s: moved %s, gone %s, added %s, grade moved %s' % (
                   len(TF.get('moved') or []), len(TF.get('gone') or []), len(TF.get('added') or []), len(TF.get('grade_moved') or []))),
        'S2': (('HELD' if RA.get('root_recomputed') == RA.get('root') and RA.get('root_copy') != RA.get('root') and not RA.get('late') else 'REFUTED')
               if RA else 'PENDING', 'the root recomputed equal, the one-byte control moving it, the root order holding locally'),
        'S3': ('HELD' if sh and all(v == 'agree' for _t, v in sh) else 'REFUTED', 'the sealed tools` hashes %s' % dict(collections.Counter(v for _t, v in sh))),
    }
    for k2 in SCORE_KEYS:
        read_score_row(k2, list(S[k2]))
    put_json('b667_scores.json', dict((k2, list(v)) for k2, v in S.items()))
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:500]))


NEXT_LINE = 'b668, per `(R277)`(8), the re-cut act on SIDE-grh-transfer under `(R265)`’s form; b669 the χ-Li converse; b670 the reading act'


def _sv(S, k):
    return read_score_row(k, S.get(k) or ['?', ''])[1] if S.get(k) else '?'


def _title():
    j, rows = _cert()
    off = sum(1 for x in rows if x[0] == 'OFF' and x[2] == 1)
    on = sum(1 for x in rows if x[0] == 'ON' and x[2] == 1)
    H = _hyp()
    lj = re.search(r'j₀ = (\d+)', H[3][2] or '')
    held = all(ok for _k, ok, _l in H)
    rel = 'equal to' if j.get('N_R') == 180 and j.get('N_B') == 0 else 'exceeding'
    return ('## Q0’s zeros below 150 in balls: %d off-line and %d on-line isolated, the region count %s the list; the b663 control on the '
            'balls at j₀ = %s; H1–H5 %s' % (off, on, rel, lj.group(1) if lj else '?', 'held' if held else 'not all held'))


def _finding_text():
    S, rl, J, ld = jl('b667_scores.json'), jl('b667_record_lines.json'), jl('b667_act_root.json'), jl('b667_landing.json')
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b667_author_answers.txt'), re.M))
    ls = (rl.get('lines') or []) + [{}]
    ll = (ld.get('lines') or []) + [{}, {}]
    j, rows = _cert()
    cc = re.search(r'CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    w = sum(1 for x in rows if x[3])
    rungs = re.search(r'FACTORS AT 600 BITS: (\d+)', rdn('b667_bessel_rungs.txt'))
    e = ['', _title(), '',
         '*Filed at b667 on the author’s ruling `(R277)` and the author’s word on its plan and its four amendments, (3a) to (3d) (%d questions '
         'in %d calls). Banks: relay `data/b667_citation_check.txt`, `data/b667_epstein_plan.txt`, `data/b667_bessel_obstruction.txt`, '
         '`data/b667_epstein_counts.txt`, `data/b667_epstein_zeros_certified.txt`, `data/b667_epstein_control_balls.txt`, '
         '`data/b667_hypotheses.txt`, `data/b667_act_root.txt`.*' % (n_ans, len(_calls())), '',
         '**The citation check** (the gate step from b662): %s cites checked at HEAD, %s OK, %s missed.' % (
             cc.group(1) if cc else '?', cc.group(2) if cc else '?', cc.group(3) if cc else '?'), '',
         '**The record line** (`(R277)`(1)): b666 at its weight (FINDINGS :%s).' % ls[0].get('line'), '',
         '**The route** (`(R277)`(3), raised before any number): Z_Q by the Chowla-Selberg form -- 2ζ(2s), the Γ-ratio term with ζ(2s − 1), and '
         'the Bessel sum -- every term an Arb ball or bounded with its source (DLMF 10.32.9 for the truncation and for a derivative bound); two '
         'obstructions found by measurement before any Q0 point was counted and ruled by the author: the Bessel factor needs 600 bits above '
         'height 120 ((3a)), and Arb’s ball through the Bessel order is useless, replaced by a shifted-contour derivative bound ((3b)); R’s right '
         'edge by the tail bound Z_Q(3/2) − 2 < 2 ((3c)); the truncation bound restated for |σ − ½| ≤ 2 ((3d)). Each checked against 800-bit '
         'evaluations. N2 %s.' % _sv(S, 'N2'), '',
         '**The controls** (`(R277)`(4)): the same engine pointed at ζ counted 1, 1, 1 about Arb’s three lowest zeros and 3 in its region; a Q0 '
         'zero shifted by 10⁻¹⁰ counted 0; the list less one point read UNLISTED 1 -- each before the first Q0 square. N3 %s.' % _sv(S, 'N3'), '',
         '**The balls** (`(R277)`(5)): the 17 off-line zeros and the 146 on-line ordinates each counted 1 in a square of half-width 10⁻¹² about '
         'its banked double (%s), the reflection partners likewise; the region [−0.5, 1.5] × [0.5, 150] counted %s, the list’s 146 + 2 × 17, and '
         'the band below it %s, so P2’s data is certified below 150; %s Bessel factors taken at 600 bits. The b663 control on the balls: j₀ = 38, '
         'the zero side below zero. N4 %s.' % ('none widened' if not w else '%d widened to 10⁻⁹' % w, j.get('N_R'), j.get('N_B'),
                                             rungs.group(1) if rungs else '?', _sv(S, 'N4')), '',
         '**The landing** (`(R277)`(6)): the dated line beneath relay `data/b663_epstein_control.txt` (“ball-certified at b667”); '
         'W-ORD-EPSTEIN-CERTIFY DISCHARGED (OPEN_TRAILS :%s); the kernel item for P1 and P2 placed (OPEN_TRAILS :%s); b326’s banks unedited.' % (
             ll[0].get('line'), ll[1].get('line')), '',
         '**The root.** b667 over %d repositories, %d tags and %d banks, the last step of the act’s banks; its chain read at commit inside the suite.' % (
             len((J.get('reads') or {}).get('heads') or []), len((J.get('reads') or {}).get('tags') or []), len((J.get('reads') or {}).get('banks') or [])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): this act re-reads b326’s two banks, b663’s configuration and its negative control, and '
         'b627’s precision bank; it is re-read by the kernel item that restates P1 and P2 on certified data and by b663’s control, whose second '
         'caveat it removes. It strengthens the programme’s offering of statements a reader can check: the Q0 configuration the negative control '
         'stands on is now a list of balls with a counted completeness, not a list of decimals from two agreeing routes.', '',
         '**Next.** %s.' % NEXT_LINE, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero of ζ; the balls are Q0’s, an Epstein zeta function with zeros off '
         'the line, counted below height 150.*', '']
    return _title(), NL.join(e)


FOR_AUTHOR = ('(1) R’s half path has no left edge, the left half its reflection; (2) C1’s right edge at σ = 2, ζ(3/2) − 1 exceeding 1; '
              '(3) eight workers under the hold; (4) the (3b) check points re-named onto σ = ½ after the first run, T4’s domain; (5) the (3d) tail '
              'read in three states, the pass condition the author’s alone')


def _trail_text():
    S, fj, rl, J, ld = (jl(n_) for n_ in ('b667_scores.json', 'b667_findings.json', 'b667_record_lines.json', 'b667_act_root.json', 'b667_landing.json'))
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b667_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    ls = (rl.get('lines') or []) + [{}]
    ll = (ld.get('lines') or []) + [{}, {}]
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R277) ratified.** (1) b666 at its weight. (2) The object: Q0’s list as b326 banks it. (3) The method’s shape, the route raised in '
             'a plan; (3a)-(3d) added on the author’s word. (4) The controls. (5) H1-H5. (6) The landing. (7) The draft held at v5. (8) The act '
             'after: b668.', '',
             '**Entered:** FINDINGS.md:%s (b666’s weight), :%s (the entry); OPEN_TRAILS.md:%s (W-ORD-EPSTEIN-CERTIFY DISCHARGED), :%s (the kernel '
             'item for P1 and P2); this record.' % (ls[0].get('line'), fj.get('entry_line'), ll[0].get('line'), ll[1].get('line')), '',
             '**Act root:** b667 `%s` (previous `%s`, b666’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF.' % (
                 J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d questions in %d calls (relay data/b667_author_answers.txt): the plan’s prompt of `(R277)`(3) before any '
             'number, its four amendments as the measurements raised them, the plan again before Component 3; none after the root.' % (n_ans, len(_calls())), '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b667_defects.txt): %s.' % ('; '.join(_defect_short()) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.**', '',
             '**Next:** %s.' % NEXT_LINE, '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b667_scores.json')
    L = ['=' * 104, 'b667 -- THE DESK.', '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in SCORE_KEYS]
    L += [''] + rdn('b667_defects.txt').rstrip(NL).split(NL)
    put_txt('b667_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl, J, ld = (jl(n_) for n_ in ('b667_scores.json', 'b667_findings.json', 'b667_trail.json', 'b667_record_lines.json',
                                              'b667_act_root.json', 'b667_landing.json'))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    ls = (rl.get('lines') or []) + [{}]
    ll = (ld.get('lines') or []) + [{}, {}]
    j, _rows = _cert()
    L = ['b667 -- THE COMPONENTS, BANKED UNDER (R277).', '',
         '### COMPONENT 0 : the citation check (data/b667_citation_check.txt), step zero (data/b667_ferry.txt, data/b667_stepzero.txt, '
         'data/b667_tests_stepzero.txt, data/b667_readfirst.txt) ; push-out relay %s' % K.STEPZERO,
         '### COMPONENT 1 : b666`s weight FINDINGS :%s' % ls[0].get('line'),
         '### COMPONENT 2 : the plan (data/b667_epstein_plan.txt), the obstruction (data/b667_bessel_obstruction.txt) ; N2 %s' % S['N2'][0],
         '### COMPONENT 3 : the isolation (data/b667_epstein_counts.txt, data/b667_epstein_zeros_certified.txt, data/b667_bessel_rungs.txt ; the '
         'stopped runs data/b667_certify_run1.txt to run3.txt) ; N(R) %s ; N(B) %s ; N3 %s' % (j.get('N_R'), j.get('N_B'), S['N3'][0]),
         '### COMPONENT 4 : the b663 control on the balls (data/b667_epstein_control_balls.txt, data/b667_map_balls_diff.txt) ; N4 %s' % S['N4'][0],
         '### COMPONENT 5 : the landing -- the dated line beneath data/b663_epstein_control.txt ; OPEN_TRAILS :%s (DISCHARGED), :%s (the kernel '
         'item) ; H1-H5 (data/b667_hypotheses.txt)' % (ll[0].get('line'), ll[1].get('line')),
         '### COMPONENT 6 : the dry-run step (data/b667_reg_gate.txt), the seal (data/b667_seal_hashes.json), the suite ; S3 %s' % S['S3'][0],
         '### COMPONENT 7 : the root %s ; FINDINGS :%s ; OPEN_TRAILS :%s ; N1 %s ; N5 %s' % (
             (J.get('root') or '')[:16], fj.get('entry_line'), tj.get('line'), S['N1'][0], S['N5'][0])]
    put_txt('b667_components.txt', L)
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
    ln = _land_one(FIND, t, e, 'b667_findings.json', dict(title=t))
    j = jl('b667_findings.json')
    j['entry_line'] = ln
    put_json('b667_findings.json', j)
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
    ln = _land_one(OT, TRAIL_HEAD(), e, 'b667_trail.json', {})
    print('  OPEN_TRAILS record :%s' % ln)


def _face_needles(face_text, which):
    m = re.search(r'^### THE DRY-RUN NEEDLES -- %s: (.*)$' % which, face_text, re.M)
    return re.findall(r'"([^"]+)"', m.group(1)) if m else []


def drycheck(*a):
    """(R267)(2), STANDING FROM b657: the FINDINGS entry and the trail record composed as the record tool composes them -- under stand-ins
    for the banks not yet written (the `standin` argument) -- converted by conv and run through the screens their landing runs, the needles
    the face names read in each; prints DRY-RUN STEP : CLEAN and exits 0 only when both screens are quiet and every needle is found. Writes
    no bank."""
    face = rd(a[0] if a and a[0] != 'standin' else FACE)
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


# ================================================================================ THE LARGE BANKS (the navigator's answer: option 1, the names fixed)
LARGE = ('b667_bessel_rungs.txt', 'b667_epstein_zeros_certified.json')


def gzbanks(*a):
    """the run's two large banks gzipped under their own names (-9, mtime 0), the run's bytes unchanged; each read back and compared byte for
    byte; data/b667_large_banks.txt with the uncompressed byte count, the sha256 of the uncompressed bytes and of the .gz; and
    data/b667_bessel_rungs_summary.txt, counts by m and by height. Deletes nothing (the seat deletes the uncompressed files after the read-back,
    one verified absolute path per command)."""
    import gzip
    import hashlib
    rows, rb = [], {}
    for n in LARGE:
        src = os.path.join(D, n)
        b = open(src, 'rb').read()
        z = gzip.compress(b, 9, mtime=0)
        gp = src + '.gz'
        if os.path.exists(gp):
            sys.exit('### %s.gz EXISTS -- NOTHING WRITTEN' % n)
        open(gp + '.tmp', 'wb').write(z)
        os.replace(gp + '.tmp', gp)
        back = gzip.decompress(open(gp, 'rb').read())
        eq = back == b
        rows.append((n, len(b), hashlib.sha256(b).hexdigest(), len(z), hashlib.sha256(open(gp, 'rb').read()).hexdigest(), eq))
        rb[n] = b
        print('  %s.gz : %d bytes from %d ; READ BACK BYTE-EQUAL %s' % (n, len(z), len(b), eq))
    if not all(r[5] for r in rows):
        sys.exit('### A READ-BACK DIFFERS -- THE BANKS NOT WRITTEN, NOTHING TO DELETE')
    L = ['b667 -- THE RUN`S TWO LARGE BANKS, GZIPPED UNDER THEIR OWN NAMES (%s), the navigator`s answer on the large banks: rows are banks -- the '
         'uncompressed byte count, the sha256 of the uncompressed bytes, the .gz`s byte count and sha256 as committed, the read-back.' % utc(), '']
    for n, nb, sh, nz, shz, eq in rows:
        L.append('  data/%s.gz | uncompressed %d bytes, sha256 %s | gz %d bytes, sha256 %s | read back byte-equal %s' % (n, nb, sh, nz, shz, eq))
    L += ['', '### the rows of data/b667_bessel_rungs.txt.gz are Bessel factors: m, the evaluation`s point (σ, t) at its centre, the precision; the',
          '### run printed no ball column for a factor (the answer`s "ball" not in the rows as written; nothing added). The rows of',
          '### data/b667_epstein_zeros_certified.json.gz are squares with their balls and their rung lists. Nothing re-written from the run`s output.']
    put_txt('b667_large_banks.txt', L)
    cnt_m, cnt_t = collections.Counter(), collections.Counter()
    tot = 0
    for l in rb['b667_bessel_rungs.txt'].decode('utf-8').split(NL):
        m = re.match(r'^  m\s+(\d+) \| σ (\S+) \| t (\S+) \| (\d+) bits', l)
        if m:
            tot += 1
            cnt_m[int(m.group(1))] += 1
            cnt_t[int(float(m.group(3)) // 10) * 10] += 1
    S_ = ['b667 -- THE BESSEL FACTORS TAKEN AT 600 BITS, SUMMARISED (%s), from data/b667_bessel_rungs.txt.gz: rows are counts -- by m, then by height '
          '(t in bands of 10).' % utc(), '']
    S_ += ['  m %2d : %d' % (k, cnt_m[k]) for k in sorted(cnt_m)] + [''] + ['  t in [%3d, %3d) : %d' % (k, k + 10, cnt_t[k]) for k in sorted(cnt_t)]
    S_ += ['', '### ### **FACTORS %d ; the run`s own total line %s.**' % (tot, re.search(r'FACTORS AT 600 BITS: \d+', rb['b667_bessel_rungs.txt'].decode('utf-8')).group(0))]
    put_txt('b667_bessel_rungs_summary.txt', S_)
    print(S_[-1])


def cert_json():
    """the certified rows, read from data/b667_epstein_zeros_certified.json.gz (I/O alone)."""
    import gzip
    p = os.path.join(D, 'b667_epstein_zeros_certified.json.gz')
    if not os.path.exists(p):
        return jl('b667_epstein_zeros_certified.json')
    return json.loads(gzip.decompress(open(p, 'rb').read()).decode('utf-8'))


# ================================================================================ THE DIFFS ((R277)(3d); Component 4)
def diffs(*a):
    """data/b667_certify_diff_run3.txt: tools/b667_epstein_certify.py at the second run's commit (15918f9d) against the working file; and
    data/b667_map_balls_diff.txt: tools/b663_epstein_map.py against tools/b667_epstein_map_balls.py. Each git diff's output whole."""
    out = {}
    r = subprocess.run(['git', '-C', ROOT, 'diff', '15918f9d', '--', 'tools/b667_epstein_certify.py'], capture_output=True)
    out['b667_certify_diff_run3.txt'] = ('b667 -- THE CERTIFY SCRIPT, THE THIRD RUN`S AGAINST THE SECOND`S (15918f9d) ((R277)(3d)): `git diff 15918f9d -- '
                                         'tools/b667_epstein_certify.py`, whole.', r.stdout.decode('utf-8', 'replace').replace(chr(13), ''))
    r = subprocess.run(['git', '-C', ROOT, 'diff', 'be6b8d76', '--', 'tools/b667_epstein_certify.py'], capture_output=True)
    out['b667_certify_diff_run4.txt'] = ('b667 -- THE CERTIFY SCRIPT, THE FOURTH RUN`S AGAINST THE THIRD`S (be6b8d76) (defect (g)): `git diff be6b8d76 -- '
                                         'tools/b667_epstein_certify.py`, whole.', r.stdout.decode('utf-8', 'replace').replace(chr(13), ''))
    r = subprocess.run(['git', '-C', ROOT, 'diff', '--no-index', 'tools/b663_epstein_map.py', 'tools/b667_epstein_map_balls.py'], capture_output=True)
    out['b667_map_balls_diff.txt'] = ('b667 -- THE b663 MAP CARRIED ONTO THE BALLS ((R277)(5) H4): `git diff --no-index tools/b663_epstein_map.py '
                                      'tools/b667_epstein_map_balls.py`, whole.', r.stdout.decode('utf-8', 'replace').replace(chr(13), ''))
    for name, (head, body) in out.items():
        put_txt(name, [head, ''] + body.rstrip(NL).split(NL))
        print('  %s : %d lines, %d removed, %d added' % (name, len(body.split(NL)), sum(1 for l in body.split(NL) if l.startswith('-') and not l.startswith('---')),
                                                       sum(1 for l in body.split(NL) if l.startswith('+') and not l.startswith('+++'))))


ROUTES = {'c1': c1, 'answers': answers, 'diffs': diffs, 'gzbanks': gzbanks, 'hypotheses': hypotheses, 'landing': landing, 'commands': commands, 'kernels': kernels,
          'defects': defects, 'root': root, 'root_arm': root_arm, 'table_final': table_final, 'gatebanks': gatebanks, 'scores': scores,
          'desk': desk, 'components': components, 'findings': findings, 'trail': trail, 'drycheck': drycheck}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b667_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
