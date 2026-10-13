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


READERS = ['read_head']


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


ROUTES = {'c1': c1, 'answers': answers, 'dominance': dominance, 'c2': c2, 'c2b': c2b, 'a0list': a0list, 'runner': runner, 'mapdiff': mapdiff}

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b663_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
