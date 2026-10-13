# -*- coding: utf-8 -*-
"""b663_record.py -- THE ACT'S RECORD TOOL, b663 under (R273).

### (R262)(2), standing: ONE conversion of a backtick possessive -- `conv`, with the landing, guard and look-up built on it, is IMPORTED from
### tools/b652_record.py and defined nowhere here. This tool's own screens and guarded landing write their scan files under b663's name.
### (R263)(3), standing: every route here that reads a row of a bank does so through a small reader named in READERS, so the satisfiability
### spec's planted rows can run each reader over one row of each shape before the seal.
### Carried by the Write tool from b662_record.py (the helpers, the guarded landing, the answers route); new here: the record line of
### (R273)(1). The later routes are added to this file by the Edit tool before the seal, each run before the face names it.
### Routes: `python tools/b663_record.py <route> [dry]`; each route banks under data/ and prints what it wrote.
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
import b663_worklist as K          # noqa: E402

STANDIN = bool(os.environ.get('B663_STANDIN'))


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
        'b663_scores.json': dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        'b663_findings.json': dict(entry_line=99999, title='stand-in'),
        'b663_trail.json': dict(line=99999),
        'b663_act_root.json': dict(root='0' * 64, previous='769efd11' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
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


# ================================================================================ THE GUARDED LANDING (b652's, its scan files b663's)
def screens(items, tag, dry):
    import b633_record as R3
    import b641_record as R41
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if dry else D, 'b663_scanfile_%s.md' % tag)
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
def read_head(path, head):
    """a landed head looked up in a ledger through the one conversion; returns its line or raises."""
    ln = line_of(path, head)
    if ln is None:
        raise LookupError('head not found through conv: %s' % head[:60])
    return ln


def read_score_row(k, v):
    """a scores row: key N1..N5, H1..H4 or S1..S3, value [verdict, text]; returns (key, the whole verdict, text) -- the whole verdict, not
    its first word (b656's defect (e))."""
    if not re.match(r'^(N[1-5]|H[1-4]|S[1-3])$', k) or not isinstance(v, list) or len(v) != 2 or not isinstance(v[0], str) or not v[0].strip():
        raise ValueError('score row of another shape: %r' % (k,))
    return k, v[0], v[1]


INSTANCE_KEYS = ('run', 'conclusion', 'sha256', 'sha_ok', 'mem_low', 'build_exit', 'errors', 'rows', 'H1', 'H2', 'landing')


def read_instance(j):
    """the instance bank (data/b663_epstein_instance.json): every key of INSTANCE_KEYS present, rows each with name, axioms, std3, grade;
    returns (H1, H2, the run id, the merge or None); raises on a bank of another shape."""
    miss = [k for k in INSTANCE_KEYS if k not in j]
    if miss or not isinstance(j.get('rows'), list) or not all(isinstance(r, dict) and {'name', 'axioms', 'std3', 'grade'} <= set(r) for r in j['rows']):
        raise KeyError('instance bank without %s' % (miss or 'its rows'))
    return bool(j['H1']), bool(j['H2']), j['run'].get('run_id'), j.get('merged')


def read_control_cell(r):
    """a cell of the computation bank (data/b663_epstein_control.json, rows are cells): name, base, certs a non-empty list of [name,
    CERTIFIED or NOT CERTIFIED, why], a reading `j₀ = <j>` or `NONE ≤ J_max` or `HYP-UNVERIFIED(<name>)`; returns (name, form, j0, the zero
    side's held or None); raises on a row of another shape."""
    if not isinstance(r, dict) or not isinstance(r.get('name'), str) or not isinstance(r.get('base'), list):
        raise ValueError('control cell of another shape')
    cs = r.get('certs')
    if not isinstance(cs, list) or not cs or not all(isinstance(c, list) and len(c) == 3 and c[1] in ('CERTIFIED', 'NOT CERTIFIED') for c in cs):
        raise ValueError('control cell without its certifications')
    rd_ = r.get('reading') or ''
    form = [f for f in ('j₀ = ', 'NONE ≤ J_max', 'HYP-UNVERIFIED(') if rd_.startswith(f)]
    if len(form) != 1:
        raise ValueError('control cell reading of another form: %r' % (rd_,))
    j0 = r.get('j0') if form[0] == 'j₀ = ' else None
    if form[0] == 'j₀ = ' and not isinstance(j0, int):
        raise ValueError('control cell with an index and no j0')
    zs = r.get('zero_side')
    return r['name'], form[0].strip(' =('), j0, (zs.get('held') if isinstance(zs, dict) else None)


READERS = ['read_head', 'read_score_row', 'read_instance', 'read_control_cell']


# ================================================================================ COMPONENT 1: THE RECORD LINE, (R273)(1)
WH = ('*Appended 2026-10-13 by b663 to b662’s entry (:8509), under `(R273)`(1) -- b662 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b662_closing.txt):*')


def _weight():
    return ('\n' + WH + ' the citation check a gate step at step zero, 59 cites, 54 OK, its five misses raised in one prompt before '
            'Component 1, all the navigator’s (relay data/b662_citation_check.txt; data/b662_defects.txt (a)-(d)); the map at J_max = D + 40 '
            '(relay data/b662_detection_map_40.txt) -- every one of the 20 cells with an index, j₀ = 28, 31, 44, 84 at t = 14.1, 29.6, 50, '
            '100, identical across σ at every height, both seats’ sentences banked (relay data/b662_map_readings.txt); W-ORD-E2-SEPARATION '
            'at OPEN_TRAILS :14132; W-ORD-CITATION-CHECK ACTED at :14136; the dated line in the shared bank, its tool re-run reading 8 of 8 '
            'additive (relay data/b662_additive_rerun.txt); SIDE-carrier-spec -- 54 sentence rows, 12 graded OVERREACHES, 9 blocks cut in 4 '
            'files, the "DERIVES." label removed on the cell’s VACUOUS; run 38370416643 with 27 profiles equal to the README’s; merged at '
            'dd54a61, tag v0.4.2; relay 51838723, PLACE-papers 16be102, FINDINGS :8507 and :8509, OPEN_TRAILS :14138, the root 769efd11…; '
            'the suite 79 of 81 with G-MERGES-ON-GATE (the workflow file) and G-AXIOM-CLAIM declared; the mirror '
            'mirror-refresh-2026-10-13-b662.zip (MANIFEST md5 a888b7af…); eight defects, (a)-(d) the navigator’s and (e)-(h) the seat’s, '
            'and the seat’s late one -- the closing push piped through tail -- entered at b663’s step zero (relay data/b663_defects.txt). '
            'Nothing deposited.\n')


def c1(*a):
    land([('FINDINGS.md', WH, _weight())], 'b663_record_lines.json', 'c1', entry=K.B662_ENTRY,
         check=[('FINDINGS.md', K.B662_ENTRY, '## SIDE-carrier-spec'), ('OPEN_TRAILS.md', K.B662_TRAIL, '### b662')],
         dry='dry' in a)


# ================================================================================ THE AUTHOR'S ANSWERS (b662's route, carried)
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
    """data/b663_author_answers.txt: every prompt put by the seat in this act, with its options and the answer; and every word of the author
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
    head = ['### b663 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
            'mark; and %d word(s) of the author delivered between BEGIN and END; the session read: %s from %r (transcript line %d).' % (
                n, K.DATE, nw, K.SESSION_ID[:8], K.ANCHOR, start), '']
    put_txt('b663_author_answers.txt', [l.replace('\r', '') for l in head + (L or ['### NONE: no prompt has been put to the author in this act.']) + W])
    put_json('b663_author_answers.json', dict(at=utc(), calls=[dict(line=i, id=cid, ts=ts, result_ts=(results.get(cid) or (None, None, None))[2])
                                                               for i, cid, _inp, ts in calls]))
    print('  prompts banked: %d ; words banked: %d' % (n, nw))


# ================================================================================ COMPONENT 2: THE DOMINANCE READING BESIDE THE PLAN
def _zeros():
    """the banked list (on the author's word, b326's): the on-line ordinates (gamma_a == gamma_b) and the off-line zeros (rho_a == rho_b),
    each by its index in its bank; a row whose two routes disagree is refused."""
    on = jl(K.ZEROS_ON)['zeros']
    off = jl(K.ZEROS_OFF)['zeros']
    if not all(z['agree'] and z['gamma_a'] == z['gamma_b'] for z in on) or not all(z['agree'] and z['rho_a'] == z['rho_b'] for z in off):
        sys.exit('### A BANKED ZERO WHOSE TWO ROUTES DISAGREE -- NOTHING WRITTEN')
    return [(i, repr(z['gamma_a'])) for i, z in enumerate(on)], [(i, repr(z['rho_a'][0]), repr(z['rho_a'][1])) for i, z in enumerate(off)]


def dominance(*a):
    """(R273)(3) and the author's word on the second question: the configuration's excluded zero and its tie set are read from all seventeen
    off-line zeros. At the base detectorBase ρb (Schema/Detector.lean :40, half-width baseWidth ρb :33) of each off-line zero ρb in turn, the
    score offScore g0 ρ = |paperFT (phiC g0) (gammaOf ρ)| (PowerWindow.lean :328; gammaOf Defs.lean :121) of every off-line zero, in Arb balls
    at 200 bits through tools/b662_map.py's ghat, imported unedited; which zero's score is largest and whether the largest is decided; and at
    the named base (rhoE's) the count of on-line ordinates whose score is not below the largest (the kill set's size, D = 2 · card Xr + 8 by
    coeffs_exist's witness when every off-line orbit but the dominant's lies below M). A reading beside the plan; no hypothesis scored."""
    import b662_map as MP
    from flint import arb, acb, ctx
    ctx.prec = MP.PREC
    on, off = _zeros()
    t0 = time.time()
    L = ['b663 -- COMPONENT 2: THE DOMINANCE READING BESIDE THE PLAN (%s)' % utc(), '',
         '### the zeros: relay data/%s (%d on-line ordinates, by index) and data/%s (%d off-line zeros, by index), banked by two agreeing routes'
         % (K.ZEROS_ON, len(on), K.ZEROS_OFF, len(off)),
         '### in mpmath at 119 digits, NOT BALL-CERTIFIED (the author`s word on the third question); each entered here as its decimal literal, exact.',
         '### rows are bases: the off-line zero ρb whose detectorBase is g0; per row every off-line zero`s score at g0, the largest, and whether',
         '### the largest ball lies wholly above every other (DECIDED) or meets one (TIED). Arb balls at %d bits; tools/b662_map.py`s ghat.' % MP.PREC, '']
    rows = []
    for bi, bs, bt in off:
        sb, tb = arb(bs), arb(bt)
        ell = 1 / (4 * (abs(acb(tb, -(sb - arb(1) / 2))) + 1))
        sc = []
        for i, s, t in off:
            z = acb(arb(t), -(arb(s) - arb(1) / 2))
            sc.append((i, abs(MP.ghat(z, ell, MP.PREC))))
        top = max(sc, key=lambda x: x[1].mid())
        decided = all(top[1].lower() > x[1].upper() for x in sc if x[0] != top[0])
        rows.append(dict(base=bi, base_rho=[bs, bt], ell=MP.b(ell, 8), dominant=top[0], decided=decided,
                         scores=[[i, MP.b(x, 10)] for i, x in sc]))
        L.append('  base off[%2d] = %s + %s i ; ℓ = %s ; the largest score off[%d] (t = %s) %s %s' % (
            bi, bs[:10], bt[:10], MP.b(ell, 8), top[0], off[top[0]][2][:10], MP.b(top[1], 10), 'DECIDED' if decided else 'TIED'))
        L.append('      scores: ' + ' ; '.join('[%d] %s' % (i, x.str(6, radius=False)) for i, x in sc))
    named = [r for r in rows if r['base_rho'] == list(K.RHO_E)]
    L += ['']
    if len(named) != 1:
        L.append('### rhoE (Schema/Epstein.lean :32) IS NOT ONE OF THE BANKED OFF-LINE ZEROS AS WRITTEN -- printed, not repaired')
    else:
        r = named[0]
        bi = r['base']
        sb, tb = arb(K.RHO_E[0]), arb(K.RHO_E[1])
        ell = 1 / (4 * (abs(acb(tb, -(sb - arb(1) / 2))) + 1))
        dz = off[r['dominant']]
        M = abs(MP.ghat(acb(arb(dz[2]), -(arb(dz[1]) - arb(1) / 2)), ell, MP.PREC))
        kill, strad = [], []
        for i, gm in on:
            g_ = abs(MP.ghat(acb(arb(gm)), ell, MP.PREC))
            if g_.lower() >= M.upper():
                kill.append(i)
            elif not g_.upper() < M.lower():
                strad.append(i)
        L += ['### AT THE NAMED BASE, rhoE = off[%d] (Schema/Epstein.lean :32): the dominant off[%d] (t = %s), M = %s; on-line ordinates with score '
              'not below M: %d (indices %s)%s; card Xr = %d distinct |γ| would give D = 2 · card Xr + 8 = %d, J_max = D + 40 = %d.' % (
                  bi, r['dominant'], dz[2][:10], MP.b(M, 10), len(kill), kill[:40], (' ; STRADDLING M: %s' % strad) if strad else ' ; none straddling',
                  len(kill), 2 * len(kill) + 8, 2 * len(kill) + 48)]
    self_dom = [r['base'] for r in rows if r['dominant'] == r['base'] and r['decided']]
    L += ['### the bases at which the base`s own zero is the decided dominant: %s' % (self_dom or 'NONE'), '']
    # ### the two candidate bases: the kill set, θ over the listed points, and the heights above which each decay bound clears θ·M
    lo4, hi4 = MP.i4_ball()
    i4 = MP.span(lo4, hi4)
    L += ['### THE TWO CANDIDATE BASES (off[0], the self-dominant; rhoE = off[1], the kernel`s named zero): at each, M = the dominant`s score;',
          '### the kill set = listed points scoring ≥ M (decided in balls); θ = the largest score/M over the listed points outside the tie set',
          '### (the dominant`s orbit) and the kill set; then the height H above which an UNLISTED strip point is cleared, offScore ≤ θ·M:',
          '###   first order  -- |paperFT g0 z| ≤ (1/|z|) ∫|g0`| e^{|Im z| |u|} du ≤ 2 e^{ℓ/2}/|z| (g0 monotone on each side of 0, total',
          '###                   variation 2, support [-ℓ, ℓ], |Im z| ≤ 1/2): H1 = 2 e^{ℓ/2}/(θ M); integration by parts, NOT A KERNEL LEMMA;',
          '###   fourth order -- zero_weight`s hsA (PowerLimit.lean :825), offScore ≤ Aw/(1 + |γ|⁴), Aw (:800) as tools/b662_map.py :216:',
          '###                   H4 = (Aw/(θ M) - 1)^{1/4}; A KERNEL LEMMA. I4 = %s.' % MP.b(i4, 15)]
    cand = {}
    for bi in (0, 1):
        _bi, bs, bt = off[bi]
        sb, tb = arb(bs), arb(bt)
        ell = 1 / (4 * (abs(acb(tb, -(sb - arb(1) / 2))) + 1))
        dz = off[[r for r in rows if r['base'] == bi][0]['dominant']]
        M = abs(MP.ghat(acb(arb(dz[2]), -(arb(dz[1]) - arb(1) / 2)), ell, MP.PREC))
        kill, strad, th, targ = [], [], arb(0), None
        for i, gm in on:
            g_ = abs(MP.ghat(acb(arb(gm)), ell, MP.PREC))
            if g_.lower() >= M.upper():
                kill.append(i)
            elif g_.upper() < M.lower():
                r_ = arb((g_.upper() / M.lower()).upper())
                if r_.upper() > th.upper():
                    th, targ = r_, 'on[%d] γ = %s' % (i, gm[:10])
            else:
                strad.append(i)
        for i, s, t in off:
            if (s, t) == (dz[1], dz[2]):
                continue
            g_ = abs(MP.ghat(acb(arb(t), -(arb(s) - arb(1) / 2)), ell, MP.PREC))
            if g_.lower() >= M.upper():
                kill.append('off%d' % i)
            elif g_.upper() < M.lower():
                r_ = arb((g_.upper() / M.lower()).upper())
                if r_.upper() > th.upper():
                    th, targ = r_, 'off[%d] t = %s' % (i, t[:10])
            else:
                strad.append('off%d' % i)
        aw = (arb(3) / 2 * ell + 16 * i4 / ell ** 3) * (ell / 2).exp()
        h1 = 2 * (ell / 2).exp() / (th * M)
        h4 = ((aw / (th * M) - 1).log() / 4).exp()
        cand[bi] = dict(ell=MP.b(ell, 10), M=MP.b(M, 12), kill=kill, straddle=strad, theta=MP.b(th, 12), theta_at=targ, D=2 * len(kill) + 8,
                        H1=MP.b(h1, 8), H4=MP.b(h4, 8), Aw=MP.b(aw, 8))
        L.append('  base off[%d] (%s + %s i): ℓ = %s ; dominant off[%d], M = %s ; kill set %d (%s)%s ; θ = %s at %s ; D = %d, J_max = %d ; '
                 'H1 = %s ; Aw = %s, H4 = %s ; the banked list ends at T = 150' % (
                     bi, bs[:10], bt[:10], MP.b(ell, 8), dz[0], MP.b(M, 10), len(kill), kill, (' ; STRADDLING %s' % strad) if strad else '',
                     MP.b(th, 10), targ, 2 * len(kill) + 8, 2 * len(kill) + 48, MP.b(h1, 8), MP.b(aw, 6), MP.b(h4, 8)))
    L += ['### elapsed %d s' % int(time.time() - t0)]
    put_txt('b663_dominance.txt', L)
    put_json('b663_dominance.json', dict(at=utc(), rows=rows, self_dominant=self_dom, candidates=cand))
    print(NL.join(L[-4:]))


CERT_H = ('### `W-ORD-EPSTEIN-CERTIFY` -- THE Q0 ZERO LIST IN BALLS, PRICED, NOT STARTED, appended 2026-10-13, b663, on the author’s word '
          'to b663’s citation prompt')


def _certify():
    return ('\n' + CERT_H + '\n\n**Items.** The seventeen off-line zeros of Z_Q (Q = x² + xy + 6y², discriminant −23) below T = 150 (relay '
            'data/b326_offline.json, key "zeros", index 0-16) and the 146 on-line ordinates (data/b326_epstein_zeros.json, index 0-145) '
            'isolated in Arb balls at 200 bits by an argument-principle count, so the configuration’s points carry balls; with them the band '
            '|t| < 0.5 and σ in (1/2, 0.52), which neither census of b326 reads. Today the zeros are banked by two agreeing routes in mpmath at '
            '119 digits with winding counts, registered_gate_passed = False: banked, not ball-certified (relay data/b663_defects.txt (c)). '
            '**Price:** one act, b642’s R5 price for a witnessed certificate (relay data/b642_epstein_rungs.txt :182), a compiled one '
            'unpriced. **Trigger:** H4 of b663 held -- a control that fires on banked data earns the certification that makes it stand. '
            '**Entered** beside b663’s plan (relay data/b663_epstein_plan.txt).\n')


def c2(*a):
    land([('OPEN_TRAILS.md', CERT_H, _certify())], 'b663_record_lines_c2.json', 'c2', entry=K.EPSTEIN_LINE,
         check=[('OPEN_TRAILS.md', K.EPSTEIN_LINE, 'W-ORD-EPSTEIN-ZQ'), ('OPEN_TRAILS.md', K.RUNGS_LINE, 'W-ORD-EPSTEIN-ZQ')],
         dry='dry' in a)


FT_H = ('### `W-ORD-FT-FIRST-ORDER` -- THE FIRST-ORDER TRANSFORM BOUND AS A KERNEL LEMMA, PRICED, NOT STARTED, appended 2026-10-13, b663, '
        'on the author’s word to b663’s plan prompt')


def _ft():
    return ('\n' + FT_H + '\n\n**Items.** For the plateau base g0 = plateau (1/2) ℓ (SIDE-explicit-formula TwoPropertyWindow.lean :56-:69) '
            'and z ≠ 0: ‖paperFT (phiC g0) z‖ ≤ 2 e^{ℓ |Im z|} / ‖z‖, by one integration by parts (the boundary terms 0 at ±ℓ; ∫ |g0′| = 2). '
            'It is b663’s B1 (relay data/b663_epstein_plan.txt, section 8), used there as a named READ premise of the computation to certify '
            'hθ at Z_Q’s points above T = 150, where the kernel’s fourth-order bound (zero_weight’s hsA, PowerLimit.lean :825) clears only '
            'above a height near 629. **Price:** one lemma, one integration by parts, built and printed on the runner; one act, or inside '
            'another. **Trigger:** b663’s use of B1. **Acted:** at the next research slot or inside W-ORD-E2-SEPARATION’s act, on the '
            'author’s word.\n')


def c2b(*a):
    land([('OPEN_TRAILS.md', FT_H, _ft())], 'b663_record_lines_c2b.json', 'c2b', entry=K.EPSTEIN_LINE,
         check=[('OPEN_TRAILS.md', 14158, 'W-ORD-EPSTEIN-CERTIFY')], dry='dry' in a)


def a0list(*a):
    """the author's word on Q1: A₀Q = 10 printed with its source line or its reason. The banked list's own step maximum -- HCount's ratio
    N(s, s+1] / log(|s| + 3) read over the 360 listed points by tools/b662_map.py's a0_upper, imported unedited (every listed ordinate as a
    ball of radius 0: the points are the configuration's literals) -- banked as data/b663_a0_list.txt, the reason for A₀Q printed beside."""
    import b662_map as MP
    from flint import arb, ctx
    ctx.prec = MP.PREC
    on, off = _zeros()
    ords = [x for _i, gm in on for x in (arb(gm), -arb(gm))] + [x for _i, _s, t in off for x in (arb(t), arb(t), -arb(t), -arb(t))]
    a0, sarg, cnt = MP.a0_upper(ords)
    L = ['b663 -- THE BANKED LIST`S OWN LOCAL COUNT, BESIDE P3`s A₀Q (%s)' % utc(), '',
         '### HCount (RestBound.lean :44-:45): 1 ≤ A₀ and N(s, s+1] ≤ A₀ log(|s| + 3) for every real s, N counting Im in (s, s+1] with',
         '### multiplicity (Defs.lean :162). Over the 360 listed points (%d ordinates with sign and multiplicity) by tools/b662_map.py`s a0_upper:' % len(ords),
         ('  the listed points` own A₀ = %s (the largest ratio at s = %s, count %d there)' % (a0.str(15, radius=False), MP.b(sarg, 10), cnt))
         if sarg is not None else
         '  the listed points` own A₀ = %s: NO STEP`S RATIO N(s, s+1] / log(|s| + 3) EXCEEDS 1, so HCount`s clause 1 ≤ A₀ sets it' % a0.str(15, radius=False),
         '',
         '### A₀Q = 10 HAS NO SOURCE LINE; ITS REASON: P3 states HCount for Z_Q`s whole configuration, above T = 150 too, where no bank lists',
         '### a zero. 10 is the plan`s round constant above the listed points` own value printed here, a margin for the unlisted zeros above 150',
         '### (whose count in (s, s+1] grows like (1/π) log s), stated, not proved; open. In hrate A₀ enters once, linearly, inside 3 A₀ Bf',
         '### (RateIndexCfg.lean :146), so its size moves j₀ by at most the index where θ^(2^(j+1) - 2^(D+1)) absorbs a factor of 10.']
    put_txt('b663_a0_list.txt', L)
    print(NL.join(L[4:5]))


# ================================================================================ COMPONENT 3: THE RUNNER, READ BY ITS RUN ID
STD3 = {'propext', 'Classical.choice', 'Quot.sound'}
PRINT_RE = re.compile(r"^'(.+?)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])", re.M)
ERR_RE = re.compile(r'^(?:error: )?(\S+\.lean):(\d+):(\d+): error: (.*)$', re.M)
RUN = dict(run_id=38413488503, ref='c7d28584d0976625f63014f1e9b2e21a2a0c6c76', dispatched_at='main', target='SIDEExplicitFormula.Schema.EpsteinQ0',
           file='SIDEExplicitFormula/Schema/EpsteinQ0.lean')
PREMISES = ('Q0Listed', 'Q0Complete', 'Q0Count', 'EpsteinPremises')


def _gh(*a):
    r = subprocess.run(['gh'] + list(a), capture_output=True)
    return r.returncode, r.stdout, r.stderr.decode('utf-8', 'replace')


def runner(*a):
    """the run read by its id; the artifact listed, downloaded by its id into memory, its sha256 against the platform's digest BEFORE any
    reading; the build's exit and error lines, the memory log's low and any STOP; every print of print_targets.txt read at the standard
    three or none, no sorryAx; every declaration of the new file graded by the shared E0 rule (tools/e0_rule.py) from its statement at the
    branch tip, the premises listed by name beside the print (the author's word on the INTERFACES miss); H1 and H2 scored by printed line;
    the landing point of (R273)(5). Banked as data/b663_epstein_instance.txt and .json."""
    import hashlib
    import zipfile
    import b569_record as R9
    import e0_rule as E0
    repo = 'psinary-sketch/' + K.KERNEL
    rc, out, err = _gh('run', 'view', str(RUN['run_id']), '-R', repo, '--json', 'status,conclusion,headSha,headBranch,createdAt,updatedAt,url')
    run = json.loads(out or b'{}')
    rc, out, err = _gh('api', 'repos/%s/actions/runs/%d/artifacts' % (repo, RUN['run_id']))
    arts = (json.loads(out or b'{}').get('artifacts') or [])
    art = arts[0] if arts else {}
    pt = [l.strip() for l in (_show(K.KD, RUN['ref'], 'print_targets.txt') or '').split(NL) if l.strip()]
    src = _show(K.KD, RUN['ref'], RUN['file']) or ''
    L = ['b663 -- COMPONENT 3, (R273)(2), (5): THE Q0 INSTANCE ON THE HOSTED RUNNER, READ BY ITS RUN ID (%s)' % utc(), '',
         '### the branch %s at %s (pushed by name before the dispatch); the file %s, sha256 %s, %d bytes; print_targets.txt at the ref: %d names' % (
             K.BRANCH, RUN['ref'][:7], RUN['file'], hashlib.sha256(src.encode('utf-8')).hexdigest(), len(src.encode('utf-8')), len(pt)),
         '### the one dispatch: at %s (the workflow on main since b654), the ref input %s (the branch`s tip) ; target %s' % (
             RUN['dispatched_at'], RUN['ref'], RUN['target']),
         '### the run: id %s ; %s ; status %s ; conclusion %s ; head %s on %s ; %s to %s' % (
             RUN['run_id'], run.get('url'), run.get('status'), run.get('conclusion'), run.get('headSha'), run.get('headBranch'), run.get('createdAt'),
             run.get('updatedAt'))]
    T_, sha_ok, sha = {}, False, None
    if art:
        rz = subprocess.run(['gh', 'api', 'repos/%s/actions/artifacts/%d/zip' % (repo, art['id'])], capture_output=True)
        sha = hashlib.sha256(rz.stdout).hexdigest()
        digest = (art.get('digest') or '').replace('sha256:', '')
        sha_ok = bool(digest) and digest == sha
        L.append('### the artifact: id %s ; name %s ; %s bytes ; sha256 %s ; the platform`s digest %s ; %s' % (
            art['id'], art.get('name'), art.get('size_in_bytes'), sha, digest or '### NONE GIVEN',
            'AGREE' if sha_ok else ('### DIFFER' if digest else 'no digest to compare -- NOTHING READ FROM IT')))
        if sha_ok:
            with zipfile.ZipFile(io.BytesIO(rz.stdout)) as z:
                for n in z.namelist():
                    T_[n] = z.read(n).decode('utf-8', 'replace').replace(chr(13), '')
    else:
        L.append('### the artifact: ### NONE LISTED')
    mem = T_.get('mem.log', '')
    low = re.findall(r'^LOW (\d+)', mem, re.M)
    mem_low = int(low[-1]) if low else None
    stops = [l for l in mem.split(NL) if l.startswith('STOP ')]
    blog = T_.get('build.log', '')
    bexit = T_.get('build_exit.txt', '').strip()
    errs = [(m.group(1), int(m.group(2)), int(m.group(3)), m.group(4)) for m in ERR_RE.finditer(blog)]
    axt = T_.get('axioms.txt', '')
    P = dict((k_, sorted(v_)) for k_, v_ in R9.prints_axioms(axt).items())          # ### Lean's wrapped lines read (b569's reader)
    axerr = [l for l in axt.split(NL) if ': error' in l]
    L += ['### the ref built (out/ref.txt): %s' % ' '.join(T_.get('ref.txt', '### UNREAD').split()),
          '### the memory log: samples %d ; LOW %s MB ; the hold %d ; STOP lines %s' % (
              len([l for l in mem.split(NL) if 'avail_mb=' in l]), mem_low, K.HOLD, stops or 'NONE'),
          '### the build: exit %s ; error lines %d ; the log`s last lines:' % (bexit or '### UNREAD', len(errs))] + \
        ['    ' + l for l in blog.rstrip(NL).split(NL)[-6:]] + ['    %s:%d:%d: %s' % e for e in errs[:30]] + [
          '### the print step: error lines %d%s ; names refused %s' % (len(axerr), (' -- ' + ' | '.join(axerr[:4])) if axerr else '',
                                                                       T_.get('axioms_refused.txt', '').strip() or 'NONE'), '',
          ] + E0.RULE_TEXT + ['### MET at this read carries Q0Premises: %s (entered by ruling at b663, the author`s word on Component 3; the test '
                               'tools/test_e0_rule.py case (56) before and after: relay data/b663_tests_met_before.txt, data/b663_tests_met_after.txt)'
                               % ('Q0Premises' in E0.MET),
                               '', '### THE GATE READING PER TERMINAL: the run`s print ; the E0 grade from the statement at the tip (declarations of '
                               '%s; the others b590`s and the schema`s, printed for the reading):' % RUN['file']]
    rows, unread = [], []
    for n in pt:
        ax = P.get(n)
        short = n.split('.')[-1]
        m = re.search(r'^(theorem|def|structure|abbrev)\s+%s(?![\w\'])' % re.escape(short), src, re.M)
        kind = m.group(1) if m else None
        gr, why = ('-', 'not in the new file')
        if kind == 'theorem':
            head, _ln = R9.header_of(src, short)
            gr, why, _b = E0.grade(head or '', 'theorem')
        elif kind is not None:
            gr, why = 'DEF', ''
        std = ax is not None and set(ax) <= STD3 and 'sorryAx' not in ax
        prem = [p for p in PREMISES if re.search(r'\b%s\b' % p, why or '')]
        rows.append(dict(name=n, axioms=ax, std3=std, grade=gr, why=why, premises=prem, in_file=kind is not None))
        if ax is None:
            unread.append(n)
        L.append('  %-58s %-32s %-11s %s%s' % (n.replace('SIDEExplicitFormula.', ''), ax if ax is not None else '### NOT PRINTED',
                                               gr, ('premises by name: ' + ', '.join(prem)) if prem else '', ('' if not why or gr in ('DEF', '-') else ' -- ' + why[:110])))
    infile = [r for r in rows if r['in_file']]
    sorry_src = len(re.findall(r'\bsorry\b', src))
    h1 = (run.get('conclusion') == 'success' and sha_ok and bexit == '0' and not errs and not stops and mem_low is not None and mem_low >= K.HOLD
          and not unread and not axerr and all(r['std3'] for r in rows) and sorry_src == 0
          and all(r['grade'] in ('INTERFACES', 'DERIVES', 'DEF') for r in infile))
    h2r = [r for r in rows if r['name'].endswith('.q0_h2_iff_target')]
    h2_line = re.search(r'theorem q0_h2_iff_target[\s\S]*?:=\s*\n?\s*(h2_sign_cfg_iff_target \(q0Config Z rhs hP\))', src)
    h2 = bool(run.get('conclusion') == 'success' and sha_ok and bexit == '0' and not errs and h2r and h2r[0]['std3'] and h2_line)
    warns = [l.strip() for l in blog.split(NL) if 'warning' in l and 'EpsteinQ0' in l]
    n_int = sum(1 for r in infile if r['grade'] == 'INTERFACES')
    n_der = sum(1 for r in infile if r['grade'] == 'DERIVES')
    compiled = run.get('conclusion') == 'success' and sha_ok and bexit == '0' and not errs and not stops
    unl0 = [r for r in infile if r['grade'] == 'PREDICATE-UNLISTED']
    land_pt = ('THE INSTANCE COMPILED ON THE RUNNER, EVERY PREMISE A PROP THE SCHEMA ACCEPTS: to merge alone on this gate reading (Component 5)'
               if h1 else
               ('THE INSTANCE COMPILED ON THE RUNNER, EVERY PREMISE A PROP THE SCHEMA ACCEPTS (it is consumed by epsteinConfig, the detector and '
                'the rate theorem at the standard three); THE E0 GRADE OF ITS %d PREMISE-CARRYING THEOREMS IS PREDICATE-UNLISTED, NOT INTERFACES '
                '-- neither landing point of (R273)(5) as written; the branch unmerged pending the author`s word' % len(unl0))
               if compiled and unl0 else
               'THE INSTANCE NOT COMPILED AS WRITTEN: the branch stays unmerged, its tip banked; the obstruction by file and line above')
    unl = [r['name'].split('.')[-1] for r in infile if r['grade'] == 'PREDICATE-UNLISTED']
    L += ['', '  sorry in the new file: %d' % sorry_src,
          '  the build`s warning lines on the new file: %d%s' % (len(warns), ''.join(NL + '    ' + w[:200] for w in warns[:12])),
          '  PREDICATE-UNLISTED (the E0 rule, (R243)(2): a predicate met for the first time is printed, not graded INTERFACES; MET, '
          'tools/e0_rule.py :308-:315): %d -- %s' % (len(unl), ', '.join(unl) or 'NONE'),
          '', '### ### **RUN %s ; CONCLUSION %s ; ARTIFACT SHA256 %s %s ; MEMORY LOW %s MB (HOLD %d) ; BUILD EXIT %s ; ERROR LINES %d ; TERMINALS %d, '
          'PRINTED %d, AT THE STANDARD THREE OR NONE %d ; THE NEW FILE`S DECLARATIONS %d: INTERFACES %d, DERIVES %d, DEF %d.**' % (
              RUN['run_id'], run.get('conclusion'), (sha or '### NONE')[:16], 'AGREE' if sha_ok else '### NOT AGREED', mem_low, K.HOLD,
              bexit or '### UNREAD', len(errs), len(pt), len(pt) - len(unread), sum(1 for r in rows if r['std3']), len(infile), n_int, n_der,
              sum(1 for r in infile if r['grade'] == 'DEF')),
          '  H1 %s -- the instance %s on the runner (run %s); every premise (%s) INTERFACES by the E0 rule beside a print at the standard three; '
          'every other declaration at the standard three or none%s' % ('HELD' if h1 else 'REFUTED', 'compiled' if bexit == '0' else 'NOT compiled',
                                                                         RUN['run_id'], ', '.join(PREMISES),
                                                                         '' if h1 else ' -- REFUTED IN ONE CLAUSE: compiled, every print at the standard '
                                                                         'three, but the premise-carrying theorems grade PREDICATE-UNLISTED (hP : '
                                                                         'Q0Premises Z rhs, Q0Premises not in MET), not INTERFACES'),
          '  H2 %s -- q0_h2_iff_target := h2_sign_cfg_iff_target (q0Config Z rhs hP), one application, printed %s' % (
              'HELD' if h2 else 'REFUTED', h2r[0]['axioms'] if h2r else '### NOT PRINTED'),
          '', '### THE LANDING POINT, (R273)(5): %s.' % land_pt]
    put_txt('b663_epstein_instance.txt', L)
    put_json('b663_epstein_instance.json', dict(at=utc(), run=RUN, conclusion=run.get('conclusion'), sha256=sha, sha_ok=sha_ok, mem_low=mem_low,
                                                build_exit=bexit, errors=[list(e) for e in errs], rows=rows, H1=h1, H2=h2, landing=land_pt))
    print(L[-5])
    print(L[-4])
    print(L[-3])
    for e in errs[:12]:
        print('  ERROR %s:%d:%d: %s' % e)


def mapdiff(*a):
    """Component 4: tools/b662_map.py against tools/b663_epstein_map.py, a unified diff by difflib, banked as data/b663_map_diff.txt with
    its hunk count and the b662 line ranges each hunk touches, read against the plan's section 6 list."""
    import difflib
    old = rd(os.path.join(T, K.MAP_FROM)).split(NL)
    new = rd(os.path.join(T, K.MAP_TO)).split(NL)
    d = list(difflib.unified_diff(old, new, 'tools/' + K.MAP_FROM, 'tools/' + K.MAP_TO, lineterm='', n=0))
    hunks = [l for l in d if l.startswith('@@')]
    L = ['b663 -- COMPONENT 4: tools/%s CARRIED INTO tools/%s, THE DIFF (%s)' % (K.MAP_FROM, K.MAP_TO, utc()), '',
         '### the plan`s section 6 (relay data/b663_epstein_plan.txt) names the lines the author let change: the configuration (zero_list ->',
         '### q0_list beside it; the cell), M and hdom (:197-:210), θ and the kill set (:219-:236), hA (:241), the zero side (:351-:388); ghat,',
         '### ramp_R, i4_ball, a0_upper, the controls of hQtie and hQb, hrate and the rung unchanged. Hunks: %d ; lines removed %d ; added %d.' % (
             len(hunks), sum(1 for l in d if l.startswith('-') and not l.startswith('---')), sum(1 for l in d if l.startswith('+') and not l.startswith('+++'))),
         '### the hunks` b662 ranges: ' + ' '.join(h.split(' ')[1] for h in hunks), ''] + d
    put_txt('b663_map_diff.txt', L)
    print('  hunks %d' % len(hunks))


def merged(*a):
    """`merged <merge sha> <tag>`: the instance row's merge and tag, after main and the tag are read back at the remote by push_gated.sh
    (relay data/b663_merge_push_out.txt)."""
    sha, tag = a[:2]
    j = jl('b663_epstein_instance.json')
    pk = g(K.KD, 'rev-parse', '%s^{commit}' % tag).strip()
    j.update(merged=sha, tag=tag, tag_peeled=pk, merge_tree_equals_built=g(K.KD, 'rev-parse', sha + '^{tree}').strip() == g(K.KD, 'rev-parse', RUN['ref'] + '^{tree}').strip())
    put_json('b663_epstein_instance.json', j)
    print('  merged %s ; tag %s peeled %s ; the merged tree equals the built tree: %s' % (sha, tag, pk[:7], j['merge_tree_equals_built']))


# ================================================================================ THE LATE ROUTES (b662's, carried; every row read through READERS)
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
    L = ['b663 -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING AND THE LOCAL LEAN READING (N1) (%s)' % utc(), '',
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
    put_txt('b663_commands.txt', [l.replace('\r', '') for l in L])
    put_json('b663_commands.json', dict(at=utc(), anchor=K.ANCHOR, rows=rows, offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                        local_lean=[r['n'] for r in lean]))
    print(L[-1])


def kernels(*a):
    import b641_record as R41
    put_json('b663_kernels_face.json', dict(at=utc(), kernels=R3.kern_state(list(R41.KERNS_READ))))
    print('  kernels read: %d' % len(R41.KERNS_READ))


def _defect_short():
    out = []
    for l in rdn('b663_defects.txt').split(NL):
        m = re.match(r'^    \(([a-z]|b662-late)\) ([^.]*)\.', l)
        if m:
            out.append(m.group(0).strip()[:-1])
    return out


def defects(*a):
    t = rdn('b663_defects.txt')
    ds = [l.strip() for l in t.split(NL) if re.match(r'^    \(([a-z]|b662-late)\) ', l)]
    put_json('b663_defects.json', dict(at=utc(), defects=ds, short=_defect_short()))
    print('  defects %d' % len(ds))


def seal_hashes():
    import hashlib
    rec_ = jl('b663_seal_hashes.json').get('tools') or {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


ROOT_EXCLUDE = re.compile(r'^b663_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|commands)\.(txt|json|md)$')


def root_banks():
    return sorted('data/' + f for f in os.listdir(D) if f.startswith('b663_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f))


def root(*a):
    banks = root_banks()
    crlf = [b for b in banks if b'\r\n' in open(os.path.join(ROOT, *b.split('/')), 'rb').read()]
    print('  banks named: %d ; the seal bank among them %s ; written with CR LF: %s' % (len(banks), 'data/b663_seal_hashes.json' in banks, crlf or 'none'))
    if crlf:
        sys.exit('### A BANK THE ROOT WOULD NAME IS CR LF -- NOTHING WRITTEN')
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b663'] + banks + ([] if 'dry' in a else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    import tempfile
    import act_root as AR
    J = jl('b663_act_root.json')
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/')][0]
    with tempfile.TemporaryDirectory(prefix='b663_ra_') as tmp:
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
    L = ['b663 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; its recorded commit %s ; banks named %d ; changed or written after the root: %s' % (
             J.get('at'), (J.get('commit') or {}).get('relay', '?')[:12], len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b663_root_arm.txt', L)
    put_json('b663_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
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
    L = ['b663 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d ; against relay HEAD %s' % (utc(), r.returncode, g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved))]
    L += ['    added   %s / %s' % k for k in added[:60]] + ['    gone    %s / %s' % k for k in gone[:60]] + [
        '    moved   %s / %s : %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved[:60]]
    L += ['### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b663_table_final.txt', L)
    put_json('b663_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


NK = ('N1', 'N2', 'N3', 'N4', 'N5')
HK = ('H1', 'H2', 'H3', 'H4')
SK = ('S1', 'S2', 'S3')
SCORE_KEYS = NK + HK + SK
N5_RELAY_DATA = ('act_roots.txt', 'b662_closing_push_out.txt')
N5_RELAY_TOOLS = ('e0_rule.py', 'test_e0_rule.py')          # ### the one tool edit of the act, by ruling (the author's word on Component 3)
N5_PP = ('FINDINGS.md', 'OPEN_TRAILS.md')
N5_KFILES = ['SIDEExplicitFormula/Schema/EpsteinQ0.lean', 'print_targets.txt']
FACE = os.path.join(D, 'b663_registration_2026-10-13.txt')
OPEN_DOC = 'stated, not proved; open'


def TRAIL_HEAD():
    return ('### b663 — lane two, act ninety, the research act under (R273): b662 at its weight; the Epstein rungs read and the plan raised; '
            'the Q0 configuration built on premises; the detector and the rate index at the real configuration')


def _iso(s):
    import calendar
    try:
        return calendar.timegm(time.strptime((s or '')[:19], '%Y-%m-%dT%H:%M:%S'))
    except Exception:
        return None


def _calls():
    return jl('b663_author_answers.json').get('calls') or []


def _main_src():
    return _show(K.KD, 'main', K.EPSTEIN_FILE) or ''


def _premise_docs(src):
    """each premise of the new file with its docstring: (name, is a Prop, carries the open docstring)."""
    out = []
    for nm in ('Q0Listed', 'Q0Complete', 'Q0Count', 'Q0Premises'):
        m = re.search(r'/--((?:(?!-/)[\s\S])*)-/\s*\n(def|structure) %s\b[^\n]*' % nm, src)
        out.append((nm, bool(m) and (': Prop' in m.group(0).split('\n')[-1]), bool(m) and OPEN_DOC in m.group(1)))
    return out


def _n2():
    src = _main_src()
    pd = _premise_docs(src)
    sorry_main = len(re.findall(r'\bsorry\b', src))
    sorry_br = len(re.findall(r'\bsorry\b', _show(K.KD, K.BRANCH, K.EPSTEIN_FILE) or ''))
    ok = bool(src) and all(p and d for _n, p, d in pd) and sorry_main == 0 and sorry_br == 0
    return ('HELD' if ok else 'REFUTED'), (
        'the premises this act states, at SIDE-explicit-formula main (%s): %s; P4 b590`s EpsteinPremises carried by name inside Q0Premises (its '
        'own docstring b590`s, "cited, not compiled", the file untouched on the author`s word); sorry in the file at main %d, at the branch %d' % (
            K.EPSTEIN_FILE, ' ; '.join('%s Prop %s, open docstring %s' % x for x in pd), sorry_main, sorry_br))


def _n3():
    j = jl('b663_epstein_instance.json')
    rows = [r for r in j.get('rows') or [] if r.get('name', '').split('.')[-1].startswith('q0_')]
    beyond = [r['name'] for r in j.get('rows') or [] if not r.get('std3')]
    unl = [r['name'] for r in rows if r.get('grade') != 'INTERFACES']
    ok = bool(rows) and not beyond and not unl
    return ('HELD ON THE RE-GRADE' if ok else 'REFUTED'), (
        'the gate reading (relay data/b663_epstein_instance.txt): every terminal at the standard three or none, beyond it %s; the premise-carrying '
        'theorems %d, INTERFACES on Q0Premises %d -- on the re-grade after Q0Premises entered MET by ruling (the first reading printed them '
        'PREDICATE-UNLISTED, (R243)(2))' % (beyond or 'NONE', len(rows), len(rows) - len(unl)))


def _ctl():
    return [read_control_cell(r) for r in jl('b663_epstein_control.json').get('cells') or []]


def _n4():
    cs = _ctl()
    q = [c for c in cs if c[0].startswith('Q0')]
    z = [c for c in cs if c[0].startswith('THE CONTROL')]
    cells = jl('b663_epstein_control.json').get('cells') or []
    qcert = [x for x in (cells[-1].get('certs') if cells else []) if x[1] == 'CERTIFIED']
    ok = bool(q) and q[0][1] == 'j₀' and q[0][2] is not None and bool(z) and z[0][2] == 31
    return ('HELD ON B1' if ok else 'REFUTED'), (
        'the computation (relay data/b663_epstein_control.txt): Q0 at qE0 reads j₀ = %s, every hypothesis certified by name (%s), hθ above 150 on '
        'B1 (READ); the control Z₁(0.8, 29.6) j₀ = %s' % (q[0][2] if q else '?', ', '.join(x[0] for x in qcert), z[0][2] if z else '?'))


def _n5():
    face = jl('b663_kernels_face.json').get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    others_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in N5_PP]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b663_|audit_b663_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('data/') and x[5:] in N5_RELAY_DATA)
                                                or (x.startswith('tools/') and x[6:] in N5_RELAY_TOOLS))]
    km = [l for l in g(K.KD, 'log', '--first-parent', '--format=%h %p', K.K_MAIN + '..main').split(NL) if l.strip()]
    km_ok = len(km) == 1 and len(km[0].split()) == 3
    k_files = sorted(x for x in g(K.KD, 'diff', '--name-only', K.K_MAIN, 'main').split(NL) if x.strip())
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    import b663_checks as CH
    new_arms = sorted(set(a[0] for a in CH.ARMS) - set(CH.STANDING) - set(K.ACT_ARMS))
    zeta = [l for l in rdn('b663_epstein_control.txt').split(NL) + _main_src().split(NL) if re.search(r'\bζ\b|zeta\b', l) and 'not about' not in l
            and 'Nothing here is about' not in l and 'zeta3Sum' not in l and 'zeta_zeros' not in l and 'zeta_nzeros' not in l and 'zeta()' not in l
            and "nothing of ζ" not in l and "is not ζ" not in l and 'and nothing here is about' not in l]
    ok = others_ok and not pp_beyond and not kinds_beyond and not differ and km_ok and not new_arms and k_files == sorted(N5_KFILES)
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unsubmitted); %s`s main written by the one merge under Component 5 alone '
            '(first-parent commits since %s: %s ; %s), its files against %s: %s; every kernel as the face read it %s; standing arms added: %s (the '
            'act`s arms over its own banks %d); sealed tools not agreeing %s; PLACE-papers beyond FINDINGS and OPEN_TRAILS: %s; relay files of a '
            'kind beyond the banks, the tools, the root list, b662`s push-out bank and the one tool edit of the act by ruling (tools/e0_rule.py`s '
            'MET line with its test): %s; lines of the act`s computation bank and file naming ζ beyond saying they are not about it: %d; no '
            'identifier of the author in any outbound request (git pushes, remote reads, the runner`s dispatch with a ref and a target, the '
            'artifact`s download)' % (
                K.DRAFT, K.KERNEL, K.K_MAIN, [l.split()[0] for l in km], 'AS RULED' if km_ok else '### OTHERWISE', K.K_MAIN, k_files, others_ok,
                new_arms or 'NONE', len(K.ACT_ARMS), differ or 'NONE', pp_beyond or 'NONE', kinds_beyond or 'NONE', len(zeta)))


def _h_from(bank, h):
    m = re.search(r'^  %s (.*)$' % h, rdn(bank), re.M)
    line = m.group(1) if m else ''
    w = line.split(' -- ')[0].strip() or '### UNREAD'
    return w, 'relay data/%s: %s %s' % (bank, h, line[:400])


def scores(*a):
    TF, RA = jl('b663_table_final.json'), jl('b663_root_arm.json')
    _r, _n, sh = seal_hashes()
    cm = jl('b663_commands.json')
    S = {
        'N1': (('HELD' if cm and not cm.get('local_lean') else 'REFUTED'),
               'commands of this act that run lean or lake on this host: %s (relay data/b663_commands.txt); the build on the hosted runner alone' % (
                   cm.get('local_lean') if cm else '### UNREAD')),
        'N2': _n2(), 'N3': _n3(), 'N4': _n4(), 'N5': _n5(),
        'H1': _h_from('b663_epstein_instance.txt', 'H1'), 'H2': _h_from('b663_epstein_instance.txt', 'H2'),
        'H3': _h_from('b663_epstein_control.txt', 'H3'), 'H4': _h_from('b663_epstein_control.txt', 'H4'),
        'S1': (('HELD' if not TF.get('gone') and not TF.get('grade_moved') else 'REFUTED') if TF else 'PENDING',
               'the table at the end against relay HEAD`s: moved %s, gone %s, added %s, grade moved %s' % (
                   len(TF.get('moved') or []), len(TF.get('gone') or []), len(TF.get('added') or []), len(TF.get('grade_moved') or []))),
        'S2': (('HELD' if RA.get('root_recomputed') == RA.get('root') and RA.get('root_copy') != RA.get('root') and not RA.get('late') else 'REFUTED')
               if RA else 'PENDING', 'the root recomputed equal, the one-byte control moving it, the root order holding locally'),
        'S3': ('HELD' if sh and all(v == 'agree' for _t, v in sh) else 'REFUTED', 'the sealed tools` hashes %s' % dict(collections.Counter(v for _t, v in sh))),
    }
    for k2 in SCORE_KEYS:
        read_score_row(k2, list(S[k2]))
    put_json('b663_scores.json', dict((k2, list(v)) for k2, v in S.items()))
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:500]))


