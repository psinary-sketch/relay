# -*- coding: utf-8 -*-
"""b550_record.py -- THE CASCADE, ACT SIX: THE_IDENTITY_CHAIN TIERED; THE RESIDUE PIN TAGGED; b546`S ORDER CORRECTED;
W-ORD-POWER-SWEEP FILED; THE BRIDGE`S THREE CONSUMERS ENTERED: THE RECORD, UNDER (R160).
### `python tools/b550_record.py reads | tag_read | pin_lines | order_lines | trails | tiers | reading37 | findings | identity_block |
### components | desk | trail`
### The tag itself is the seat`s command (READING (1)); this file reads it back and writes the lines. This file deletes nothing.
"""
import io, json, os, re, subprocess, sys, time
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
GS = os.path.join('D:', os.sep, 'SIDE-global-section')
LV = os.path.join('D:', os.sep, 'SIDE-lv-conservation')
FIND, OT = os.path.join(PP, 'FINDINGS.md'), os.path.join(PP, 'OPEN_TRAILS.md')
IDC = os.path.join(PP, 'phase2', 'method', 'THE_IDENTITY_CHAIN.md')
RES = os.path.join(PP, 'phase1.5', 'proofs', 'THE_RESIDUE_OF_RH.md')
SPIRAL = os.path.join(PP, 'SPIRAL_MAP.md')
NL = chr(10)
GS_HEAD = '2e43315'
GS_TAG = 'v0.1.0'
LV_MAIN = '2f71068'
TAG = 'v0.11.0'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rd(p):
    return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')


def jl(n):
    p = os.path.join(D, n)
    return json.loads(rd(p)) if os.path.exists(p) else {}


def put_json(n, obj):
    io.open(os.path.join(D, n), 'w', encoding='utf-8', newline=NL).write(json.dumps(obj, indent=1, ensure_ascii=False) + NL)


def put_txt(n, lines):
    io.open(os.path.join(D, n), 'w', encoding='utf-8', newline=NL).write(NL.join(lines) + NL)


