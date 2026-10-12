# -*- coding: utf-8 -*-
"""b656_record.py -- THE ACT'S RECORD TOOL, b656 under (R266).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b656's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows (tools/b656_regspec.py) can run each reader over one row of each shape before the seal.
### Carried from b655_record.py at b656 by the Write tool: the guarded landing, the answers, the command capture, the kernels' face, the
### defects, the seal hashes, the root and its arm, the terminal table, the desk, the components and the mirror routes as b655 wrote them;
### b655's grade, cut and runner routes not carried (no kernel is cut or built in this act); c1, the cell reader and the act's scores new.
### Routes: `python tools/b656_record.py <route> [dry]`; each route banks under data/ and prints what it wrote.
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
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/1199f364-78c4-4147-843f-edf01bb11b28/scratchpad'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from b652_record import conv, append_to, guard_absent, line_of, odd_lines   # noqa: E402,F401  ### the one conversion, imported
import b656_worklist as K          # noqa: E402


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def rd(path):
    return io.open(path, encoding='utf-8').read().replace(chr(13), '') if os.path.exists(path) else ''


def rdn(name):
    return rd(os.path.join(D, name))


def put_json(name, obj):
    b = (json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)


def put_txt(name, lines):
    b = (NL.join(lines) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)


def jl(name):
    try:
        return json.load(io.open(os.path.join(D, name), encoding='utf-8'))
    except Exception:
        return {}


def g(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def _show(repo, rev, path):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b656's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b656_scanfile_%s.md' % tag)
    R3._write(p, allt.encode('utf-8'))
    sc = R3._scan(p)
    clean = R3._clean(sc)
    ticks = odd_lines(allt)
    unread = [x for x in ('### NOT', 'None', ' ? ', '`?`') if x in allt]
    outside = [n for n in R41.OAI_NEEDLES if n in allt]
    stems = [s for s in ('gap', 'blind') if re.search(r'\b' + s, allt, re.I)]
    widths = [w for w in ('33.19', '38.96') if w in allt]
    print('  table cells: %s ; no-disclosure hits: %s ; scanner %s ; odd backticks by line: %s ; unread figures: %s ; outside names: %s ; '
          'stems: %s ; plateau widths: %s' % (cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN', ticks or 'NONE', unread or 'NONE',
                                              outside or 'NONE', stems or 'NONE', widths or 'NONE'))
    if not clean:
        print(sc[-1500:])
    fired = bool(any(nd.values()) or not clean or ticks or unread or outside or stems or widths)
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
RUNNER_KEYS = ('kernel', 'branch', 'ref', 'target', 'run_id', 'conclusion', 'artifact_sha256', 'mem_low', 'stopped', 'gate', 'merged', 'tag')


def read_runner_row(r):
    """a row of a runner-rows bank (this act reads b654's, the kernel's last run) -- every key of RUNNER_KEYS present (None where a step did
    not reach it); returns the row's reading (kernel, outcome, merged); raises KeyError on a row of another shape."""
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


def read_score_row(k, v):
    """a scores row: key N1..N5 or S1..S5 or H1..H3, value [verdict, text]; returns (key, first verdict word, text)."""
    if not re.match(r'^[NSH][1-5]$', k) or not isinstance(v, list) or len(v) != 2:
        raise ValueError('score row of another shape: %r' % (k,))
    return k, v[0].split(' ')[0], v[1]


def read_head(path, head):
    """a landed head looked up in a ledger through the one conversion; returns its line or raises."""
    ln = line_of(path, head)
    if ln is None:
        raise LookupError('head not found through conv: %s' % head[:60])
    return ln


READERS = ('read_runner_row', 'read_score_row', 'read_head')


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R266)(1), (2)
WH = ('*Appended 2026-10-12 by b656 to b655’s entry (:8337), under `(R266)`(1) -- b655 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b655_closing.txt):*')
CH = ('*Appended 2026-10-12 by b656 beneath the b655 record (:13970), under `(R266)`(2) -- `(R265)`(7) CORRECTED, THE NAVIGATOR’S:*')
MH = ('*Appended 2026-10-12 by b656 beside the correction, under `(R266)`(1) -- THE MIRROR CLAUSE, AS IT READS FROM b656:*')