NEXT_LINE = 'b664, per `(R273)`(7), the re-cut act on the next kernel by count under `(R265)`’s form; then b665, the Keiper face'


def _sv(S, k):
    return read_score_row(k, S.get(k) or ['?', ''])[1] if S.get(k) else '?'


def _q0():
    cs = jl('b663_epstein_control.json').get('cells') or []
    q = [c for c in cs if str(c.get('name', '')).startswith('Q0')]
    return q[0] if q else {}


def _title():
    q = _q0()
    zs = q.get('zero_side') or {}
    j = jl('b663_epstein_instance.json')
    S = jl('b663_scores.json')
    hs = [_sv(S, k) for k in HK]
    allh = all(h.startswith('HELD') for h in hs)
    return ('## The Epstein instance at Q0 on four named premises, merged alone at %s on the runner’s gate reading; the detector at the real '
            'configuration: j₀ = %s, the zero side %s zero; H1–H4 %s' % (
                j.get('tag') or 'its next tag', q.get('j0', '?'), 'below' if zs.get('held') else 'not below',
                'held, H3 and H4 on B1' if allh else ' '.join('%s %s' % (k, h) for k, h in zip(HK, hs))))


def _finding_text():
    S, J = jl('b663_scores.json'), jl('b663_act_root.json')
    rl, rl2, rl3 = jl('b663_record_lines.json'), jl('b663_record_lines_c2.json'), jl('b663_record_lines_c2b.json')
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b663_author_answers.txt'), re.M))
    ln0 = ((rl.get('lines') or [{}])[0]).get('line')
    lc2 = ((rl2.get('lines') or [{}])[0]).get('line')
    lc2b = ((rl3.get('lines') or [{}])[0]).get('line')
    j = jl('b663_epstein_instance.json')
    q = _q0()
    zs = q.get('zero_side') or {}
    cc = re.search(r'CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    e = ['', _title(), '',
         '*Filed at b663 on the author’s ruling `(R273)` and the author’s word (%d questions in %d calls). Banks: relay '
         '`data/b663_citation_check.txt`, `data/b663_epstein_plan.txt`, `data/b663_dominance.txt`, `data/b663_epstein_instance.txt`, '
         '`data/b663_epstein_control.txt`, `data/b663_map_diff.txt`, `data/b663_act_root.txt`.*' % (n_ans, len(_calls())), '',
         '**The citation check** (the gate step from b662): %s cites checked at HEAD, %s OK, %s misses -- the Q0 list named in banks that read '
         'it, one off-line zero where the bench banks seventeen and calls them certified, the instance described as new where b590 built it, '
         'a grade read as a print, a range naming five defects of eight -- each the navigator’s on the author’s word.' % (
             cc.group(1) if cc else '?', cc.group(2) if cc else '?', cc.group(3) if cc else '?'), '',
         '**The record lines** (`(R273)`(1)): b662 at its weight (FINDINGS :%s); W-ORD-EPSTEIN-CERTIFY (OPEN_TRAILS :%s) and W-ORD-FT-FIRST-ORDER '
         '(:%s) entered priced beside the plan on the author’s word.' % (ln0, lc2, lc2b), '',
         '**The plan** (`(R273)`(3)): the five rungs read by line and all five left priced, b590’s Schema/Epstein.lean read first and built on; '
         'the bench’s 360 points below height 150 -- 146 ordinates on the line, 17 off-line zeros with their orbits -- banked by two agreeing '
         'routes in mpmath, not ball-certified; the dominant at every base read is the zero at 0.9533 + 16.2902 i, not b590’s named one; raised as '
         'one prompt before any Lean.', '',
         '**The instance** (`(R273)`(2), (5)): SIDEExplicitFormula/Schema/EpsteinQ0.lean on four named premises -- the list in the configuration, '
         'the list complete below 150, a local count with the constant 10, and b590’s EpsteinPremises -- each a Prop stated, not proved; open; '
         'the target false, the schema’s equivalence by one application, the detector at the dominant, b590’s control at its zero, the rate '
         'theorem read at the instance; one dispatch, run %s, the artifact’s sha256 agreeing, %d prints at the standard three; Q0Premises entered '
         'in the E0 rule’s list of met names by ruling, the seven premise-carrying theorems INTERFACES on it; merged alone at %s. N2 %s, '
         'N3 %s.' % ((j.get('run') or {}).get('run_id'), len(j.get('rows') or []), j.get('tag'), _sv(S, 'N2'), _sv(S, 'N3')), '',
         '**The computation** (`(R273)`(4)): b662’s script carried whole with the changes the author let -- the configuration, the dominant over '
         'all seventeen orbits, θ and the kill set over the others and over the points above 150, the local count by its premise, the zero side '
         '-- its control at b661’s cell reproducing j₀ = 31; at Q0 every hypothesis of the rate theorem certified by name, the points above 150 on '
         'the first-order transform bound B1, a named READ premise, not a kernel lemma; hrate holds at j₀ = %s ≤ D + 40 = %s, and the zero side '
         'there is %s zero in certified arithmetic on the banked configuration. H1 %s, H2 %s, H3 %s, H4 %s. N4 %s.' % (
             q.get('j0', '?'), q.get('J_max', '?'), 'below' if zs.get('held') else 'not below', _sv(S, 'H1'), _sv(S, 'H2'), _sv(S, 'H3'),
             _sv(S, 'H4'), _sv(S, 'N4')), '',
         '**The root.** b663 over %d repositories, %d tags and %d banks, the last step of the act’s banks; its chain read at commit inside the suite.' % (
             len((J.get('reads') or {}).get('heads') or []), len((J.get('reads') or {}).get('tags') or []), len((J.get('reads') or {}).get('banks') or [])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): this act re-reads b590’s Epstein instance, b326’s zero census and b642’s rungs, and '
         'b661’s and b662’s map at its control cell; it is re-read by W-ORD-EPSTEIN-CERTIFY, by W-ORD-FT-FIRST-ORDER and by W-ORD-E2-SEPARATION’s '
         'act. It strengthens the programme’s offering of statements a reader can check: the schema’s negative control now fires at a '
         'configuration whose points a reader can list, on premises a reader can name, with the index and the sign printed in balls.', '',
         '**Next.** %s.' % NEXT_LINE, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero, or about ζ; the instance states what follows from its named '
         'premises, and the computation what the compiled rate theorem says of the banked configuration.*', '']
    return _title(), NL.join(e)