def g(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def cite(L, path, a, z, what, text=None):
    t = (text if text is not None else rd(path)).split(NL)
    rel = os.path.relpath(path, PP) if path.startswith(PP) else (os.path.relpath(path, ROOT) if path.startswith(ROOT) else path)
    L.append('### %s:%d-%d -- %s' % (rel.replace(os.sep, '/'), a, min(z, len(t)), what))
    L.extend('  :%d %s' % (i + 1, t[i][:900]) for i in range(a - 1, min(z, len(t))))
    L.append('')


IFACE = ['Interfaces/FiniteInstanceIdentity.lean', 'Interfaces/GlobalSection.lean', 'Interfaces/LocalLimit.lean', 'Interfaces/RestrictedTensorLayer1.lean']
CORE_MODS = ['SectorNonvanishingShadow', 'InvolutionScalarShadow', 'AlternationShadow', 'SignTransferShadow', 'LadderOrientationShadow',
             'AggregationCircularityShadow', 'StatedChoiceShadow', 'TraceFactorizationShadow', 'FoldedMirrorShadow']
EXTRA_CORE = {'B270.absorb_2_2': 'BallAbsorptionShadow', 'B298.boundary_value_at_cell_2_2_on_member_radii_neg1_0': 'BoundaryValueShadow'}
IFACE_TERMS = [('FiniteInstanceIdentity.DiagonalCell', 'Interfaces/FiniteInstanceIdentity.lean'),
               ('FiniteInstanceIdentity.ArchimedeanE1Trace', 'Interfaces/FiniteInstanceIdentity.lean'),
               ('FiniteInstanceIdentity.QuotientTrace', 'Interfaces/FiniteInstanceIdentity.lean'),
               ('FiniteInstanceIdentity.WeilLedger', 'Interfaces/FiniteInstanceIdentity.lean'),
               ('FiniteInstanceIdentity.finiteInstanceIdentity', 'Interfaces/FiniteInstanceIdentity.lean'),
               ('GlobalSection.GlobalSectionData', 'Interfaces/GlobalSection.lean'),
               ('LocalLimit.proj4', 'Interfaces/LocalLimit.lean'), ('LocalLimit.proj4_eigen', 'Interfaces/LocalLimit.lean'),
               ('LocalLimit.proj4_sum', 'Interfaces/LocalLimit.lean'), ('LocalLimit.inner_map_self_of_fixed', 'Interfaces/LocalLimit.lean'),
               ('LocalLimit.radical_zero', 'Interfaces/LocalLimit.lean'), ('LocalLimit.eigenvector_of_commute', 'Interfaces/LocalLimit.lean'),
               ('LocalLimit.real_no_compact_open_addSubgroup', 'Interfaces/LocalLimit.lean'),
               ('RestrictedTensorLayer1.Ftensor_sq', 'Interfaces/RestrictedTensorLayer1.lean'),
               ('RestrictedTensorLayer1.parityTensor_sq', 'Interfaces/RestrictedTensorLayer1.lean'),
               ('RestrictedTensorLayer1.tensorFactor', 'Interfaces/RestrictedTensorLayer1.lean')]
LOCALLIMIT_SIX = ['proj4_eigen', 'proj4_sum', 'inner_map_self_of_fixed', 'radical_zero', 'eigenvector_of_commute', 'real_no_compact_open_addSubgroup']


def doc_named():
    """### every SIDE-global-section declaration the document names inside backticks, with the five generic-word matches the seat read
    ### by hand (`cell`, `identity`, `forced`, `corr`, `resid` -- a variable, a label, a formula`s symbol) removed and printed."""
    doc = rd(IDC).split(NL)
    out = g(GS, 'grep', '-nE', r'^\s*(noncomputable |private |protected )*(theorem|lemma|def|structure|class|abbrev|inductive|instance) [^ :({]+', GS_HEAD, '--', '*.lean')
    decl = {}
    for l in out.split(NL):
        m = re.match(r'[0-9a-f]+:([^:]+):(\d+):\s*(?:(?:noncomputable|private|protected) )*(?:theorem|lemma|def|structure|class|abbrev|inductive|instance) ([^ :({]+)', l)
        if m:
            decl.setdefault(m.group(3), []).append((m.group(1), int(m.group(2))))
    hits = {}
    for i, l in enumerate(doc, 1):
        for tok in re.findall(r'`([^`\n]+)`', l):
            for w in re.findall(r"[A-Za-z_][A-Za-z0-9_'.₀-₉]*", tok):
                b = w.split('.')[-1]
                if b in decl and len(b) > 3:
                    hits.setdefault(b, []).append(i)
    generic = {'cell', 'identity', 'forced', 'corr', 'resid'}
    return {k: dict(lines=v, decl=decl[k]) for k, v in hits.items() if k not in generic}, sorted(generic & set(hits)), len(decl)


# ------------------------------------------------------------------------------ THE READS
def reads():
    L = ['b550 -- THE ORDERED READS, CITED BY PATH AND LINE', '']
    cite(L, IDC, 1, 3166, 'THE_IDENTITY_CHAIN.md entire (§§1-38, every era block, the §37 mapping, the §38 table, the b299 pointer)')
    sp = [l for l in rd(SPIRAL).split(NL) if re.search(r'(?i)global[-_ ]?section', l)]
    L += ['### SPIRAL_MAP.md, every line naming the global section (%d):' % len(sp)] + ['  ' + l[:400] for l in sp]
    L += ['### SPIRAL_MAP cites a SIDE-global-section pin : %s' % ('NONE -- no SHA and no tag of that repository appears' if not any(re.search(r'[0-9a-f]{7}', l) and 'SIDE-global-section' in l for l in sp) else 'SEE ABOVE'),
          '### SIDE-global-section HEAD %s ; tree clean %s ; its tags: %s -> %s' % (
              g(GS, 'rev-parse', 'HEAD').strip(), g(GS, 'status', '--porcelain', '--untracked-files=no').strip() == '',
              ' '.join(g(GS, 'tag').split()), g(GS, 'rev-parse', GS_TAG + '^{commit}').strip()),
          '### commits from %s to HEAD : %s' % (GS_TAG, g(GS, 'rev-list', '--count', GS_TAG + '..HEAD').strip()), '']
    for f in IFACE:
        n = len(rd(os.path.join(GS, f)).split(NL))
        cite(L, os.path.join(GS, f), 1, n, 'SIDE-global-section HEAD %s' % GS_HEAD)
    for m in CORE_MODS + list(EXTRA_CORE.values()):
        f = os.path.join(GS, 'Core', m + '.lean')
        t = rd(f).split(NL)
        L.append('### Core/%s.lean : %d lines ; its declarations:' % (m, len(t)))
        L += ['  :%d %s' % (i + 1, l.strip()[:200]) for i, l in enumerate(t) if re.match(r'^\s*(theorem|lemma|def|structure|abbrev|inductive|instance) ', l)]
        L.append('')
    corr = rd(os.path.join(GS, 'CORRESPONDENCE.md')).split(NL)
    rows = [i for i, l in enumerate(corr) if re.match(r'^\| *(8[0-9]|90) *\|', l)]
    L.append('### SIDE-global-section CORRESPONDENCE.md rows 80-90, whole:')
    L += ['  :%d %s' % (i + 1, corr[i]) for i in rows] + ['']
    cite(L, FIND, 5529, 5531, 'the detection-geometries entry')
    cite(L, FIND, 5651, 5655, 'b549`s two lines and its entry`s heading')
    cite(L, OT, 3544, 3550, 'the owed-bridges table; W-ORD-LI-WEIL-BRIDGE at :3548')
    cite(L, os.path.join(D, 'b549_diagonal.txt'), 1, 74, 'the window definition as b549 printed it, and the price')
    t = rd(os.path.join(D, 'b548_sweep_xi.txt')).split(NL)
    L += ['### relay data/b548_sweep_xi.txt : %d lines ; its summary lines:' % len(t)] + ['  :%d %s' % (i + 1, l[:260]) for i, l in enumerate(t) if l.strip().startswith('### n =') or l.strip().startswith('### n=') or '### n = ' in l] + ['']
    L += ['### SIDE-lv-conservation main %s ; tree clean %s ; the remote`s main %s ; tags %s at the remote: %s' % (
        g(LV, 'rev-parse', 'HEAD').strip(), g(LV, 'status', '--porcelain', '--untracked-files=no').strip() == '',
        (g(LV, 'ls-remote', 'origin', 'refs/heads/main').split() or ['?'])[0], TAG,
        g(LV, 'ls-remote', 'origin', 'refs/tags/' + TAG).strip() or 'ABSENT')]
    named, generic, nd = doc_named()
    L += ['', '### the declarations the document names (backticked; %d declarations at HEAD searched; generic words dropped by hand: %s):' % (nd, generic)]
    L += ['  %-52s %s  doc lines %s' % (k, v['decl'][0][0] + ':' + str(v['decl'][0][1]), v['lines'][:6]) for k, v in named.items()]
    put_txt('b550_reads.txt', L)
    put_json('b550_named.json', dict(named=named, generic=generic))
    print('  reads banked : %d lines ; named %d' % (len(L), len(named)))


# ------------------------------------------------------------------------------ COMPONENT 1: THE TAG, READ BACK
def tag_read():
    t = rd(os.path.join(D, 'b550_tag.txt'))
    rem = dict((m.group(2), m.group(1)) for m in re.finditer(r'([0-9a-f]{40})\s+(refs/\S+)', t))
    before = re.search(r'### before: HEAD (\w+) ; status \(tracked\) \[(.*?)\]', t)
    after = re.search(r'### after: HEAD (\w+) ; status \(tracked\) \[(.*?)\]', t)
    local_peeled = re.search(r'peeled (\w+)', t).group(1)
    live = dict(tag=g(LV, 'rev-parse', TAG + '^{commit}').strip(), head=g(LV, 'rev-parse', 'HEAD').strip(),
                clean=g(LV, 'status', '--porcelain', '--untracked-files=no').strip() == '',
                annotated=g(LV, 'cat-file', '-t', TAG).strip())
    out = dict(remote_peeled=rem.get('refs/tags/%s^{}' % TAG), remote_tag=rem.get('refs/tags/' + TAG), remote_main=rem.get('refs/heads/main'),
               local_peeled=local_peeled, before_head=before.group(1), before_clean=before.group(2) == '', after_head=after.group(1),
               after_clean=after.group(2) == '', live=live)
    out['n1'] = bool(out['remote_peeled']) and out['remote_peeled'].startswith(LV_MAIN) and out['local_peeled'] == out['remote_peeled']
    put_json('b550_tag.json', out)
    print(json.dumps(out, indent=1))


# ------------------------------------------------------------------------------ THE APPENDS
def outside_bt(text):
    return sum(l.count('`') % 2 for l in text.split(NL))


def poss(t):
    return re.sub(r"(?<=[A-Za-z0-9)])`s\b", "'s", t)


def append_to(path, text):
    text = poss(text)
    if outside_bt(text):
        sys.exit('### UNBALANCED BACKTICKS IN THE APPEND TO %s' % path)
    import banned_terms as BT
    live = [m.group(0) for l in text.split(NL) for m in BT.PAT.finditer(l)]
    if live:
        sys.exit('### A BANNED STEM IN THE APPEND TO %s: %s' % (path, live))
    before = open(path, 'rb').read()
    add = text.encode('utf-8')
    if not before.endswith(b'\n'):
        add = b'\n' + add
    open(path, 'ab').write(add)
    after = open(path, 'rb').read()
    return dict(file=os.path.relpath(path, PP).replace(os.sep, '/'), before=len(before), added=len(after) - len(before), prefix=after.startswith(before))


def guard_absent(path, h):
    if poss(h).encode('utf-8') in open(path, 'rb').read():
        sys.exit('### ALREADY PRESENT IN %s: %s' % (os.path.basename(path), h[:80]))


def line_of(path, head):
    ls = [i + 1 for i, l in enumerate(rd(path).split(NL)) if l.startswith(poss(head))]
    return ls[0] if ls else None


RESL = '*Appended 2026-09-26 by b550, under the author`s ruling `(R160)`(1), to the tier block at :215:*'
PINL = '*Appended at b550 (2026-09-26) to b549`s entry (`FINDINGS.md`:5655), under `(R160)`(1):*'
ORD1 = '*Appended at b550 (2026-09-26) to the detection-geometries entry (`FINDINGS.md`:5529), under `(R160)`(2) -- A CORRECTION, THE NAVIGATOR’S:*'
ORD2 = '*Restated in the bench’s own variable (b550, under `(R160)`(2)):*'
PSH = '### `W-ORD-POWER-SWEEP` — filed 2026-09-26, b550, under the author`s ruling (R160)(3)'
BRH = ('### `W-ORD-LI-WEIL-BRIDGE` (the row at :3548) — THREE CONSUMERS AND A TOOLCHAIN PRICE, appended 2026-09-26, b550, under the '
       'author`s ruling (R160)(4)')
READH = '## The bench functional against the cell-level sign: THE_IDENTITY_CHAIN §37 read beside `h2_sign` and b522`s F'
ACTH = '## The cascade, act six: THE_IDENTITY_CHAIN tiered, the residue pin tagged, the bench functional read against the cell-level sign'
IDH = ('#### **THE CASCADE, ACT SIX -- THE TERMINALS TIERED** *(appended 2026-09-26, b550, under the author`s ruling `(R160)`(5); '
       'no byte above this block changes; §§1–38 are not edited)*')
HEADING = ('### b550 — the cascade, act six under (R160): THE_IDENTITY_CHAIN tiered; the residue pin tagged v0.11.0; b546`s order '
           'corrected; W-ORD-POWER-SWEEP filed; the bridge`s three consumers entered')


def pin_lines():
    tj = jl('b550_tag.json')
    guard_absent(FIND, PINL)
    s = ('the read`s pin is tagged: SIDE-lv-conservation `%s` (annotated, tag object `%s`) at `main` `%s`, its peeled SHA read back '
         'from the remote equal to the local. The tip `5a14205` and `main` `2f71068`, byte-identical in the two files holding the '
         'terminals, both stand as the read.' % (TAG, tj['remote_tag'][:7], tj['remote_peeled'][:7]))
    o1 = append_to(RES, NL.join(['', RESL + ' ' + s, ''])) if line_of(RES, RESL) is None else dict(note='already written by the first run of this command, which then refused its FINDINGS append')
    s2 = (' the residue terminals’ pin is tagged, SIDE-lv-conservation `%s` at `%s`, the peeled SHA read back from the remote. '
          '`(R159)`(5)`s "re-read at v0.10.0" named a tag the terminals postdate; the clause was the navigator`s, and (N1)`s tag half '
          'fails as scored.' % (TAG, tj['remote_peeled'][:7]))
    o2 = append_to(FIND, NL.join(['', PINL + s2, '']))
    put_json('b550_pin_lines.json', dict(residue=o1, residue_line=line_of(RES, RESL), findings=o2, findings_line=line_of(FIND, PINL)))
    print('  RESIDUE :%s ; FINDINGS :%s' % (line_of(RES, RESL), line_of(FIND, PINL)))


def order_lines():
    guard_absent(FIND, ORD1)
    sj = jl('b548_sweep.json')
    sn = sj['H2']['smallest_negative']
    ws = ', '.join('%.0f' % sn[k] for k in ('3', '5', '7', '9', '11'))
    tails = {p: sj['q'][p]['status'] for p in ('3', '5')}
    l1 = (ORD1 + ' the entry and `(R156)`(4) wrote "width and order" as if the bench`s order were the power-window route`s. They are two '
          'objects under one word. b522`s window of parameter a is a plateau on [−ln a, ln a] whose two ramps are order-p B-splines; its '
          'support does not grow with p, and its transform decays as |u|^(2−2p). The route`s n is a convolution power of a fixed base, '
          'whose support grows with n. The conflation was the navigator`s.')
    l2 = (ORD2 + ' at Q0 the ramp order p governs the transform`s decay, and so how much of the far zero sum reaches a given width. That '
          'is why the smallest negative width rose with p in b548 -- %s at p = 3, 5, 7, 9, 11 (relay `data/b548_sweep.json`) -- and why '
          'the low-order cells are decided under the tail estimate (at p = 3 and p = 5 every cell is VERIFIED-EST-TAIL: %s). The '
          'route`s own variable has not been measured on this bench.' % (ws, tails))
    o = append_to(FIND, NL.join(['', l1, '', l2, '']))
    put_json('b550_order_lines.json', dict(write=o, l1=line_of(FIND, ORD1), l2=line_of(FIND, ORD2), widths=sn, tails=tails))
    print('  FINDINGS :%s and :%s' % (line_of(FIND, ORD1), line_of(FIND, ORD2)))
    print(poss(l1))
    print(poss(l2))


def h3_verbatim():
    t = ' '.join(rd(os.path.join(D, 'b549_ferry.txt')).split(NL)[37:44])
    a = t.index('Hypothesis H3, fixed before any reading:')
    z = t.index('negative above its floor.', a) + len('negative above its floor.')
    return t[a:z]


def trails():
    guard_absent(OT, BRH)
    dg = rd(os.path.join(D, 'b549_diagonal.txt')).split(NL)
    pr = rd(os.path.join(D, 'b549_premise.txt')).split(NL)
    fj = jl('b549_family.json')
    h3 = h3_verbatim()
    ps = ['', PSH, '',
          '| # | ID | kind | the item | price | trigger |', '|:--|:--|:--|:--|:--|:--|',
          '| **1** | `W-ORD-POWER-SWEEP` | **BENCH** | The functional F(a, n) = P − PR + A read in the power-window route`s own variable: a '
          'window family that is the n-th convolution power of a fixed base, its support growing with n, swept at ξ and Q0 across the '
          'orders banked, so that F(n·b, n) at fixed base half-width b is the route`s sequence. b548`s bench swept a plateau whose ramps '
          'change order at fixed support (b549, relay `data/b549_diagonal.txt`:1-63); this is the other object. **The hypothesis to '
          'score, carried from `(R159)`(2) unchanged:** "%s" | as b549 priced it (relay `data/b549_diagonal.txt`:64-73): about %.0f s of '
          'cells at b548`s per-cell cost (Q0 %.0f s, ξ %.0f s); a new window class in the ladder -- the n-th convolution power, its own '
          'hhat in closed form; tail constants re-derived for the self-convolution family (b521`s divide by the plateau half-width, '
          'which this family lacks); and a fixture with floors per `(R125)`(2) | **it runs when the self-convolution family is '
          'implemented as a ladder window class with its own hhat and its fixture passes the ξ positive control at every order** |'
          % (h3, fj['cost_total']['q'] + fj['cost_total']['xi'], fj['cost_total']['q'], fj['cost_total']['xi']), '',
          '*Filed, not started. No grade moves; `h2` stands where the deposit left it.*', '']
    br = ['', BRH, '',
          '**Three consumers**, each a place the bridge would carry a result the corpus holds on one side only:', '',
          '- **(a) The Weil premise of `residue_irreducible`.** Its premise `inequalityToPositivity` is Li-channel on arbitrary sequences ℕ → ℝ, '
          'not in the `classK` form of `h2_sign` (b549, relay `data/b549_premise.txt`:20); the bridge is what would carry '
          '`h2_sign_iff_rh` into it.',
          '- **(b) The two detection costs of `(R156)`(4).** The Weil side`s cost (a window of width and ramp order at Q0) and the Li '
          'side`s (an index, n ≳ 2T²) are stated in different variables (`FINDINGS.md`:5529); the bridge would translate them into one.',
          '- **(c) The Li form made T0.** §1 of THE_RESIDUE_OF_RH states Li`s criterion, T1-lit per `(R156)`(1); a compiled bridge to '
          '`h2_sign_iff_rh` (T0) would make the Li form T0.', '',
          '**The price gains one line, as its own item, before any lemma:** a toolchain alignment. The two kernels sit on different '
          'toolchains and Mathlib pins -- %s (relay `data/b549_premise.txt`:24) -- so the bridge first needs one of them moved onto the '
          'other`s toolchain and Mathlib, or the statements restated in one kernel; priced as a separate item, not begun.'
          % pr[23].split('### lv requires ')[-1].split(' -- lv does not')[0].replace("['require mathlib from git'] ; ", ''), '',
          '*Appended beneath the row at :3548; the row above is unchanged. Nothing is built.*', '']
    o1 = append_to(OT, NL.join(ps)) if line_of(OT, PSH) is None else dict(note='already written by the first run of this command, which then refused its second append')
    o2 = append_to(OT, NL.join(br))
    put_json('b550_trails.json', dict(power=o1, power_line=line_of(OT, PSH), bridge=o2, bridge_line=line_of(OT, BRH), h3=h3,
                                      price_lines=dg[63:73], premise_lines=[pr[19], pr[23]]))
    print('  OPEN_TRAILS : power sweep :%s ; bridge :%s' % (line_of(OT, PSH), line_of(OT, BRH)))


# ------------------------------------------------------------------------------ COMPONENT 5: THE TERMINALS TIERED
def squash(t):
    return re.sub(r'\[([^\]]*)\]', lambda m: '[' + ' '.join(m.group(1).split()) + ']', t, flags=re.S)


def prints(path):
    out = {}
    for l in squash(rd(path)).split(NL):
        m = re.match(r"^'(.+)' (does not depend on any axioms|depends on axioms: \[([^\]]*)\])", l)
        if m:
            out[m.group(1)] = sorted(x.strip() for x in (m.group(3) or '').split(',') if x.strip()) if m.group(3) is not None else []
    return out


def statements(path, names):
    t = rd(path)
    out = {}
    for n in names:
        ms = list(re.finditer(r'(?m)^@?' + re.escape(n) + r' :', t))
        if not ms:
            continue
        lines = t[ms[-1].start():].split(NL)
        body = [lines[0]]
        for l in lines[1:]:
            if not l.startswith((' ', '\t')):
                break
            body.append(l)
        out[n] = ' '.join(' '.join(body).split())
    return out


def conclusion(stmt):
    s = stmt.split(' : ', 1)[1] if ' : ' in stmt else stmt
    depth, last = 0, 0
    for i, ch in enumerate(s):
        if ch in '([{⟨':
            depth += 1
        elif ch in ')]}⟩':
            depth -= 1
        elif ch == '→' and depth == 0:
            last = i + 1
    c = s[last:].strip()
    return re.sub(r'^∀[^,]*,\s*', '', c)


def ei(kind, stmt):
    if kind in ('def', 'structure', 'abbrev', 'inductive', 'instance'):
        return '—'
    c = conclusion(stmt)
    return 'I' if re.search(r'<|≤|≥|>', c.replace('→', '')) and '↔' not in c else 'E'


def kind_of(module_file, short):
    for l in rd(os.path.join(GS, module_file)).split(NL):
        m = re.match(r'^\s*(?:@\[[^\]]*\]\s*)?(?:noncomputable |private |protected )*(theorem|lemma|def|structure|abbrev|inductive|instance)\s+' + re.escape(short) + r'(?![A-Za-z0-9_\'])', l)
        if m:
            return m.group(1)
    return None


def in_tag(module_file, short):
    return subprocess.run(['git', '-C', GS, 'cat-file', '-e', '%s:%s' % (GS_TAG, module_file)], capture_output=True).returncode == 0 and \
        re.search(r'(?m)^\s*(?:noncomputable |private |protected )*(theorem|lemma|def|structure|abbrev|inductive|instance)\s+' + re.escape(short) + r'(?![A-Za-z0-9_\'])',
                  g(GS, 'show', '%s:%s' % (GS_TAG, module_file))) is not None


def first_added(module_file, kind=None, short=None):
    """### the commit that first carried the declaration`s line (git log -S, oldest), else the file`s first commit."""
    if kind and short:
        hits = g(GS, 'log', '--format=%h', '-S', '%s %s' % (kind, short), '--', module_file).split()
        if hits:
            return hits[-1]
    return (g(GS, 'log', '--diff-filter=A', '--format=%h', '--', module_file).split() or ['?'])[-1]


def tiers():
    ap_b, ap_f = prints(os.path.join(GS, 'AXIOM_PRINTS.txt')), prints(os.path.join(D, 'b550_allprints_run.txt'))
    ai_b = prints(os.path.join(GS, 'AXIOM_PRINTS_INTERFACES.txt'))
    ai_f = dict(prints(os.path.join(D, 'b550_iface_check_a.txt')), **prints(os.path.join(D, 'b550_iface_check_b.txt')))
    core = [n for n in ap_b if n.split('.')[0] in CORE_MODS or n in EXTRA_CORE]
    cst = statements(os.path.join(D, 'b550_core_check.txt'), core)
    ist = dict(statements(os.path.join(D, 'b550_iface_check_a.txt'), [n for n, _ in IFACE_TERMS]),
               **statements(os.path.join(D, 'b550_iface_check_b.txt'), [n for n, _ in IFACE_TERMS]))
    named = jl('b550_named.json')['named']
    rows = []
    for n, f in IFACE_TERMS:
        short = n.split('.', 1)[1]
        k = kind_of(f, short)
        mod = n.split('.')[0]
        if mod == 'LocalLimit':
            tier, grade = ('T0', 'DEFINITION') if k == 'def' else ('T0', 'DERIVES')
            why = 'a statement about an arbitrary complex inner product space or about ℝ; premise-free beyond its mathematical hypotheses'
        elif short == 'finiteInstanceIdentity':
            tier, grade, why = 'T2', 'ENCODES', 'a Prop over supplied data structures (the file: "THIS FILE STATES; IT DOES NOT PROVE")'
        elif k in ('structure', 'def', 'abbrev'):
            tier, grade, why = 'T2', 'SHELL', 'a structure or definition over free data; it constrains nothing by itself'
        else:
            tier, grade, why = 'T2', 'ENCODES', 'a theorem over the program-typed `FactorData`; the global-section shape is carried by its fields'
        fb = ai_b.get(n)
        fr = ai_f.get(n)
        disp = 'CARRIED' if (fr is not None and (fb is None or fb == fr)) else 'MOVED'
        rows.append(dict(terminal=n, module=f, kind=k, statement=ist.get(n), fresh=fr, banked=fb, tier=tier, grade=grade, why=why,
                         ei=ei(k, ist.get(n) or ''), disp=disp, named=short.split('.')[-1] in named, in_tag=in_tag(f, short), first=first_added(f, k, short)))
    for n in core:
        mod = EXTRA_CORE.get(n, n.split('.')[0])
        f = 'Core/%s.lean' % mod
        short = n.split('.', 1)[1]
        k = kind_of(f, short)
        grade = 'SHELL' if k in ('def', 'structure', 'abbrev', 'inductive', 'instance') else 'ENCODES'
        fb, fr = ap_b.get(n), ap_f.get(n)
        disp = 'CARRIED' if (fr is not None and fb == fr and n in cst) else 'MOVED'
        rows.append(dict(terminal=n, module=f, kind=k, statement=cst.get(n), fresh=fr, banked=fb, tier='T2', grade=grade,
                         why='a Core shadow: arithmetic or logic over its own types and predicates; the reading is carried by the identifier',
                         ei=ei(k, cst.get(n) or ''), disp=disp, named=short in named, in_tag=in_tag(f, short), first=first_added(f, k, short)))
    tc = {k: sum(1 for r in rows if r['tier'] == k) for k in ('T0', 'T1-open', 'T1-lit', 'T2', 'T3', 'T4')}
    gc = {k: sum(1 for r in rows if r['grade'] == k) for k in ('DERIVES', 'DEFINITION', 'ENCODES', 'SHELL')}
    dc = {k: sum(1 for r in rows if r['disp'] == k) for k in ('CARRIED', 'MOVED')}
    ec = {k: sum(1 for r in rows if r['ei'] == k) for k in ('E', 'I', '—')}
    named_rows = [r for r in rows if r['named']]
    missing_named = sorted(set(named) - set(r['terminal'].split('.')[-1] for r in rows))
    not_in_tag = [r for r in rows if r['named'] and not r['in_tag']]
    L = ['b550 -- COMPONENT 5 (a)-(b): THE TERMINALS OF THE_IDENTITY_CHAIN, TIERED (READINGS (7)-(10))', '',
         '### AllPrints at HEAD against AXIOM_PRINTS.txt: %d lines fresh, %d banked, equal %s' % (
             len(rd(os.path.join(D, 'b550_allprints_run.txt')).rstrip(NL).split(NL)), len(rd(os.path.join(GS, 'AXIOM_PRINTS.txt')).rstrip(NL).split(NL)),
             rd(os.path.join(D, 'b550_allprints_run.txt')).rstrip(NL) == rd(os.path.join(GS, 'AXIOM_PRINTS.txt')).rstrip(NL)), '',
         '  terminal                                                         kind       fresh profile                      tier grade      E/I disp     named tag`s tree / first added']
    for r in rows:
        L.append('  %-64s %-10s %-34s %-4s %-10s %-3s %-8s %-5s %s / %s' % (r['terminal'][:64], r['kind'], ('axiom-free' if r['fresh'] == [] else ', '.join(r['fresh'] or ['NONE']))[:34],
                                                                          r['tier'], r['grade'], r['ei'], r['disp'], 'yes' if r['named'] else '', 'present' if r['in_tag'] else 'ABSENT', r['first']))
    L += ['', '### the statements, fresh:'] + ['  %s' % (r['statement'] or r['terminal'] + ' : NO STATEMENT READ')[:400] for r in rows]
    L += ['', '### terminals %d (Interfaces %d, Core %d) ; tiers %s ; grades %s ; E/I %s ; dispositions %s' % (
        len(rows), len(IFACE_TERMS), len(core), tc, gc, ec, dc),
        '### the document names %d of them; named but not in the set: %s' % (len(named_rows), missing_named or 'NONE'),
        '### document-named terminals absent from the tree of %s (%s): %d -- %s' % (GS_TAG, g(GS, 'rev-parse', '--short', GS_TAG + '^{commit}').strip(), len(not_in_tag),
                                                                                   ', '.join('%s (first %s)' % (r['terminal'], r['first']) for r in not_in_tag)),
        '### the order`s wording: the Core shadows sit in correspondence rows 81-89 (FoldedMirrorShadow at 89, RestrictedTensorLayer1 at 80), '
        'and AggregationCircularityShadow has no correspondence row; its nine terminals print in AXIOM_PRINTS.txt:367-375.']
    put_json('b550_tiers.json', dict(rows=rows, tier_counts=tc, grade_counts=gc, ei_counts=ec, disp_counts=dc, named_count=len(named_rows),
                                     missing_named=missing_named, not_in_tag=[(r['terminal'], r['first']) for r in not_in_tag],
                                     allprints_equal=rd(os.path.join(D, 'b550_allprints_run.txt')).rstrip(NL) == rd(os.path.join(GS, 'AXIOM_PRINTS.txt')).rstrip(NL),
                                     iface_equal={r['terminal']: r['fresh'] == r['banked'] for r in rows if r['module'].startswith('Interfaces') and r['banked'] is not None}))
    put_txt('b550_tiers.txt', L)
    print(NL.join(L[-6:]))


# ------------------------------------------------------------------------------ COMPONENT 5 (d)-(e): THE STEMS, THE READING OF §37
def reading37():
    import banned_terms as BT
    doc = rd(IDC).split(NL)
    counts = {s: 0 for s in BT.STEMS}
    for l in doc:
        for m in BT.PAT.finditer(l):
            counts[m.group(1).lower()] += 1
    cell = [(i + 1, l.strip()) for i, l in enumerate(rd(os.path.join(T, 'b521_tail.py')).split(NL)) if 'h2=P - PR + A' in l]
    fe = [(i + 1, l.strip()) for i, l in enumerate(rd(os.path.join(GS, 'Interfaces', 'FiniteInstanceIdentity.lean')).split(NL)) if 'T.value + Q.value = W.wInf - W.wPrimes' in l and '`' not in l]
    right = [(i + 1, l.strip()) for i, l in enumerate(doc) if l.startswith('**LEFT**') or ('**RIGHT**' in l and 'A − PR' in l)]
    h2 = g(os.path.join('D:', os.sep, 'SIDE-explicit-formula'), 'show', 'v0.2:SIDEExplicitFormula/H2Sign.lean').split(NL)
    s37 = [(i + 1, l.strip()) for i, l in enumerate(doc) if 'THE SIGN OF `A − PR`' in l]
    wdef = [l for l in rd(os.path.join(D, 'b549_diagonal.txt')).split(NL) if l.startswith('### read: L = ln a') or l.startswith('### φ = ') or l.startswith('### function is k̂')]
    ok = bool(cell) and bool(fe) and bool(right) and 'poleTerm k - primeSum k + archTerm k' in h2[29] and bool(s37)
    L = ['b550 -- COMPONENT 5 (d)-(e): THE STEMS; THE READING OF §37 (READINGS (11)-(12))', '',
         '### (d) banned stems in THE_IDENTITY_CHAIN.md, counted per stem, none listed, none edited: %s' % counts, '',
         '### (e) the b522 window, as b549 read it (relay data/b549_diagonal.txt):'] + ['  ' + w for w in wdef] + [
        '', '### the three expressions, side by side:',
        '  the bench (b521`s cell, tools/b521_tail.py:%d)          %s' % (cell[0][0], cell[0][1]) if cell else '  the bench : NOT FOUND',
        '  file E (Interfaces/FiniteInstanceIdentity.lean:%d)     %s' % (fe[0][0], fe[0][1]) if fe else '  file E : NOT FOUND',
        '  §38`s sides (THE_IDENTITY_CHAIN.md:%s)                 %s' % (','.join(str(x[0]) for x in right), ' | '.join(x[1][:200] for x in right)),
        '  h2_sign (SIDE-explicit-formula v0.2, H2Sign.lean:29-30) %s %s' % (h2[28].strip(), h2[29].strip()),
        '  §37`s mapping (THE_IDENTITY_CHAIN.md:%s)               %s' % (','.join(str(x[0]) for x in s37), ' '.join(x[1][:160] for x in s37)),
        '', '### READ: F = P − PR + A (the bench) ; file E`s right side W.wInf − W.wPrimes, adopted as A − PR at the atlas`s convention (§38) ;',
        '### h2_sign = 0 ≤ P − PR + A over every classK k. So F and file E`s adopted right side share A − PR and differ by the pole term P;',
        '### F at a ladder window is h2_sign`s quantity at one test function. VERDICT (N4) : %s' % ('HOLDS' if ok else 'NOT ESTABLISHED')]
    put_json('b550_reading37.json', dict(stems=counts, cell=cell, fileE=fe, right=right, h2sign=[h2[28], h2[29]], s37=s37, ok=ok))
    put_txt('b550_reading37.txt', L)
    print(NL.join(L))


def findings():
    guard_absent(FIND, READH)
    tj, rj, pl, ol, tr = jl('b550_tiers.json'), jl('b550_reading37.json'), jl('b550_pin_lines.json'), jl('b550_order_lines.json'), jl('b550_trails.json')
    rd_ = ['', READH, '',
           '*Filed at b550 on the author`s ruling `(R160)`(6). A reading, in the descriptive voice; §§1–38 of THE_IDENTITY_CHAIN are not '
           'edited. Bank: relay `data/b550_reading37.txt`.*', '',
           '§37 maps the deposit`s fourth register -- "the balance-to-positivity distance at the multiplicative place" -- to the sign of '
           '`A − PR` at a diagonal a² cell under one named convention. The b522 witness functional is F = P − PR + A on the ladder`s window '
           'class (relay `tools/b521_tail.py`:%d), and b548 swept it at ξ and at Q0. File E`s relation is `T.value + Q.value = W.wInf - '
           'W.wPrimes` (SIDE-global-section `Interfaces/FiniteInstanceIdentity.lean`:%d), whose right side §38 adopts as `A − PR` at the '
           'atlas`s convention. So the cell-level object of §37 and the bench`s F are one quantity up to the pole term P; and the compiled '
           '`h2_sign` (SIDE-explicit-formula v0.2, `H2Sign.lean`:29–30) is that quantity`s nonnegativity, 0 ≤ P − PR + A, over every '
           '`classK` test function -- of which the ladder`s window at a given a and p is one.' % (rj['cell'][0][0], rj['fileE'][0][0]), '',
           '**Its three limits, stated with it.** (i) The identity`s LEFT side, T + Q -- the traces -- is not the Weil functional, and '
           '`h2_sign` does not touch it. (ii) The b240 dissonance at six cells (§38) is about that left side and is unchanged. (iii) '
           'Nothing about ζ’s zeros is claimed: the reading relates three statements of one quantity; it proves none of them.', '',
           '*Nothing deposits; nothing here is a statement about RH.*', '']
    o1 = append_to(FIND, NL.join(rd_))
    tc, gc, dc, ec = tj['tier_counts'], tj['grade_counts'], tj['disp_counts'], tj['ei_counts']
    act = ['', ACTH, '',
           '*Filed at b550 on the author`s ruling `(R160)`. The cascade`s act six. Banks: relay `data/b550_tiers.txt`, `data/b550_tag.txt`, '
           '`data/b550_allprints_run.txt`, `data/b550_core_check.txt`, `data/b550_iface_check_a.txt`, `data/b550_iface_check_b.txt`, '
           '`data/b550_reading37.txt`.*', '',
           '**THE_IDENTITY_CHAIN (Tier C), tiered; it stays Tier C** -- it organizes and certifies nothing. Its terminals are '
           'SIDE-global-section`s, read at HEAD `2e43315` (SPIRAL_MAP cites no pin of that repository): %d in all -- the %d declarations '
           'the document names, and the modules `(R160)`(5) names (file E, GlobalSection`s structure, six LocalLimit theorems, '
           'RestrictedTensorLayer1`s three, and every printed terminal of the nine Core shadows). Tiers: %s. Grades: %s. E/I: %s. '
           'Dispositions: %s. `AllPrints.lean` re-run at HEAD reproduces `AXIOM_PRINTS.txt` line for line; the interface prints match '
           'their bank. The Core shadows sit in correspondence rows 81–89, and AggregationCircularityShadow has none.'
           % (len(tj['rows']), tj['named_count'], ' · '.join('%s %d' % kv for kv in tc.items()), ' · '.join('%s %d' % kv for kv in gc.items()),
              ' · '.join('%s %d' % kv for kv in ec.items()), ' · '.join('%s %d' % kv for kv in dc.items())), '',
           '**The residue pin, tagged.** SIDE-lv-conservation `v0.11.0` at `2f71068`, annotated, the peeled SHA read back from the remote '
           '(`FINDINGS.md`:%s; THE_RESIDUE_OF_RH.md:%s).' % (pl['findings_line'], pl['residue_line']), '',
           '**b546`s "order", corrected** as the navigator`s at `FINDINGS.md`:%s, with the observation restated in the bench`s own variable '
           'at :%s.' % (ol['l1'], ol['l2']), '',
           '**Filed and entered on the trails:** `W-ORD-POWER-SWEEP` (OPEN_TRAILS.md:%s), H3 carried unchanged; the Li–Weil bridge`s three '
           'consumers and its toolchain price (OPEN_TRAILS.md:%s).' % (tr['power_line'], tr['bridge_line']), '',
           '**The bench functional against the cell-level sign** is read at `FINDINGS.md`:%d.' % line_of(FIND, READH), '',
           '**Next keystone:** THE_KEYSTONE_CENSUS.', '',
           '*Nothing deposits; nothing at Zenodo written; no kernel file edited; nothing here is a statement about RH or about ζ’s zeros.*', '']
    o2 = append_to(FIND, NL.join(act))
    put_json('b550_findings.json', dict(reading=o1, reading_line=line_of(FIND, READH), act=o2, act_line=line_of(FIND, ACTH)))
    print('  FINDINGS : reading :%s ; act :%s' % (line_of(FIND, READH), line_of(FIND, ACTH)))


CORRL = '*Correction, appended at b550 (2026-09-26) to the reading at `FINDINGS.md`:5685:*'


def correction():
    guard_absent(FIND, CORRL)
    t = (CORRL + ' it cites file E`s relation at `Interfaces/FiniteInstanceIdentity.lean`:176, a docstring line that quotes it; the '
         'definition is at :216 and its body, `T.value + Q.value = W.wInf - W.wPrimes`, at :219. The relation is the same; the citation '
         'was the docstring`s.')
    o = append_to(FIND, NL.join(['', t, '']))
    o['line'] = line_of(FIND, CORRL)
    put_json('b550_correction.json', o)
    print('  FINDINGS correction :%s' % o['line'])


def identity_block():
    guard_absent(IDC, IDH)
    tj, fj = jl('b550_tiers.json'), jl('b550_findings.json')
    groups = {}
    for r in tj['rows']:
        key = r['module'] if r['module'].startswith('Core') else r['terminal']
        groups.setdefault(key, []).append(r)
    tab = ['| terminal or module | count | fresh profile | tier | grade | E/I | disposition |', '|:--|--:|:--|:--|:--|:--|:--|']
    for k, rs in groups.items():
        prof = sorted(set('axiom-free' if r['fresh'] == [] else ', '.join(r['fresh'] or ['NONE']) for r in rs))
        eic = {}
        for r in rs:
            eic[r['ei']] = eic.get(r['ei'], 0) + 1
        tab.append('| `%s` | %d | %s | %s | %s | %s | **%s** |' % (
            k.replace('Core/', '').replace('.lean', ''), len(rs), '; '.join(prof), ', '.join(sorted(set(r['tier'] for r in rs))),
            ', '.join(sorted(set(r['grade'] for r in rs))), ' · '.join('%s %d' % kv for kv in sorted(eic.items())),
            ', '.join(sorted(set(r['disp'] for r in rs)))))
    L = ['', '<!-- b550 TIER BLOCK, 2026-09-26 -->', '', IDH, '',
         '**The terminals, re-read at SIDE-global-section HEAD `2e43315`** (SPIRAL_MAP cites no pin of that repository; its one tag, '
         '`v0.1.0` = `706a81b`, predates most of them). Statements by a fresh `#check`, profiles by `#print axioms`: the Core layer by '
         '`AllPrints.lean`, which reproduces `AXIOM_PRINTS.txt` line for line; the Interfaces against Mathlib at the declared pin, and '
         'RestrictedTensorLayer1 at the checkout its own print names (relay `data/b550_tiers.txt`).', ''] + tab + [
        '', '*Totals over %d terminals: tiers %s; grades %s; E/I %s; dispositions %s.*' % (
            len(tj['rows']), ' · '.join('%s %d' % kv for kv in tj['tier_counts'].items()), ' · '.join('%s %d' % kv for kv in tj['grade_counts'].items()),
            ' · '.join('%s %d' % kv for kv in tj['ei_counts'].items()), ' · '.join('%s %d' % kv for kv in tj['disp_counts'].items())), '',
        '**This document stays Tier C:** it organizes and certifies nothing; the table grades its terminals, not it.', '',
        '**Back matter -- the reading the cascade adds.** §37`s cell-level sign read beside the bench`s F and the compiled `h2_sign`, '
        'with its three limits, is entered at `FINDINGS.md`:%d (b550).' % fj['reading_line'], '',
        '*Appended by b550. No claim of §§1–38 is altered; `h2` stays where the deposit left it.*', '']
    o = append_to(IDC, NL.join(L))
    o['heading_line'] = line_of(IDC, IDH)
    put_json('b550_identity_block.json', o)
    print('  THE_IDENTITY_CHAIN : block :%s %s' % (o['heading_line'], o))


# ------------------------------------------------------------------------------ THE SCORES, THE DESK, THE COMPONENTS, THE TRAIL
PRIOR_PP = '84adecd'
WRITE_OK = {'FINDINGS.md', 'OPEN_TRAILS.md', 'phase1.5/proofs/THE_RESIDUE_OF_RH.md', 'phase2/method/THE_IDENTITY_CHAIN.md'}
MEMDIR = os.path.join(os.path.expanduser('~'), '.claude', 'projects', 'D--', 'memory')


def w(v):
    return 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')


def scores():
    tj, tg, rj = jl('b550_tiers.json'), jl('b550_tag.json'), jl('b550_reading37.json')
    committed = g(PP, 'log', '-1', '--pretty=%s').startswith('b550 --')
    base = 'HEAD~1' if committed else 'HEAD'
    pref = {}
    for f in sorted(WRITE_OK):
        old = subprocess.run(['git', '-C', PP, 'show', '%s:%s' % (base, f)], capture_output=True).stdout.replace(b'\r\n', b'\n')
        new = open(os.path.join(PP, f), 'rb').read().replace(b'\r\n', b'\n')
        pref[f] = new.startswith(old)
    written = sorted(x for x in g(PP, 'diff', '--name-only', PRIOR_PP).split(NL) if x) if not committed else \
        sorted(x for x in g(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x)
    needle = 'https://' + 'zenodo' + '.org'
    zen = [x for x in os.listdir(T) if x.startswith('b550_') and needle in rd(os.path.join(T, x))]
    tk = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    tok = sum(open(os.path.join(d0, f), 'rb').read().count(tk) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b550_')) if tk else None
    heads = {'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-explicit-formula': '81ae175', 'SIDE-global-section': '2e43315'}
    kernels = {k: g(os.path.join('D:', os.sep, k), 'status', '--porcelain', '--untracked-files=no').strip() == '' and
               g(os.path.join('D:', os.sep, k), 'rev-parse', 'HEAD').startswith(h) for k, h in heads.items()}
    rows = tj.get('rows', [])
    core = [r for r in rows if r['module'].startswith('Core')]
    ll6 = [r for r in rows if r['terminal'].split('.')[-1] in LOCALLIMIT_SIX]
    fii = [r for r in rows if r['terminal'] == 'FiniteInstanceIdentity.finiteInstanceIdentity']
    return dict(
        n1=bool(tg.get('n1')),
        n2=bool(core) and all(r['tier'] == 'T2' for r in core) and len(ll6) == 6 and all(r['tier'] == 'T0' for r in ll6)
        and len(fii) == 1 and fii[0]['tier'] == 'T2' and fii[0]['grade'] == 'ENCODES' and tj['disp_counts'].get('MOVED') == 0,
        n3=bool(tj.get('allprints_equal')),
        n4=bool(rj.get('ok')),
        n5=None,
        n6=all(pref.values()) and not zen and tok == 0 and all(kernels.values()) and set(written) <= WRITE_OK,
        prefixes=pref, written=written, zen=zen, token=tok, kernels=kernels,
        s1=bool(tj.get('iface_equal')) and all(tj['iface_equal'].values()),
        s2=bool(tg.get('remote_main')) and tg['remote_main'].startswith(LV_MAIN),
        s3=len(tj.get('not_in_tag', [])) > 0)


def desk():
    sc = scores()
    N, SS = ('n1', 'n2', 'n3', 'n4', 'n5', 'n6'), ('s1', 's2', 's3')
    tj, tg = jl('b550_tiers.json'), jl('b550_tag.json')
    L = ['=' * 104, 'b550 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '', '### THE NAVIGATOR`S SIX.', '-' * 104,
         '  **(N1)** ### **%s.** -- v0.11.0 at the remote: tag object %s, peeled %s ; local peeled %s.' % (w(sc['n1']), tg['remote_tag'], tg['remote_peeled'], tg['local_peeled']),
         '  **(N2)** ### **%s.** -- tiers %s ; dispositions %s ; the Core shadows all T2, the six LocalLimit theorems T0, finiteInstanceIdentity T2 ENCODES.'
         % (w(sc['n2']), tj['tier_counts'], tj['disp_counts']),
         '  **(N3)** ### **%s.** -- AllPrints at HEAD against AXIOM_PRINTS.txt: equal %s.' % (w(sc['n3']), tj['allprints_equal']),
         '  **(N4)** ### **%s.** -- F = P − PR + A ; file E`s right side adopted as A − PR ; they differ by P (relay data/b550_reading37.txt).' % w(sc['n4']),
         '  **(N5)** ### **%s.** -- SPIRAL_MAP cites no SIDE-global-section pin. Read against the repository`s one tag v0.1.0 instead: %d of the '
         'document-named terminals are absent from its tree -- %s.' % (w(sc['n5']), len(tj['not_in_tag']), ', '.join('%s (first %s)' % tuple(x) for x in tj['not_in_tag'][:8]) + (' ...' if len(tj['not_in_tag']) > 8 else '')),
         '  **(N6)** ### **%s.** -- prefixes kept %s ; files written %s ; tools naming the platform %s ; token %s ; kernels clean %s.'
         % (w(sc['n6']), sc['prefixes'], sc['written'], sc['zen'] or 'NONE', sc['token'], sc['kernels']),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- the interface prints fresh against their bank: %s.' % (w(sc['s1']), tj['iface_equal']),
         '  **(S2)** ### **%s.** -- the remote`s main after the tag push: %s.' % (w(sc['s2']), tg['remote_main']),
         '  **(S3)** ### **%s.** -- document-named terminals absent from v0.1.0`s tree: %d.' % (w(sc['s3']), len(tj['not_in_tag'])),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in N].count(True), [sc[k] for k in N].count(False), [sc[k] for k in N].count(None),
            [sc[k] for k in SS].count(True), [sc[k] for k in SS].count(False)),
         '', '### THIS ACT`S OWN DEFECTS.'] + ([l for l in rd(os.path.join(D, 'b550_defects.txt')).rstrip(NL).split(NL) if l]
                                              if os.path.exists(os.path.join(D, 'b550_defects.txt')) else ['    NONE RECORDED.']) + ['=' * 104]
    put_txt('b550_desk_notes.txt', L)
    put_json('b550_scores.json', sc)
    print(NL.join(L))


def components():
    L = ['=' * 132, 'b550 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '']
    for n in ('b550_tag.txt', 'b550_tiers.txt', 'b550_reading37.txt'):
        L += ['### relay data/%s' % n] + ['  ' + l for l in rd(os.path.join(D, n)).rstrip(NL).split(NL)] + ['']
    for n in ('b550_tag.json', 'b550_pin_lines.json', 'b550_order_lines.json', 'b550_trails.json', 'b550_findings.json', 'b550_identity_block.json'):
        L.append('### %s : %s' % (n, json.dumps(jl(n), ensure_ascii=False)))
    L += ['### THE BRANCHES : see data/b550_branches.txt', '=' * 132]
    put_txt('b550_components.txt', L)
    print(NL.join(L[:6]))


def trail():
    sc, tj, fj, ib, pl, ol, tr = (scores(), jl('b550_tiers.json'), jl('b550_findings.json'), jl('b550_identity_block.json'),
                                  jl('b550_pin_lines.json'), jl('b550_order_lines.json'), jl('b550_trails.json'))
    body = ['', HEADING, '',
            '**(R160) ratified.** (1) The residue terminals’ pin settled and tagged: SIDE-lv-conservation `v0.11.0` at `2f71068`. (2) b546`s '
            '"order" corrected as the navigator`s: two objects under one word. (3) The power-window sweep filed as a work-order with its '
            'trigger, H3 carried unchanged. (4) The Li–Weil bridge`s three consumers entered, with a toolchain-alignment price. (5) '
            'THE_IDENTITY_CHAIN tiered as the cascade`s act six; it stays Tier C. (6) The bench functional read against §37`s cell-level '
            'sign, with its three limits. (7) The stems counted, not listed. (8) THE_KEYSTONE_CENSUS next.', '',
            '**Entered:** THE_RESIDUE_OF_RH.md:%s (the tag line); THE_IDENTITY_CHAIN.md:%s (the tier block, the Tier C line, the pointer); '
            'FINDINGS.md:%s (the b549 pin line), :%s and :%s (the correction and the restatement at :5529), :%s (the reading), :%s (the act); '
            'OPEN_TRAILS.md:%s (W-ORD-POWER-SWEEP) and :%s (the bridge`s consumers at :3548).'
            % (pl['residue_line'], ib['heading_line'], pl['findings_line'], ol['l1'], ol['l2'], fj['reading_line'], fj['act_line'],
               tr['power_line'], tr['bridge_line']), '',
            '**The terminals:** %d at SIDE-global-section HEAD `2e43315`; tiers %s; dispositions %s; AllPrints equal to its bank.'
            % (len(tj['rows']), ' · '.join('%s %d' % kv for kv in tj['tier_counts'].items()), ' · '.join('%s %d' % kv for kv in tj['disp_counts'].items())), '',
            '**CP-1:** open; the cascade continues with THE_KEYSTONE_CENSUS.', '',
            '**Next:** THE_KEYSTONE_CENSUS.', '',
            '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s · (N6) %s.** The seat`s own: (S1) %s, (S2) %s, (S3) %s.'
            % tuple(w(sc[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
            '**No lane opened at this act; one tag made.** Nothing deposits; nothing at Zenodo written; no kernel file edited; no monograph '
            'byte changed; ERRATA untouched; the ceiling unchanged; row U1 unedited; `h2` where the deposit left it; the four lists stay '
            'OPEN; nothing here is a statement about RH or about ζ’s zeros.', '']
    text = poss(NL.join(body))
    if outside_bt(text):
        sys.exit('### UNBALANCED BACKTICKS IN THE TRAIL')
    before = open(OT, 'rb').read()
    if poss(HEADING).encode('utf-8') in before:
        sys.exit('### ALREADY PRESENT')
    open(OT, 'ab').write(text.encode('utf-8'))
    after = open(OT, 'rb').read()
    out = dict(added=len(after) - len(before), prefix=after.startswith(before), headings=after.decode('utf-8').count(poss(HEADING)))
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(headings)d heading' % out)
    put_json('b550_trail_notes.json', out)


if __name__ == '__main__':
    fn = {'reads': reads, 'tag_read': tag_read, 'pin_lines': pin_lines, 'order_lines': order_lines, 'trails': trails, 'tiers': tiers,
          'reading37': reading37, 'findings': findings, 'correction': correction, 'identity_block': identity_block, 'components': components, 'desk': desk, 'trail': trail}
    if len(sys.argv) < 2 or sys.argv[1] not in fn:
        sys.exit('usage: %s %s' % (sys.argv[0], ' | '.join(fn)))
    fn[sys.argv[1]]()