def _weight():
    return ('\n' + WH + ' SIDE-global-section (43 OVERREACHES, relay data/b647_table_kernels.txt :12) -- 51 blocks, 348 sentence rows, 65 '
            'graded by hand with the cell’s words beside each, #46’s bullets graded one by one, #50’s “So:” sentence standing on its surviving '
            'premise; the cut in 33 commits, no file changed outside comments, 0 graded rows standing at the branch; the workflow on main at '
            '0b5949a by the kernel’s own build path (no lakefile), run 38276189411 building 113 Core modules with every one of 643 prints equal to '
            'the banked profiles, memory low 7,197 MB; merged alone at 504e146, tag v0.3.0; G-EDIT-ROUTE repaired, 28 of 28, a glob delete with a '
            'redirect still failing; the mirror at D:/MY-DOwnloads/mirror-refresh-2026-10-12-b655.zip (MANIFEST md5 5eedff09…, PLACE-papers '
            '651aedb), CLEAN on all three clauses; relay c296f930, PLACE-papers 651aedb, FINDINGS :8335 and :8337, OPEN_TRAILS :13968 and :13970, '
            'the root 99ca2e09…; the suite 78 of 79, the SIDE-cosmo row declared; three defects (relay data/b655_defects.txt), each caught before '
            'a kernel byte. Nothing deposited.\n')


def _correction():
    return ('\n' + CH + ' `(R265)`(7) named “the Q0 configuration (disc −23, the b548/b549 bench)” as the place to evaluate E1. Two errors in '
            'one clause, the navigator’s. E1 is stated on zetaZeroConfig (relay data/b654_e1_statement.txt :24, :55; SIDE-explicit-formula '
            'RateIndex.lean :27, :113 at v0.27), not on an Epstein configuration, and the kernel has no Epstein instance to bind to '
            '(W-ORD-EPSTEIN-ZQ, no rung built). And the b548/b549 bench is the plateau family with B-spline ramps, not the power-window family '
            'E1’s kWindow ranges over -- the conflation b550 corrected as the navigator’s (FINDINGS.md:5681). The bench’s plateau widths are not '
            'inputs to b656 and are compared with nothing in it; b656 binds E1’s quantities to the kernel and, on the author’s word, maps its rate '
            'inequality over hypothetical off-line zeros of ζ (`(R266)`(3)-(4)).\n')


def _mirror_clause():
    return ('\n' + MH + ' the mirror export is built after the act’s last PLACE-papers push and before the closing record, so the closing prints '
            'its MANIFEST md5 and the last commit it carries -- b655’s reading of `(R265)`(5), the clause from here (`(R266)`(1)).\n')


def c1(*a):
    items = [('FINDINGS.md', WH, _weight()), ('OPEN_TRAILS.md', CH, _correction()), ('OPEN_TRAILS.md', MH, _mirror_clause())]
    land(items, 'b656_record_lines.json', 'c1', entry=8337,
         check=[('FINDINGS.md', 8337, '## SIDE-global-section’s docstrings at 65 sentence rows'),
                ('OPEN_TRAILS.md', 13970, '### b655 — lane three, act eighty-two')],
         dry='dry' in a)


# ================================================================================ COMPONENT 2: THE AUTHOR'S WORD ON THE BINDING -- STOPPED HERE
# ### the author's answer (relay data/b656_author_answers.txt): Option 2, the act stops at Component 2 with the result named; no map, no
# ### H1-H3 (NOT SCORED, O-2 the reason); W-ORD-E1-CFG entered on OPEN_TRAILS; the grid lesson beside it, the navigator's.
EH = ('### `W-ORD-E1-CFG` -- E1’S RATE THEOREM OVER A CONFIGURATION WITH AN EXCLUDED ZERO AND A LOCAL COUNT, PRICED, NOT STARTED, appended '
      '2026-10-12, b656, under the author’s ruling `(R266)`(3) and the author’s word on the binding')
GH = ('*Appended 2026-10-12 by b656 beside W-ORD-E1-CFG, under the author’s word on `(R266)`(3) -- A GRID LESSON, THE NAVIGATOR’S:*')