FOR_AUTHOR = ('(1) the dominant zero qE0 named beside b590’s rhoE, both in the Lean; (2) the computation’s script changes confined to the plan’s '
              'section 6, hrate’s lines left as b662 wrote them (defect (k)); (3) the tail above 150 in the zero side bounded on B1 and P3 by a '
              'polynomial count, its derivation in the script’s zero_side docstring; (4) the print list replaced by the act’s terminals, so the '
              'merged main prints the instance’s declarations; (5) H2 read from the compiled statement and its one-application proof')


def _trail_text():
    S, fj, J = (jl(n_) for n_ in ('b663_scores.json', 'b663_findings.json', 'b663_act_root.json'))
    rl, rl2, rl3 = jl('b663_record_lines.json'), jl('b663_record_lines_c2.json'), jl('b663_record_lines_c2b.json')
    n_ans = len(re.findall(r'^### PROMPT ', rdn('b663_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R273) ratified.** (1) b662 at its weight, its late defect at step zero. (2) The object: the schema’s negative control at Q0. (3) '
             'The rungs read and the plan raised before any Lean. (4) The computation at the real configuration, H1-H4 fixed. (5) The landing '
             'points. (6) The draft held at v5. (7) The act after: b664, then b665.', '',
             '**Entered:** FINDINGS.md:%s (b662’s weight), :%s (the entry); OPEN_TRAILS.md:%s (W-ORD-EPSTEIN-CERTIFY), :%s (W-ORD-FT-FIRST-ORDER); '
             'this record.' % (((rl.get('lines') or [{}])[0]).get('line'), fj.get('entry_line'), ((rl2.get('lines') or [{}])[0]).get('line'),
                               ((rl3.get('lines') or [{}])[0]).get('line')), '',
             '**Act root:** b663 `%s` (previous `%s`, b662’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF.' % (
                 J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d questions in %d calls (relay data/b663_author_answers.txt): the citation check’s misses before '
             'Component 1, the plan before any Lean, the E0 grade before the merge; none after the root.' % (n_ans, len(_calls())), '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b663_defects.txt): %s.' % ('; '.join(_defect_short()) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in SCORE_KEYS) + '.**', '',
             '**Next:** %s.' % NEXT_LINE, '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b663_scores.json')
    L = ['=' * 104, 'b663 -- THE DESK.', '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in SCORE_KEYS]
    L += [''] + rdn('b663_defects.txt').rstrip(NL).split(NL)
    put_txt('b663_desk_notes.txt', L)


def components(*a):
    S, fj, tj, J = (jl(n_) for n_ in ('b663_scores.json', 'b663_findings.json', 'b663_trail.json', 'b663_act_root.json'))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    rl, rl2, rl3 = jl('b663_record_lines.json'), jl('b663_record_lines_c2.json'), jl('b663_record_lines_c2b.json')
    j = jl('b663_epstein_instance.json')
    q = _q0()
    L = ['b663 -- THE COMPONENTS, BANKED UNDER (R273).', '',
         '### COMPONENT 0 : the citation check (data/b663_citation_check.txt), step zero (data/b663_ferry.txt, data/b663_stepzero.txt, '
         'data/b663_tests_stepzero.txt, data/b663_defects.txt) ; push-out relay %s ; N2 %s' % (K.STEPZERO, S['N2'][0]),
         '### COMPONENT 1 : b662`s weight FINDINGS :%s' % ((rl.get('lines') or [{}])[0]).get('line'),
         '### COMPONENT 2 : the plan (data/b663_epstein_plan.txt, data/b663_dominance.txt, data/b663_a0_list.txt) ; W-ORD-EPSTEIN-CERTIFY '
         'OPEN_TRAILS :%s ; W-ORD-FT-FIRST-ORDER :%s' % (((rl2.get('lines') or [{}])[0]).get('line'), ((rl3.get('lines') or [{}])[0]).get('line')),
         '### COMPONENT 3 : the instance (data/b663_epstein_instance.txt) ; run %s ; H1 %s ; H2 %s ; N3 %s' % (
             (j.get('run') or {}).get('run_id'), S['H1'][0], S['H2'][0], S['N3'][0]),
         '### COMPONENT 4 : the computation (data/b663_epstein_control.txt, data/b663_map_diff.txt) ; j₀ %s ; H3 %s ; H4 %s ; N4 %s' % (
             q.get('j0'), S['H3'][0], S['H4'][0], S['N4'][0]),
         '### COMPONENT 5 : the merge %s tag %s (data/b663_merge_push_out.txt)' % (j.get('merged'), j.get('tag')),
         '### COMPONENT 6 : the dry-run step (data/b663_reg_gate.txt), the seal (data/b663_seal_hashes.json), the suite ; S3 %s' % S['S3'][0],
         '### COMPONENT 7 : the root %s ; FINDINGS :%s ; OPEN_TRAILS :%s ; N1 %s ; N5 %s' % (
             (J.get('root') or '')[:16], fj.get('entry_line'), tj.get('line'), S['N1'][0], S['N5'][0])]
    put_txt('b663_components.txt', L)
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
    ln = _land_one(FIND, t, e, 'b663_findings.json', dict(title=t))
    j = jl('b663_findings.json')
    j['entry_line'] = ln
    put_json('b663_findings.json', j)
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
    ln = _land_one(OT, TRAIL_HEAD(), e, 'b663_trail.json', {})
    print('  OPEN_TRAILS record :%s' % ln)


def _face_needles(face_text, which):
    m = re.search(r'^### THE DRY-RUN NEEDLES -- %s: (.*)$' % which, face_text, re.M)
    return re.findall(r'"([^"]+)"', m.group(1)) if m else []


def drycheck(*a):
    """(R267)(2), STANDING FROM b657: the FINDINGS entry and the trail record composed as the record tool composes them -- under stand-ins
    for the banks not yet written (B663_STANDIN) -- converted by conv and run through the screens their landing runs, the needles the face
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


def gatebanks(*a):
    """the gate's steps between the face and the lock (b662's order), each tool's output banked by this route, never by a shell redirect:
    banned_terms --new -> data/b663_reg_termscan.txt; b663_regspec.py -> data/b663_regspec_run.txt; reg_satisfiable.py --emit b663 (it writes
    data/audit_b663_reg_satisfiable.txt itself); the step-zero censuses and pins -> data/b663_census_stepzero.txt,
    data/b663_faces_census_stepzero.txt, data/b663_pins_stepzero.txt; then gate_hash stamps the four face-subject records."""
    import gate_hash as G
    env = dict(os.environ, PYTHONIOENCODING='utf-8')

    def runb(args, out):
        r = subprocess.run([sys.executable] + args, capture_output=True, cwd=ROOT, env=env)
        b = (r.stdout + r.stderr).replace(b'\r\n', b'\n')
        if out:
            p = os.path.join(D, out)
            open(p + '.tmp', 'wb').write(b)
            os.replace(p + '.tmp', p)
        return r.returncode, b.decode('utf-8', 'replace')
    face_rel = 'data/b663_registration_2026-10-13.txt'
    rc1, t1 = runb([os.path.join(T, 'banned_terms.py'), '--new', face_rel], 'b663_reg_termscan.txt')
    rc2, t2 = runb([os.path.join(T, 'b663_regspec.py')], 'b663_regspec_run.txt')
    rc3, t3 = runb([os.path.join(T, 'reg_satisfiable.py'), 'data/b663_satisfiable.json', '--emit', 'b663'], None)
    print('  banned_terms rc %d ; %s' % (rc1, ([l for l in t1.split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    print('  regspec rc %d ; %s' % (rc2, ([l for l in t2.split(NL) if 'PREDICTIONS FOUND' in l] or ['### NONE'])[0].strip()))
    print('  reg_satisfiable rc %d ; %s' % (rc3, ([l for l in rdn('audit_b663_reg_satisfiable.txt').split(NL) if 'VERDICT' in l] or ['### NO VERDICT'])[0][:160]))
    for tool, out in (('b307_handoff_census.py', 'b663_census_stepzero.txt'), ('b327_faces_census.py', 'b663_faces_census_stepzero.txt'),
                      ('b303_pins.py', 'b663_pins_stepzero.txt')):
        rc, t = runb([os.path.join(T, tool), 'b663'], out)
        print('  %s rc %d ; %s' % (out, rc, ([l.strip() for l in t.split(NL) if 'TOTAL MISSING' in l or 'HARD-FAILING' in l] or ['### NONE'])[0][:120]))
    fa = os.path.join(ROOT, *face_rel.split('/'))
    for r in ('data/b663_reg_gate.txt', 'data/b663_reg_termscan.txt', 'data/b663_regspec_run.txt', 'data/audit_b663_reg_satisfiable.txt'):
        ra = os.path.join(ROOT, *r.split('/'))
        print('  stamp %s %s %s' % (r, G.stamp(ra, fa)[:16], G.matches(ra, fa)[0]))


ROUTES = {'gatebanks': gatebanks, 'c1': c1, 'answers': answers, 'dominance': dominance, 'c2': c2, 'c2b': c2b, 'a0list': a0list, 'runner': runner, 'mapdiff': mapdiff,
          'merged': merged, 'commands': commands, 'kernels': kernels, 'defects': defects, 'root': root, 'root_arm': root_arm,
          'table_final': table_final, 'scores': scores, 'desk': desk, 'components': components, 'findings': findings, 'trail': trail,
          'drycheck': drycheck}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b663_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