def _e1_cfg():
    return ('\n' + EH + '\n\n**Items.** rest_norm_le_rate and zeroSide_neg_at_rate (SIDE-explicit-formula RateIndex.lean :27, :113, v0.27) are '
            'stated on zetaZeroConfig alone, whose carrier is ζ’s genuine zeros by rfl (Zeta23/Statement/SeamClosed.lean :42, :44): no '
            'hypothetical off-line zero is in their tie set, and hrate’s right side has no referent there (O-1); the kernel has no '
            'configuration-level rate theorem -- Schema/Converse.lean carries the limit form zeroSide_eventually_neg_cfg (:161) and the twins '
            'sT_cfg, fR_cfg, dominant_summable_cfg, but no rate (O-2); the full configuration’s A₀ is existential (Zeta23/RvM/LocalCount.lean '
            ':287; O-3). The item: the rate theorem over a configuration with an excluded zero and a local count, ζ an instance by rfl as v0.15 '
            'made the seam. **Price:** from the binding bank’s O-1 to O-3 (relay data/b656_e1_binding.txt): the two statements restated over a '
            'Schema.WeilConfig, their proofs using zetaZeroConfig only through dominant_summable, fR, sT and zeroSide (RateIndex.lean :84, :103, '
            ':151), each with a twin in Converse.lean; the ζ instance by rfl. **Trigger:** this finding. **Acted:** at b658, the next research '
            'act, on the runner.\n')


def _grid_lesson():
    return ('\n' + GH + ' `(R266)`(4) fixed J_max at 12 without reading D = 2 · card Xr + 8 ≥ 8 from coeffs_exist’s witness (PowerLimit.lean '
            ':683; relay data/b656_e1_binding.txt, row D): under it at most five indices could be tested, and none at a cell whose kill set has '
            'three ordinates or more. Any later grid sets J_max relative to D, not absolutely.\n')


def c2(*a):
    items = [('OPEN_TRAILS.md', EH, _e1_cfg()), ('OPEN_TRAILS.md', GH, _grid_lesson())]
    land(items, 'b656_trail_lines.json', 'c2', entry=13992,
         check=[('OPEN_TRAILS.md', 13992, 'THE MIRROR CLAUSE, AS IT READS FROM b656')], dry='dry' in a)


# ================================================================================ THE LATE ROUTES (b655's, carried; every row read through READERS)
import collections                 # noqa: E402
import b633_record as R3           # noqa: E402
import edit_route as ER            # noqa: E402
RELAY = ROOT
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID
SUBAGENTS = 'C:/Users/echo chamber/.claude/projects/D--/%s/subagents' % K.SESSION_ID
R3.SP, R3.SESSION, R3.SESSION_ID = SP, SESSION, K.SESSION_ID


def _session_rows():
    """the session's lines from the first user line carrying this act's anchor."""
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
    """data/b656_author_answers.txt: every prompt put by the seat in this act, with its options and the answer; and every word of the author
    delivered between BEGIN and END after the ruling (user lines and queued commands), and the author's plain messages, verbatim."""
    calls, results, words, plain, start = [], {}, [], [], None
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
                    plain.append((i, t.strip()))
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
    for i, t in plain:
        W += ['### THE AUTHOR`S MESSAGE (transcript line %d), verbatim: %s' % (i, t.replace('\r', '').replace(NL, ' ')), '']
    nw = len([x for x in W if x.startswith('### THE AUTHOR`S WORD')])
    head = ['### b656 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d).' % (
                n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start), '']
    put_txt('b656_author_answers.txt', [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    put_json('b656_author_answers.json', dict(at=utc(), calls=[dict(line=i, id=cid, ts=ts, result_ts=(results.get(cid) or (None, None, None))[2])
                                                               for i, cid, _inp, ts in calls]))
    print('  prompts banked: %d ; words banked: %d' % (n, nw))


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
    L = ['b656 -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING AND THE LOCAL LEAN READING (N1) (%s)' % utc(), '',
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
    put_txt('b656_commands.txt', [l.replace('\r', '') for l in L])
    put_json('b656_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                        local_lean=[r['n'] for r in lean]))
    print(L[-1])


def kernels(*a):
    import b641_record as R41
    put_json('b656_kernels_face.json', dict(at=utc(), kernels=R3.kern_state(list(R41.KERNS_READ))))
    print('  kernels read: %d' % len(R41.KERNS_READ))


def _defect_short():
    return [re.match(r'^\(([a-z])\) ([^.]*)\.', l.strip()).group(0)[:-1].lower() for l in rdn('b656_defects.txt').split(NL)
            if re.match(r'^    \([a-z]\) [^.]*\.', l)]


def defects(*a):
    t = rdn('b656_defects.txt')
    ds = [l.strip() for l in t.split(NL) if re.match(r'^    \([a-z]\) ', l)]
    put_json('b656_defects.json', dict(at=utc(), defects=ds, short=_defect_short()))
    print('  defects %d' % len(ds))


def seal_hashes():
    import hashlib
    rec_ = jl('b656_seal_hashes.json').get('tools') or {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


ROOT_EXCLUDE = re.compile(r'^b656_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|closing.*|mirror.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|commands)\.(txt|json|md)$')


def root_banks():
    return sorted('data/' + f for f in os.listdir(D) if f.startswith('b656_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f))


def root(*a):
    banks = root_banks()
    crlf = [b for b in banks if b'\r\n' in open(os.path.join(ROOT, *b.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/b656_seal_hashes.json' in banks, crlf or 'none'))
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b656'] + banks + ([] if 'dry' in a else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import shutil
    import tempfile
    import act_root as AR
    J = jl('b656_act_root.json')
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/')][0]
    tmp = tempfile.mkdtemp()
    cp = os.path.join(tmp, os.path.basename(bank_))
    shutil.copy(os.path.join(ROOT, *bank_.split('/')), cp)
    b = bytearray(open(cp, 'rb').read())
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
    L = ['b656 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '?')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b656_root_arm.txt', L)
    put_json('b656_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
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
    L = ['b656 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (utc(), r.returncode, g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b656_table_final.txt', L)
    put_json('b656_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


NK = ('N1', 'N2', 'N3', 'N4', 'N5')
HK = ('H1', 'H2', 'H3')
SK = ('S1', 'S2', 'S3')
SCORE_KEYS = NK + HK + SK
N5_RELAY_DATA = ('act_roots.txt', 'b655_closing_push_out.txt')
N5_PP = ('FINDINGS.md', 'OPEN_TRAILS.md')
WIDTHS = ('33' + '.19', '38' + '.96')
COMPUTE_CALL = re.compile(r'zeta_zeros?\(|\.integral\(')


def TRAIL_HEAD():
    return ('### b656 — lane two, act eighty-three, the research act under (R266): b655 at its weight; (R265)(7) corrected; E1’s quantities '
            'bound to the kernel at v0.27; stopped at Component 2 on the author’s word; W-ORD-E1-CFG filed; the mirror export')


def _stopped():
    """no certified computation called in the act's capture, no map bank, no map script: the stop of the author's word, read."""
    rows = capture()
    calls = [r['n'] for r in rows if r['tool'] in ('Bash', 'PowerShell') and COMPUTE_CALL.search(r['cmd'])]
    files = sorted(f for f in os.listdir(D) if f.startswith('b656_detection_map')) + sorted(f for f in os.listdir(T) if f.startswith('b656_detection_map'))
    return calls, files


def _widths():
    hits = []
    for f in sorted(os.listdir(D)):
        if f.startswith(('b656_', 'audit_b656_')) and f != 'b656_ferry.txt' and os.path.isfile(os.path.join(D, f)):
            if any(w in rd(os.path.join(D, f)) for w in WIDTHS):
                hits.append(f)
    return hits


def _n2():
    """N2: every quantity of hrate bound by file and line before any number, or the act stopped at Component 2."""
    b = rdn('b656_e1_binding.txt')
    files = g(RELAY, 'show', '--name-only', '--pretty=format:', K.BINDING_COMMIT).split()
    aj = jl('b656_author_answers.json').get('calls') or []
    ask = _iso(aj[0]['ts']) if aj and aj[0].get('ts') else None
    ct = _ct(RELAY, K.BINDING_COMMIT)
    word = 'Option 2, stop at Component 2' in rdn('b656_author_answers.txt')
    calls, mfiles = _stopped()
    ok = files == ['data/b656_e1_binding.txt'] and ask and ct and ct < ask and word and not calls and not mfiles and '(O-1)' in b
    return ('HELD' if ok else 'REFUTED'), (
        'by its second arm: the act stopped at Component 2 on the author`s word (relay data/b656_author_answers.txt, Option 2), the binding '
        'banked by file and line with O-1 to O-3 named (relay data/b656_e1_binding.txt, committed alone at %s, %s) before the one prompt (%s); '
        'certified computations called %s, map banks or scripts %s -- no number computed' % (
            K.BINDING_COMMIT, time.strftime('%H:%M:%SZ', time.gmtime(ct)) if ct else '?', time.strftime('%H:%M:%SZ', time.gmtime(ask)) if ask else '?',
            calls or 'NONE', mfiles or 'NONE'))


def _n5():
    face = jl('b656_kernels_face.json').get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    kern_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in N5_PP]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b656_|audit_b656_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('data/') and x[5:] in N5_RELAY_DATA))]
    km = g(K.KD, 'rev-parse', '--short=7', 'main').strip()
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    import b656_checks as CH
    new_arms = sorted(set(a[0] for a in CH.ARMS) - set(CH.STANDING) - set(K.ACT_ARMS))
    ok = kern_ok and not pp_beyond and not kinds_beyond and not differ and km == K.K_MAIN and not new_arms
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unsubmitted); no kernel main written (SIDE-explicit-formula main %s, '
            'v0.27, as the act began); every kernel as the face read it %s; standing arms added: %s (the act`s arms over its own banks %d); sealed '
            'tools not agreeing %s; PLACE-papers beyond FINDINGS and OPEN_TRAILS: %s; relay files of a kind beyond the banks, the tools and the '
            'root list: %s; no identifier of the author in any outbound request (git pushes and remote reads alone)' % (
                K.DRAFT, km, kern_ok, new_arms or 'NONE', len(K.ACT_ARMS), differ or 'NONE', pp_beyond or 'NONE', kinds_beyond or 'NONE'))


NOT_SCORED = 'NOT SCORED'
O2 = ('O-2: E1 is stated at zetaZeroConfig alone and has no form over a configuration with an excluded zero, so a map at the cell`s '
      'configuration would be E1`s expression where E1 says nothing; on the author`s word no map was computed (relay data/b656_e1_binding.txt, '
      'data/b656_author_answers.txt)')


def scores(*a):
    TF, RA = jl('b656_table_final.json'), jl('b656_root_arm.json')
    _r, _n, sh = seal_hashes()
    cm = jl('b656_commands.json')
    calls, mfiles = _stopped()
    wh = _widths()
    S = {
        'N1': (('HELD' if cm and not cm.get('local_lean') else 'REFUTED'),
               'commands of this act that run lean or lake on this host: %s (relay data/b656_commands.txt); no kernel file written (N5)' % (
                   cm.get('local_lean') if cm else '### UNREAD')),
        'N2': _n2(),
        'N3': (NOT_SCORED, 'H3 was not computed; ' + O2),
        'N4': (NOT_SCORED, 'no map was computed, so no grid cell is banked; ' + O2 + '. Its second clause read: a plateau width in the banks the '
               'seat wrote and the ledger lines appended %s; the ferry bank (relay data/b656_ferry.txt) carries the two widths in the ruling`s own '
               'sentence, verbatim' % (wh or 'NONE')),
        'N5': _n5(),
        'H1': (NOT_SCORED, O2), 'H2': (NOT_SCORED, O2), 'H3': (NOT_SCORED, O2),
        'S1': (('HELD' if not TF.get('gone') and not TF.get('grade_moved') else 'REFUTED') if TF else 'PENDING',
               'the table at the end against relay HEAD`s: moved %s, gone %s, added %s, grade moved %s' % (
                   len(TF.get('moved') or []), len(TF.get('gone') or []), len(TF.get('added') or []), len(TF.get('grade_moved') or []))),
        'S2': (('HELD' if RA.get('root_recomputed') == RA.get('root') and RA.get('root_copy') != RA.get('root') and not RA.get('late') else 'REFUTED')
               if RA else 'PENDING', 'the root recomputed equal, the one-byte control moving it, the root order holding locally'),
        'S3': ('HELD' if sh and all(v == 'agree' for _t, v in sh) else 'REFUTED', 'the sealed tools` hashes %s' % dict(collections.Counter(v for _t, v in sh))),
    }
    for k2 in SCORE_KEYS:
        read_score_row(k2, list(S[k2]))
    put_json('b656_scores.json', dict((k2, list(v)) for k2, v in S.items()))
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:500]))


def _ct(repo, *a):
    s = g(repo, 'log', '-1', '--format=%ct', *a).strip()
    return int(s) if s.isdigit() else None


def _iso(s):
    import calendar
    try:
        return calendar.timegm(time.strptime((s or '')[:19], '%Y-%m-%dT%H:%M:%S'))
    except Exception:
        return None


NEXT_LINE = ('b657, per `(R266)`(7), the re-cut act on SIDE-lv-conservation (35 OVERREACHES, relay data/b647_table_kernels.txt :17) in the '
             'form of `(R265)`; W-ORD-E1-CFG acted at b658, the next research act, on the runner')


def _title():
    return ('## E1’s quantities bound to the kernel at v0.27: no hypothetical zero in its tie set, no configuration-level rate theorem, the full '
            'configuration’s A₀ existential -- the act stopped at Component 2; the (R265)(7) correction')


def _finding_text():
    S, rl, tl, J = jl('b656_scores.json'), jl('b656_record_lines.json'), jl('b656_trail_lines.json'), jl('b656_act_root.json')
    ans = rdn('b656_author_answers.txt')
    n_ans = len(re.findall(r'^### PROMPT ', ans, re.M))
    ls = (rl.get('lines') or []) + [{}, {}, {}]
    ts = (tl.get('lines') or []) + [{}, {}]
    sc = lambda k: read_score_row(k, S.get(k) or ['?', ''])[1] if S.get(k) else '?'   # noqa: E731
    e = ['', _title(), '',
         '*Filed at b656 on the author’s ruling `(R266)` and the author’s word on the binding (%d prompt). Banks: relay `data/b656_e1_binding.txt`, '
         '`data/b656_readfirst.txt`, `data/b656_author_answers.txt`, `data/b656_act_root.txt`.*' % n_ans, '',
         '**The binding** (`(R266)`(3)): every quantity of E1’s rate inequality and of the statement of zeroSide_neg_at_rate -- θ, A₀, Bf, '
         'zeta3Sum, D, the tie set and its multiplicities, Nf, M, L, g0, the dominant zero, the kill set, ℓ -- read from SIDE-explicit-formula '
         'at v0.27 and bound by file and line, the b559 constants table beside each row, before any number. Three findings. (O-1) E1 is stated '
         'on zetaZeroConfig alone (RateIndex.lean :27, :113), whose carrier is ζ’s nontrivial zeros by rfl (Zeta23/Statement/SeamClosed.lean '
         ':42, :44): no hypothetical off-line zero is in its tie set, and the right side of its rate inequality has no referent at a grid point. '
         '(O-2) The kernel has no configuration-level rate theorem: Schema/Converse.lean carries the limit form zeroSide_eventually_neg_cfg '
         '(:161) and the twins of the rest’s parts, but no rate. (O-3) The full configuration’s A₀ is existential (Zeta23/RvM/LocalCount.lean '
         ':287, over zeta_growth_right’s existential constants). At the cell’s own configuration -- the orbit of four and ζ’s zeros below a '
         'height -- every quantity binds to a kernel definition, each explicit or a finite maximum, and only E1’s implication does not. Read '
         'beside the ruling’s grid: D = 2 · card Xr + 8 ≥ 8 from coeffs_exist’s witness (PowerLimit.lean :683). N2 %s.' % sc('N2'), '',
         '**The stop** (the author’s word on `(R266)`(3)): Option 2 -- the act stops at Component 2, the binding its finding. A map at the cell’s '
         'configuration would be E1’s expression at a configuration E1 says nothing about. No map, no number; H1, H2 and H3 NOT SCORED, O-2 the '
         'reason; N3 %s, N4 %s. W-ORD-E1-CFG entered on OPEN_TRAILS (:%s): the rate theorem over a configuration with an excluded zero and a '
         'local count, ζ an instance by rfl, priced from O-1 to O-3, acted at b658 on the runner; the grid lesson beside it, the navigator’s '
         '(:%s): J_max set relative to D, not absolutely.' % (sc('N3'), sc('N4'), ts[0].get('line'), ts[1].get('line')), '',
         '**The record lines** (`(R266)`(1), (2)): b655 at its weight (FINDINGS :%s); `(R265)`(7) corrected as the navigator’s (OPEN_TRAILS :%s); '
         'the mirror clause as it reads from here (:%s).' % (ls[0].get('line'), ls[1].get('line'), ls[2].get('line')), '',
         '**The root.** b656 over %d repositories, %d tags and %d banks, the last step of the act’s banks; its chain read at commit inside the suite.' % (
             len((J.get('reads') or {}).get('heads') or []), len((J.get('reads') or {}).get('tags') or []), len((J.get('reads') or {}).get('banks') or [])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k2, (S.get(k2) or ['?'])[0]) for k2 in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): this binding re-reads b559’s constants table (relay `data/b559_constants.txt` :143-:152) '
         'and b654’s statement of E1 (relay `data/b654_e1_statement.txt`), and finds the reach b559 named -- “quantities of the zero '
         'configuration” -- carried into E1’s statement as one fixed configuration; it is re-read by W-ORD-E1-CFG at b658 and by the next '
         'reading act. It strengthens the programme’s offering of statements a reader can check: the rate is a compiled theorem with its '
         'hypotheses named, and where it applies is now said by file and line, before any number is attached to it.', '',
         '**Next.** %s.' % NEXT_LINE, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero; no number was computed, and a binding names where a theorem '
         'applies and confers nothing beyond it.*', '']
    return _title(), NL.join(e)


FOR_AUTHOR = ('(1) the cell`s configuration read as the orbit of four (a zero of ζ brings its conjugate and its reflection), every multiplicity 1, '
              'and ζ`s zeros below T = 1000, the height the binding fixed; (2) D and B bound to coeffs_exist`s witness as read, a smaller pair '
              'E1 admits named and not used; (3) H1-H3 scored NOT SCORED with O-2 the reason, and N3 and N4 with them, the second clause of N4 '
              'read and printed beside it')


def _trail_text():
    S, fj, rl, tl, J = (jl(n_) for n_ in ('b656_scores.json', 'b656_findings.json', 'b656_record_lines.json', 'b656_trail_lines.json', 'b656_act_root.json'))
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b656_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    ls = (rl.get('lines') or []) + [{}, {}, {}]
    ts = (tl.get('lines') or []) + [{}, {}]
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R266) ratified.** (1) b655 at its weight; the mirror clause as the seat read it. (2) `(R265)`(7) corrected, the navigator’s. (3) '
             'The binding, before any number. (4) The evaluation, on the author’s word -- the word was to stop at Component 2. (5) No kernel edit. '
             '(6) The draft held at v5. (7) The act after: b657.', '',
             '**Entered:** FINDINGS.md:%s (b655’s weight), :%s (the entry); OPEN_TRAILS.md:%s (the correction), :%s (the mirror clause), :%s '
             '(W-ORD-E1-CFG), :%s (the grid lesson); this record.' % (ls[0].get('line'), fj.get('entry_line'), ls[1].get('line'), ls[2].get('line'),
                                                                     ts[0].get('line'), ts[1].get('line')), '',
             '**Act root:** b656 `%s` (previous `%s`, b655’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF.' % (
                 J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d (relay data/b656_author_answers.txt), the one of `(R266)`(3), before any number; none after the root.' % n_ans, '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b656_defects.txt): %s.' % ('; '.join(_defect_short()) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, (S.get(k2) or ['?'])[0]) for k2 in SCORE_KEYS) + '.**', '',
             '**Next:** %s.' % NEXT_LINE, '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b656_scores.json')
    L = ['=' * 104, 'b656 -- THE DESK.', '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in SCORE_KEYS]
    L += [''] + rdn('b656_defects.txt').rstrip(NL).split(NL)
    put_txt('b656_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl, tl, J = (jl(n_) for n_ in ('b656_scores.json', 'b656_findings.json', 'b656_trail.json', 'b656_record_lines.json',
                                              'b656_trail_lines.json', 'b656_act_root.json'))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    ls = (rl.get('lines') or []) + [{}, {}, {}]
    ts = (tl.get('lines') or []) + [{}, {}]
    L = ['b656 -- THE COMPONENTS, BANKED UNDER (R266).', '',
         '### COMPONENT 0 : step zero (data/b656_ferry.txt, data/b656_stepzero.txt, data/b656_tests_stepzero.txt) ; push-out relay %s' % K.STEPZERO,
         '### COMPONENT 1 : the read-first (data/b656_readfirst.txt) ; b655`s weight FINDINGS :%s ; the correction OPEN_TRAILS :%s ; the mirror clause :%s' % (
             ls[0].get('line'), ls[1].get('line'), ls[2].get('line')),
         '### COMPONENT 2 : the binding (data/b656_e1_binding.txt, relay %s) ; the one prompt, Option 2: stopped here ; W-ORD-E1-CFG OPEN_TRAILS :%s ; '
         'the grid lesson :%s ; N2 %s' % (K.BINDING_COMMIT, ts[0].get('line'), ts[1].get('line'), S['N2'][0]),
         '### COMPONENT 3 : NOT RUN, on the author`s word ; H1 %s ; H2 %s ; H3 %s ; N3 %s ; N4 %s' % (S['H1'][0], S['H2'][0], S['H3'][0], S['N3'][0], S['N4'][0]),
         '### COMPONENT 4 : the seal (data/b656_seal_hashes.json) ; S3 %s' % S['S3'][0],
         '### COMPONENT 5 : the root %s ; FINDINGS :%s ; OPEN_TRAILS :%s ; N1 %s ; N5 %s' % ((J.get('root') or '')[:16], fj.get('entry_line'), tj.get('line'),
                                                                                        S['N1'][0], S['N5'][0])]
    put_txt('b656_components.txt', L)
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
    ln = _land_one(FIND, t, e, 'b656_findings.json', dict(title=t))
    j = jl('b656_findings.json')
    j['entry_line'] = ln
    put_json('b656_findings.json', j)
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
    ln = _land_one(OT, TRAIL_HEAD(), e, 'b656_trail.json', {})
    print('  OPEN_TRAILS record :%s' % ln)


# ================================================================================ THE MIRROR, AT THE CLOSE ((R266)(1); b655's routes, carried)
# ### after the act's last PLACE-papers push and before the closing record: the unedited builder (-DateTag only) on the standing roster, the
# ### roots file's last line (b656's root) added to MANIFEST in the stage, verified from PLACE-papers by mirror_verify.py, banked; the closing
# ### prints its MANIFEST md5 and last commit. Its banks are written after the root and are not named by it.
import hashlib as _hl   # noqa: E402

MIRROR_TAG = '2026-10-12-b656'
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
    put_json('b656_mirror_build.json', dict(at=utc(), rc=r.returncode, out=r.stdout, err=r.stderr, seconds=int(time.time() - t0), pp_head=loc))
    print(r.stdout[-800:], r.stderr[-400:], 'exit', r.returncode)


def mroot(*a):
    last = [l for l in io.open(os.path.join(D, 'act_roots.txt'), encoding='utf-8').read().split(NL) if l.strip()][-1].split()
    if last[0] != 'b656':
        sys.exit('### THE ROOTS FILE`S LAST LINE IS %s, NOT b656`s -- NOTHING WRITTEN' % last[0])
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
    put_json('b656_mirror_root.json', dict(at=utc(), line=line, bom=bom, zip_sha_before=before, zip_sha_after=after, update_rc=ps.returncode))
    print('  %s ; update rc %d ; zip sha256 %s -> %s' % (line, ps.returncode, before[:16], after[:16]))


def mverify(*a):
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'mirror_verify.py'), ZIP, 'origin', 'main'], cwd=PP,
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    put_txt('b656_mirror_verify.txt', (r.stdout + r.stderr + '### exit %d' % r.returncode).replace(chr(13), '').split(NL))
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
    clean = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in rdn('b656_mirror_verify.txt')
    nd = R6.nd_hits(NL.join(names), R6.nd_sets())[0]
    files_ = [n for n in names if n != 'MANIFEST.md']
    pp_head = g(PP, 'rev-parse', '--short=7', 'HEAD').strip()
    L = ['b656 -- THE MIRROR-REFRESH EXPORT, BUILT AFTER THE LAST PLACE-papers PUSH BY THE UNEDITED BUILDER, banked %s' % utc(),
         '### THE ZIP : %s ; %d bytes ; md5 %s ; sha256 %s' % (ZIP, len(zb), _hl.md5(zb).hexdigest(), _hl.sha256(zb).hexdigest()),
         '### THE MANIFEST : md5 %s ; entries in the zip %d (files %d + MANIFEST)' % (_hl.md5(man).hexdigest(), len(names), len(files_)),
         '### PLACE-papers HEAD AT THE BUILD : %s ; the last commit carried in MANIFEST`s rows %s' % (pp_head, pp_head in commits),
         '### THE ROSTER LINE : %s' % (' / '.join(rosterl) or '### NONE'), '### THE ROOT LINE : %s' % (rootl[0] if rootl else '### NONE'),
         '### THE VERIFICATION : %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
         '### THE NO-DISCLOSURE ARM OVER THE FILE LIST: %s' % dict(nd), '### THE FILE LIST:'] + ['    %s' % n for n in names]
    put_txt('b656_mirror.txt', L)
    put_json('b656_mirror.json', dict(at=utc(), zip=ZIP, zip_md5=_hl.md5(zb).hexdigest(), zip_sha256=_hl.sha256(zb).hexdigest(), bytes=len(zb),
                                      manifest_md5=_hl.md5(man).hexdigest(), entries=len(names), files=len(files_), roster_line=rosterl,
                                      root_line=rootl[0] if rootl else '', clean=clean, nd=dict(nd), pp_head=pp_head, last_commit_in_manifest=pp_head in commits))
    for l in L[:8]:
        print(l[:240])


if __name__ == '__main__':
    fn = globals().get(sys.argv[1] if len(sys.argv) > 1 else '')
    if not callable(fn) or sys.argv[1].startswith('_'):
        print('usage: b656_record.py <route> [dry]')
        sys.exit(2)
    fn(*sys.argv[2:])
