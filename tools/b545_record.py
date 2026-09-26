# -*- coding: utf-8 -*-
"""b545_record.py -- THE CASCADE, ACT THREE: BALANCE_AND_POSITIVITY TIERED, THE JOINT IN TWO FORMS, ONE EARLIER FINDING
CREDITED, THE FANO THEOREM'S KERNEL STATUS: THE RECORD, UNDER (R155).
### `python tools/b545_record.py reads | anchor | select | tiers | sentences | joint | credit | fano | findings | components | desk | trail`

### BALANCE_AND_POSITIVITY takes appended blocks only (its last byte is kept as the prefix of every write); FINDINGS two appends;
### OPEN_TRAILS one append; THE_UNCONDITIONAL_SURROUND one appended line. TECHNE-Core`s names never leave memory.
### This file deletes nothing.
"""
import hashlib, io, json, os, re, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
FIND, OT = os.path.join(PP, 'FINDINGS.md'), os.path.join(PP, 'OPEN_TRAILS.md')
BAL = os.path.join(PP, 'phase1.5', 'spectral', 'BALANCE_AND_POSITIVITY.md')
MAP = os.path.join(PP, 'phase1.5', 'method', 'THE_LOAD_BEARING_MAP.md')
SURR = os.path.join(PP, 'phase1.5', 'proofs', 'THE_UNCONDITIONAL_SURROUND.md')
FACES = os.path.join(PP, 'FACES_LEDGER.md')
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
SCR = os.environ.get('B545_SCRATCH', '')
PRIV = 'TECHNE-Core'
NL = chr(10)
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


def md5(p):
    return hashlib.md5(open(p, 'rb').read()).hexdigest()


def repo_path(r):
    return os.path.join('D:', os.sep, 'MY-DOwnloads', PRIV) if r == PRIV else os.path.join('D:', os.sep, r)


def g(repo, *a):
    return subprocess.run(['git', '-C', repo_path(repo)] + list(a), capture_output=True, text=True, encoding='utf-8',
                          errors='replace').stdout


def outside_bt(text):
    return sum(l.count('`') % 2 for l in text.split(NL))


def append_to(path, text):
    text = re.sub(r"(?<=[A-Za-z0-9)])`s\b", "'s", text)
    if outside_bt(text):
        sys.exit('### UNBALANCED BACKTICKS IN THE APPEND TO %s' % path)
    before = open(path, 'rb').read()
    add = text.encode('utf-8')
    if not before.endswith(b'\n'):
        add = b'\n' + add
    open(path, 'ab').write(add)
    after = open(path, 'rb').read()
    return dict(file=os.path.relpath(path, PP), before=len(before), added=len(after) - len(before), prefix=after.startswith(before))


# ------------------------------------------------------------------------------ THE READS (pre-seal, declared on the face)
PPREADS = [(BAL, [(21, 27)], 'the Role paragraph -- the purpose statement, printed before any edit'),
           (MAP, [(16, 18), (24, 25), (41, 41), (56, 56), (103, 109), (126, 126), (134, 134), (144, 146), (150, 152)],
            'the map`s BALPOS row, its keystone set, and its appendix'),
           (FIND, [(4955, 4957), (5272, 5276), (5457, 5457)], 'CP-2 and CP-3'),
           (OT, [(3548, 3548), (4698, 4698), (11097, 11097)], 'the Li-to-Weil trail and b544`s CP-3 line'),
           (SURR, [(209, 213)], 'the b539 tier table'),
           (FACES, [(22, 22), (28, 28)], 'the F3 and L1 rows')]
READS = [('SIDE-explicit-formula', 'HEAD', 'SIDEExplicitFormula/RegisterDepth.lean', [(1, 10 ** 6)]),
         ('SIDE-explicit-formula', 'HEAD', 'SIDEExplicitFormula/H2Bridge.lean', [(1, 10 ** 6)]),
         ('SIDE-explicit-formula', 'HEAD', 'SIDEExplicitFormula/Seam.lean', [(1, 10 ** 6)]),
         ('SIDE-explicit-formula', 'HEAD', 'SIDEExplicitFormula/PowerLimit.lean', [(1233, 1244)]),
         ('SIDE-lv-conservation', 'v0.10.0', 'SIDELvConservation/PartialPositivity.lean', [(1, 10 ** 6)]),
         ('SIDE-lv-conservation', 'v0.10.0', 'SIDELvConservation/C7FiniteTypeFalse.lean', [(68, 72)]),
         ('SIDE-lv-conservation', 'v0.10.0', 'SIDELvConservation/DirichletC7Order.lean', [(771, 776)]),
         ('SIDE-lv-conservation', 'v0.10.0', 'SIDELvConservation/CouplingsAtPhi.lean', [(60, 200), (197, 200), (205, 207), (222, 224),
                                                                                     (243, 245), (262, 264), (277, 279), (298, 300),
                                                                                     (315, 317), (362, 364), (405, 430)]),
         ('SIDE-lv-conservation', 'v0.10.0', 'SIDELvConservation/T3_StepNineBridge.lean', [(44, 70)]),
         ('SIDE-li-map', '73cee42', 'LiLinearMap.lean', [(50, 80)]),
         ('SIDE-kernel', '691295b', 'Kernel/Voice7Witness.lean', [(128, 150)])]


def reads():
    L = ['b545 -- THE ORDERED READS, CITED BY PATH AND LINE', '']
    b = rd(BAL).split(NL)
    L.append('### BALANCE_AND_POSITIVITY.md : %d lines ; md5 %s ; headings:' % (len(b) - (1 if b[-1] == '' else 0), md5(BAL)))
    L += ['  :%d %s' % (i + 1, l[:160]) for i, l in enumerate(b) if l.startswith('#') or l.startswith('<!--')]
    for p, spans, what in PPREADS:
        t = rd(p).split(NL)
        L.append('')
        L.append('### %s -- %s' % (os.path.relpath(p, PP).replace(os.sep, '/'), what))
        for a, z in spans:
            L += ['  :%d %s' % (i + 1, t[i][:600]) for i in range(a - 1, min(z, len(t)))]
    for repo, pin, path, spans in READS:
        t = g(repo, 'show', '%s:%s' % (pin, path)).replace(chr(13), '').split(NL)
        for a, z in spans:
            z = min(z, len(t))
            L += ['', '### %s %s (%s) %s:%d-%d' % (repo, g(repo, 'rev-parse', '--short', pin + '^{commit}').strip(), pin, path, a, z)]
            L += ['  :%d %s' % (i + 1, t[i]) for i in range(a - 1, z)]
    sj = jl('b539_sentences.json')
    L += ['', '### relay data/b539_sentences.json -- lv-conservation`s deposited description, as b539 banked it']
    for r in sj['selected']:
        if r['block'].startswith('lv'):
            L.append('  [%s] %s -- %s :: "%s"' % (r['grade'], r['block'], r['where'], r['sentence']))
    put_txt('b545_reads.txt', L)
    print('  reads banked : %d lines' % len(L))


ANCHOR = ['SIDEExplicitFormula.B321.h2_sign_iff_rh', 'SIDEExplicitFormula.B321.h2_sign_iff_rh_strip', 'SIDEExplicitFormula.B321.ch_iff_rh',
          'SIDEExplicitFormula.RegisterDepth.not_register1', 'SIDEExplicitFormula.RegisterDepth.register5_output_holds',
          'SIDEExplicitFormula.RegisterDepth.lvh2_corrected_iff', 'SIDEExplicitFormula.RegisterDepth.lv_h2_false_on_strip',
          'SIDEExplicitFormula.RegisterDepth.mellin_Phi_eq_zero_of_re_le_one']


def anchor():
    src = ['import SIDEExplicitFormula.RegisterDepth', 'import SIDEExplicitFormula.Seam', ''] + ['#check @' + n for n in ANCHOR]
    p = os.path.join(SCR, 'b545_anchor_check.lean')
    io.open(p, 'w', encoding='utf-8', newline=NL).write(NL.join(src) + NL)
    head = g('SIDE-explicit-formula', 'rev-parse', 'HEAD').strip()
    dirty = g('SIDE-explicit-formula', 'status', '--porcelain').strip()
    r = subprocess.run(['lake', 'env', 'lean', p], cwd=KER, capture_output=True, text=True, encoding='utf-8', errors='replace')
    out = (r.stdout + r.stderr).replace(chr(13), '')
    L = ['b545 -- THE RH-ANCHOR, FRESH #check at SIDE-explicit-formula %s (tree %s; exit %d)' % (head, 'clean' if not dirty else 'DIRTY', r.returncode)]
    L += ['  ' + l for l in out.split(NL) if l.strip()]
    put_txt('b545_anchor.txt', L)
    print(NL.join(L))


# ------------------------------------------------------------------------------ THE SENTENCE SELECTION (the needles of (R155)(2))
PAT = [('h2', r'(?<![A-Za-z0-9_])h2(?![A-Za-z0-9_])'),
       ('registers', r'(?i)register'),
       ('pentagon', r'(?i)pentagon'),
       ('Route 3', r'Route 3|Route-3|ConservationHypothesis|ConservationBridge'),
       ('goal state', r'(?i)goal[ -]state|goalState|goal ⇐'),
       ('the open clause', r'(?i)open clause|the clause'),
       ('the joint', r'(?i)(?<![A-Za-z])joint(?![A-Za-z])'),
       ('a named terminal', None)]


def terminal_names():
    """### the federation`s theorem names (b544`s enumeration at b542`s pins, lv at v0.10.0) plus li-map at 73cee42 -- last component"""
    d = jl('b544_decls.json')
    names = {x.get('full', x.get('name', '')).split('.')[-1] for x in d['decls'] if x.get('kw') in ('theorem', 'lemma') and x['repo'] != PRIV}
    t = g('SIDE-li-map', 'show', '73cee42:LiLinearMap.lean')
    names |= set(re.findall(r'(?m)^theorem\s+([A-Za-z0-9_\']+)', t))
    return names


def segs(lines):
    out, cur, start, code = [], [], None, False
    for i, l in enumerate(lines, 1):
        if l.strip().startswith('```'):
            if cur:
                out.append((start, ' '.join(cur)))
            cur, start, code = [], None, not code
            continue
        if code:
            continue
        if re.match(r'^\s*(- |\d+\. |#|>|<!--)', l) or not l.strip() or l.startswith('|'):
            if cur:
                out.append((start, ' '.join(cur)))
            cur, start = [], None
            if l.startswith('|') or re.match(r'^\s*(- |\d+\. |#|>)', l):
                out.append((i, l.strip()))
            continue
        if start is None:
            start = i
        cur.append(l.strip())
    if cur:
        out.append((start, ' '.join(cur)))
    return out


def split_rows(lines):
    names = terminal_names()
    rows = []
    for ln, seg in segs(lines):
        if re.match(r'^\|[\s:|-]+\|$', seg):
            continue
        parts = [seg] if seg.startswith('|') else [p for p in re.split(r'(?<=[.!?])\s+(?=[A-Z*`(\[])', ' '.join(seg.split())) if p.strip()]
        for s in parts:
            hits = [n for n, p in PAT if p and re.search(p, s)]
            named = sorted({m for m in re.findall(r'`([^`]+)`', s) for m in [m.split('.')[-1].split('{')[0].strip()] if m in names})
            if named:
                hits.append('a named terminal')
            rows.append(dict(line=ln, sentence=s, hits=hits, terminals=named))
    return rows


def select():
    rows = split_rows(rd(BAL).split(NL))
    sel = [r for r in rows if r['hits']]
    yields = {n: sum(1 for r in rows if n in r['hits']) for n, _ in PAT}
    for n, v in yields.items():
        print('  matcher %-17s yield %d' % (n, v))
    print('  sentences read %d ; selected %d' % (len(rows), len(sel)))
    for r in sel:
        print('  :%-4d %-40s %s' % (r['line'], ','.join(h.replace('a named terminal', 'T') for h in r['hits'])[:40], r['sentence'][:150]))


# ------------------------------------------------------------------------------ COMPONENT 5: THE FANO SEARCH (READING (10))
FANO_NEEDLES = [('Fano', r'Fano'), ('PG(2,2)', r'PG\(2, ?2\)|PG22'), ('triple', r'(?i)triple'),
                ('line with Fin 7', None), ('secondMoment', r'(?i)second_?moment'), ('2-(7,3,1) design', r'(?i)2-\(7, ?3, ?1\)|\bdesign\b')]
B542_PINS = {}


def fed_repos():
    """### every git repository D:/SIDE-* (READING (10)), with TECHNE-Core"""
    base = os.path.join('D:', os.sep)
    out = sorted(d for d in os.listdir(base) if d.startswith('SIDE-') and os.path.isdir(os.path.join(base, d))
                 and subprocess.run(['git', '-C', os.path.join(base, d), 'rev-parse', '--git-dir'], capture_output=True).returncode == 0)
    return out + [PRIV]


def fano():
    d = jl('b544_decls.json')
    for x in d['decls']:
        B542_PINS.setdefault(x['repo'], x['pin'])
    repos = fed_repos()
    in542 = [r for r in repos if r in B542_PINS]
    L = ['b545 -- THE FANO SEARCH (READING (10)): %d repositories (%d in b542`s enumeration, %d outside it: %s)' % (
        len(repos), len(in542), len(repos) - len(in542), ', '.join(r for r in repos if r not in B542_PINS))]
    L.append('  needles: ' + ' ; '.join(n for n, _ in FANO_NEEDLES))
    hits, revs_read, files_read = [], 0, 0
    for r in repos:
        revs = ['HEAD'] + [t for t in g(r, 'tag').split() if t]
        if B542_PINS.get(r) and B542_PINS[r] not in revs:
            revs.append(B542_PINS[r])
        seen = set()
        for rev in revs:
            sha = g(r, 'rev-parse', '--short', rev + '^{commit}').strip()
            if not sha:
                continue
            revs_read += 1
            files = [f for f in g(r, 'ls-tree', '-r', '--name-only', sha).split(NL) if f.endswith('.lean')]
            files_read += len(files)
            out = g(r, 'grep', '-n', '-I', '-E', '-i', r'fano|pg\(2, ?2\)|pg22|triple|second_?moment|2-\(7, ?3, ?1\)|design|fin 7', sha, '--', '*.lean')
            for ln in out.replace(chr(13), '').split(NL):
                m = re.match(r'^[0-9a-f]+:(.+?):(\d+):(.*)$', ln)
                if not m:
                    continue
                f, n, text = m.group(1), int(m.group(2)), m.group(3)
                which = [k for k, p in FANO_NEEDLES if p and re.search(p, text)]
                if re.search(r'Fin 7', text) and re.search(r'(?i)\bline', text):
                    which.append('line with Fin 7')
                if not which:
                    continue
                key = (f, text.strip())
                if key in seen:
                    continue
                seen.add(key)
                hits.append(dict(repo=r, rev=rev, sha=sha, file=f, line=n, needles=which,
                                 text=('(private: module and shape only)' if r == PRIV else text.strip()[:240])))
    by_repo = {}
    for h in hits:
        by_repo[h['repo']] = by_repo.get(h['repo'], 0) + 1
    L.append('  revisions read %d ; .lean files read %d ; hits (distinct file+text per repository) %d' % (revs_read, files_read, len(hits)))
    for r, n in sorted(by_repo.items()):
        L.append('  %-36s %d' % (r, n))
    for h in hits:
        L.append('  %s %s (%s) %s:%d [%s] %s' % (h['repo'], h['rev'], h['sha'], h['file'], h['line'], ','.join(h['needles']), h['text']))
    put_json('b545_fano_hits.json', dict(repos=repos, outside_b542=[r for r in repos if r not in B542_PINS], revisions=revs_read,
                                         files=files_read, hits=hits, by_repo=by_repo))
    put_txt('b545_fano_search.txt', L)
    print(NL.join(L[:3 + len(by_repo) + 1]))
    print('  (every hit in relay data/b545_fano_search.txt)')


# ------------------------------------------------------------------------------ READINGS (10) AND (12): THE VANILLA PROBES
TOOLCHAIN = 'leanprover/lean4:v4.29.0-rc8'
PROBES = [('SIDE-li-map', '73cee42', 'LiLinearMap.lean', ['LiLinearMap.lam_add', 'LiLinearMap.lam_one']),
          ('SIDE-fano-darkness', '0f6ce5b', 'FanoTwoDarkness.lean',
           ['FanoTwoDarkness.second_moment', 'FanoTwoDarkness.first_moment', 'FanoTwoDarkness.point_line_count',
            'FanoTwoDarkness.pair_line_count', 'FanoTwoDarkness.point_triple_count', 'FanoTwoDarkness.pair_triple_count',
            'FanoTwoDarkness.frequency_match', 'FanoTwoDarkness.counts', 'FanoTwoDarkness.lines_are_triples'])]


def probe():
    """### the file at its pin, fed to `lean --stdin` with `#print axioms` and `#check` appended -- no file is written"""
    L, res = ['b545 -- THE VANILLA PROBES (READINGS (10) AND (12)): each file at its pin fed to `lean +%s --stdin`' % TOOLCHAIN], {}
    for repo, pin, path, names in PROBES:
        full = g(repo, 'rev-parse', pin + '^{commit}').strip()
        tc = g(repo, 'show', '%s:lean-toolchain' % pin).strip()
        src = g(repo, 'show', '%s:%s' % (pin, path)).replace(chr(13), '')
        src += NL + NL.join(['#print axioms ' + n for n in names] + ['#check @' + n for n in names]) + NL
        r = subprocess.run(['lean', '+' + TOOLCHAIN, '--stdin'], input=src, capture_output=True, text=True, encoding='utf-8', errors='replace')
        out = (r.stdout + r.stderr).replace(chr(13), '')
        L += ['', '### %s %s (%s) %s ; its toolchain file: %s ; exit %d' % (repo, pin, full, path, tc, r.returncode)]
        L += ['  ' + l for l in out.split(NL) if l.strip()]
        prof = {}
        for n in names:
            m = re.search(r"'%s' (depends on axioms: \[[^\]]*\]|does not depend on any axioms)" % re.escape(n), out)
            prof[n] = m.group(1) if m else None
        res[repo] = dict(pin=pin, full=full, exit=r.returncode, profiles=prof, toolchain=tc)
    put_json('b545_probes.json', res)
    put_txt('b545_probes.txt', L)
    print(NL.join(L))


# ------------------------------------------------------------------------------ COMPONENT 1: B.5 TIERED (READING (1))
MAPL = 'THE_LOAD_BEARING_MAP.md'
LV, SK, LI, FD = 'SIDE-lv-conservation', 'SIDE-kernel', 'SIDE-li-map', 'SIDE-fano-darkness'
NA = 'T0, not RH-anchor: '
# ### (repo, the row`s pin, the pin re-read beside it, full name, kind, grade kept, tier, reason, earlier (tier, source) or None,
# ###  the profile`s source where b544`s probe banks carry none)
B5 = [
    (343, 'SIDE-li-map (Li linear map, `lam_add`; = pentagon R4_channelDecomposition)', 'T2', [
        (LI, '73cee42', 'HEAD', 'LiLinearMap.lam_add', 'theorem', 'DERIVES', 'T2',
         'linearity of the Li map over `Nat → Int` streams; the reading as λ_A + λ_Z of log ξ is manuscript-resident (the file`s own header)',
         ('T2', 'relay data/b540_tiers.json, PATHS :139'), 'fresh, relay data/b545_probes.txt'),
        (LV, '2d86182', 'v0.10.0', 'SIDELvConservation.RegisterPentagon.R4_channelDecomposition', 'theorem', 'DERIVES (the pentagon`s edge)', 'T2',
         'INTERFACES on its own hypothesis `lam_additive` over an arbitrary `lam`: the additivity is assumed there, not imported from SIDE-li-map; STRUCTURE',
         None, 'not probed (b544 probed ZETA terminals; subject PROGRAMME-TYPE)')]),
    (344, 'SIDE-lv-conservation (T1/T2/T3 bracket)', 'T2', [
        (LV, 'c8e3d31', 'v0.10.0', 'SIDELvConservation.completedRiemannZeta_eq_mellinPhi', 'theorem', 'DERIVES', 'T0',
         NA + '`completedRiemannZeta s = mellin Phi (s / 2)` for 1 < re s -- Mathlib`s objects, `Phi` built from Mathlib`s `evenKernel`; says nothing about where the zeros are',
         ('T0', 'relay data/b544_t0.json (CP-2, PREMISE-FREE)'), None),
        (LV, 'c8e3d31', 'v0.10.0', 'SIDELvConservation.T3.T3prime_shared_witness', 'theorem', 'INTERFACES on h1, h2', 'T2',
         'its hypothesis h2 is lv`s h2, `mellin Phi (s / 2) ≠ 0`, false at every s with re s ≤ 1 (`lv_h2_false_on_strip`)',
         ('T2', 'relay data/b540_tiers.json, PATHS :293 (the bracket)'), None),
        (LV, 'c8e3d31', 'v0.10.0', 'SIDELvConservation.T3.T3doubleprime_general_commutation_fails', 'theorem', 'DERIVES (a countermodel)', 'T2',
         'logic over abstract couplings: the unrestricted ∀∃ ⟹ ∃∀ fails at s = 3',
         ('T2', 'relay data/b540_tiers.json, PATHS :293 (the bracket)'), 'not probed (b544 probed ZETA terminals)'),
        (LV, 'c8e3d31', 'v0.10.0', 'SIDELvConservation.T3.T3_perClass_to_combinations', 'theorem', 'OPEN (one `sorry`, disclosed)', 'T2',
         'logic over abstract couplings; the pin carries its one `sorry` (T3_StepNineBridge.lean:108 at v0.10.0)',
         ('T2', 'relay data/b540_tiers.json, PATHS :293 (the bracket)'), 'not probed; it carries `sorryAx` by its own `sorry`')]),
    (345, 'SIDE-lv-conservation (ARM-2 instruments)', 'T2', [
        (LV, 'c80bdc2', 'v0.10.0', 'SIDELvConservation.h1_complete_at_Phi', 'theorem', 'DERIVES', 'T0',
         NA + 'the eight coupling facts of Mathlib`s theta-kernel function `Phi`; nothing about where the zeros are, and h1 ∧ h2 at `Phi` holds at no s of the strip',
         ('T0', MAPL + ':103 (b539)'), 'SURR Correspondence :184, as the map cites it'),
        (LV, '2d86182', 'v0.10.0', 'RegisterPentagon (module)', 'module', 'STRUCTURE (R3 edge NOT-COMPILED)', 'T2',
         'its faces include R1 FALSE-AS-STATED, R5-output a theorem and `goalState_sevenClasses_of_h2`, vacuous on the strip (b538)',
         ('T2', MAPL + ':104 (b539)'), 'SURR Correspondence :185, as the map cites it'),
        (LV, '6efa9e5', 'v0.10.0', 'SIDELvConservation.PartialPositivity.partialPositivity_finiteRange', 'theorem', 'INTERFACES (3 named)', 'T1-lit',
         'INTERFACES on `ExplicitFormulaDecomp` and `TailBoundPremise` (literature, not compiled) and the numerical `VerifiedZerosTo T`; B.5`s cell groups it with v0.5.0 = 1767bd6, where the module does not exist -- it is at v0.8.0 = 6efa9e5',
         ('T1-lit', MAPL + ':144 (b540)'), 'SURR Correspondence :187, as the map cites it'),
        (LV, '6efa9e5', 'v0.10.0', 'SIDELvConservation.PartialPositivity.blTerm_nonneg_of_onLine', 'lemma', 'DERIVES', 'T0',
         NA + 'for a zero of Mathlib`s `riemannZeta` with re = 1/2, `0 ≤ (1 - (1 - 1/ρ)^n).re`; nothing about where the zeros are',
         ('T0', MAPL + ':109 (b539)'), 'SURR Correspondence :186, as the map cites it'),
        (LV, '1767bd6', 'v0.10.0', 'SIDELvConservation.exists_norm_completedLFunction_le_exp', 'theorem', 'DERIVES', 'T0',
         NA + 'the order-≤1 growth of Mathlib`s `completedLFunction`, no premise but `χ ≠ 1`',
         ('T0', MAPL + ':113 (b539)'), 'SURR Correspondence :188, as the map cites it'),
        (LV, 'bc4751e', 'v0.10.0', 'SIDELvConservation.C7_finite_type_false', 'theorem', 'DERIVES', 'T0',
         NA + '`¬ ∃ C A, ∀ s, ‖completedRiemannZeta₀ s‖ ≤ C * exp (A * ‖s‖)`; nothing about where the zeros are',
         ('T0', MAPL + ':107 (b539)'), None)]),
    (346, 'SIDE-kernel (route terminals, `ConservationHypothesis`)', 'T2', [
        (SK, 'v1.2', 'v1.5', 'ConservationBridge.riemann_hypothesis', 'theorem', 'INTERFACES on `ConservationHypothesis`', 'T2',
         'its premise is RH restated (`ch_iff_rh`), EQUIVALENT-REWORDING under (R151)(2): ENCODES-CONCLUSION',
         ('T2', MAPL + ':115 (b539), (R151)(2) at :152 (b541)'), 'relay data/b532_profile_log.txt, as the map cites it'),
        (SK, 'v1.2', 'v1.5', 'structural_exhaustiveness_proved', 'theorem', 'DERIVES', 'T2',
         'its catalogue conjunct is `Fintype.card MechanismClass = 7` by `decide` (E-2026-09-14-1) and C₇ is a disclosed stand-in',
         ('T2', MAPL + ':122 (b539)'), 'not probed (b544: subject PROGRAMME-TYPE)'),
        (SK, 'v1.2', 'v1.5', 'SpectralCannonFull.spectral_cannon', 'theorem', 'DERIVES', 'T0',
         NA + '`(deriv completedRiemannZeta₀ ⟨1/2, t⟩).re = 0`, a fact about the line',
         ('T0', MAPL + ':112 (b539)'), None)]),
    (347, 'Monograph Ch. 15 §15.2 (the seven classes)', 'T4', [
        ('', '', '', 'day1/A_Place_to_Stand.md Chapter 15 (manuscript v5.8 / Zenodo v1.1.1)', 'manuscript', 'read 2026-07-13', 'T4',
         'the row pins the chapter`s text as the source of the seven classes: manuscript-resident, no terminal. b541 tiered the chapter`s own claim (exhaustive by Ostrowski, Route 1`s terminal) T2; this row names no terminal',
         ('T2', 'FINDINGS.md:4865 (b541`s chapter tier map, Chapter 15)'), None)]),
    (348, 'Li channel computation', 'T3', [
        ('', '', '', 'internal/bench/li_bench.py (dps 260, M 4096, r ∈ {0.85, 0.75}, n ≤ 130)', 'script', 'two-radius agreement ≥ 215 digits', 'T3',
         'numerical, verified by two-radius agreement; its bank the script (C.2`s extension, li_bench300.py, to n = 300)', None, None)]),
]
FANO_ROW = (FD, '0f6ce5b', '0f6ce5b', 'FanoTwoDarkness.second_moment', 'theorem', 'DERIVES', 'T0',
            'the second-moment identity for integer point values, `4 · Σ_lines (sum)² = Σ_non-lines (sum)²` over the seven lines and the twenty-eight non-line triples (the triples read by hand: exactly the 7 and the 28); with `first_moment`, `point_line_count`, `pair_line_count`, `point_triple_count`, `pair_triple_count`. §V states real values; the real-valued form follows from the integer polynomial identity and is not compiled',
            None, 'fresh, relay data/b545_probes.txt')
RANK = ['T0', 'T1-open', 'T1-lit', 'T2', 'T3', 'T4']


HINT = {'structural_exhaustiveness_proved': 'Bridge/TheBridgeComplete.lean'}   # Route 1`s terminal, premise-free (not ConservationBridge`s)


def decl_text(repo, rev, full, kind):
    """### the declaration`s statement at a revision: from its keyword line to the first `:=`, whitespace collapsed"""
    short = full.split('.')[-1]
    out = g(repo, 'grep', '-n', '-E', r'^(theorem|lemma) %s\b' % re.escape(short), rev, '--', HINT.get(full, '*.lean')).replace(chr(13), '')
    hits = [l for l in out.split(NL) if l.strip()]
    if not hits:
        return None, None
    m = re.match(r'^[^:]+:(.+?):(\d+):', hits[0])
    f, n = m.group(1), int(m.group(2))
    t = g(repo, 'show', '%s:%s' % (rev, f)).replace(chr(13), '').split(NL)
    buf = []
    for l in t[n - 1:n + 40]:
        buf.append(l)
        if ':=' in l:
            break
    s = ' '.join(' '.join(buf).split())
    return '%s:%d' % (f, n), s.split(':=')[0].strip()


def module_blob(repo, rev, path):
    return g(repo, 'rev-parse', '%s:%s' % (rev, path)).strip()


def ei_of(full):
    idx = jl('b544_index.json')['rows']
    hit = [r for r in idx if r['full'] == full]
    if hit:
        return '%s (%s)' % (hit[0]['mark'], hit[0]['shape'])
    dec = [x for x in jl('b544_decls.json')['decls'] if x.get('full') == full]
    return 'not indexed (b544 subject %s)' % dec[0]['subject'] if dec else 'not indexed (not in b542`s enumeration)'


def profile_of(repo, full, src):
    if repo in (LI, FD):
        return (jl('b545_probes.json').get(repo, {}).get('profiles', {}) or {}).get(full) or '--'
    p = os.path.join(D, 'b544_probe_%s.json' % repo)
    if os.path.exists(p):
        pr = jl('b544_probe_%s.json' % repo)['profiles']
        if full in pr:
            return pr[full] + ' (b544 probe bank)'
    return src or '--'


def reread(term):
    repo, rp, cp, full, kind, grade, tier, reason, earlier, psrc = term
    if kind in ('manuscript', 'script'):
        return dict(where_row='--', where_now='--', same='--', statement='--')
    if kind == 'module':
        a, b = module_blob(repo, rp, 'SIDELvConservation/RegisterPentagon.lean'), module_blob(repo, cp, 'SIDELvConservation/RegisterPentagon.lean')
        return dict(where_row='RegisterPentagon.lean blob %s' % a[:10], where_now='blob %s' % b[:10],
                    same='SAME FILE' if a == b else 'FILE CHANGED', statement='(a module: its faces and edges)')
    w1, s1 = decl_text(repo, rp, full, kind)
    w2, s2 = decl_text(repo, cp, full, kind)
    return dict(where_row=w1 or 'ABSENT', where_now=w2 or 'ABSENT', same=('SAME' if s1 == s2 else 'DIFFERENT') if s1 and s2 else 'ABSENT AT ONE PIN',
                statement=s2 or s1 or '--')


def tiers():
    fano_hits = jl('b545_fano_hits.json')
    compiled = bool(jl('b545_probes.json').get(FD, {}).get('profiles', {}).get(FANO_ROW[3]))
    rows, L = [], ['b545 -- COMPONENT 1: B.5 (BALANCE_AND_POSITIVITY.md:339-348) TIERED, ROW FOR ROW; each terminal re-read at its pin']
    b = rd(BAL).split(NL)
    for line, obj, rtier, terms in B5:
        L.append('')
        L.append('### :%d %s' % (line, b[line - 1][:150]))
        out = []
        for t in terms:
            repo, rp, cp, full, kind, grade, tier, reason, earlier, psrc = t
            rr = reread(t)
            if earlier is None:
                cm = 'NEW'
            else:
                cm = 'CARRIED' if earlier[0] == tier else 'MOVED (%s -> %s)' % (earlier[0], tier)
            row = dict(line=line, object=obj, repo=repo, row_pin=rp, now_pin=cp, terminal=full, kind=kind, grade=grade, tier=tier,
                       reason=reason, earlier=earlier, carried=cm, ei=(ei_of(full) if repo else '--'), profile=(profile_of(repo, full, psrc) if repo else '--'),
                       **rr)
            out.append(row)
            L.append('  %-70s %s@%s / %s  %s  %s | %s | %s | E/I %s' % (full[:70], repo, rp, cp, rr['same'], tier, cm, row['profile'][:60], row['ei']))
            L.append('      statement: %s' % row['statement'][:300])
        low = max(out, key=lambda r: RANK.index(r['tier']))['tier']
        if low != rtier:
            sys.exit('### ROW :%d -- TYPED TIER %s, LOWEST OF ITS TERMINALS %s' % (line, rtier, low))
        rows.append(dict(line=line, object=obj, tier=rtier, terminals=out))
    fano = None
    if compiled:
        rr = reread(FANO_ROW)
        pr = jl('b545_probes.json')[FD]['profiles']
        fano = dict(terminal=FANO_ROW[3], repo=FD, pin=FANO_ROW[1], full_sha=jl('b545_probes.json')[FD]['full'], tier='T0', grade='DERIVES',
                    reason=FANO_ROW[7], carried='NEW', ei=ei_of(FANO_ROW[3]), profiles=pr, **rr)
        L += ['', '### THE FANO CORRESPONDENCE ROW (READING (10), COMPILED): %s at %s -- %s' % (FANO_ROW[3], FD, rr['same'])]
        L += ['  %-45s %s' % (k, v) for k, v in pr.items()]
    terms = [t for r in rows for t in r['terminals']]
    counts = dict(rows={k: sum(1 for r in rows if r['tier'] == k) for k in RANK},
                  terminals={k: sum(1 for t in terms if t['tier'] == k) for k in RANK},
                  carried={k: sum(1 for t in terms if t['carried'].split(' ')[0] == k) for k in ('CARRIED', 'MOVED', 'NEW')},
                  same={k: sum(1 for t in terms if t['same'] == k) for k in ('SAME', 'DIFFERENT', 'SAME FILE', 'FILE CHANGED', 'ABSENT AT ONE PIN', '--')})
    put_json('b545_tiers.json', dict(table='BALANCE_AND_POSITIVITY.md:339-348', rows=rows, fano=fano, counts=counts,
                                     fano_compiled=compiled, fano_hits=len(fano_hits.get('hits', []))))
    L += ['', '  counts: %s' % json.dumps(counts, ensure_ascii=False)]
    put_txt('b545_tiers.txt', L)
    print(NL.join(L))


# ------------------------------------------------------------------------------ COMPONENT 2: THE SENTENCE READ (READINGS (3)-(6))
E1, E3, E6, E914 = 'E-2026-09-25-1', 'E-2026-09-25-3', 'E-2026-09-25-6', 'E-2026-09-14-1'
S, H, R = 'STANDS', 'STANDS-AS-HISTORY', 'RESTS'
ANCHOR_SHORT = [n.split('.')[-1] for n in ANCHOR]
DEPTHS = ('the registers stand at four depths (b538): R1, stated for every essential interface, is false (`not_register1`); R2 is RH '
          'restated (`ch_iff_rh`); R3 is undecided (FINDINGS.md:4787); R4, in its Weil form, is equivalent to RH (`h2_sign_iff_rh`); '
          'R5`s compiled output face holds outright (`register5_output_holds`) -- SIDE-explicit-formula 81ae175')
PIN = 'SIDE-explicit-formula `81ae175`'
# ### (line, key, clause, verdict, tier, grounds, reason, rectification, flag) -- the key is a substring of exactly one selected sentence
SGR = [
    (21, 'That distance **is** the open clause', '', S, 'T1-lit', '', 'the Li form of the joint: Li`s criterion under the channel split, a literature theorem (Bombieri–Lagarias 1999; Appendix C.3, C.7); `R4_positivity_to_RH` INTERFACES on it', '', ''),
    (21, 'The complete argument is the monograph', '', S, 'T1-open', '', 'the clause is open: in its Weil form it is `h2_sign`, equivalent to RH (`h2_sign_iff_rh`) and not proved', '', ''),
    (23, '*Kernel currency (2026-07-24 deposit)', '', H, 'T2', '', 'a dated currency note, accurate to its date and since: the six named terminals are SAME at v0.10.0 (this act`s tier table); the lowest tier among them is T2 (`RegisterPentagon`)', '', ''),
    (23, 'The all-n tail of the clause remains the open gap', '', S, 'T1-lit', '', 'the certificate covers n ≤ N₀(T); the all-n statement is the Li form, T1-lit and open', '', ''),
    (25, '**Sign-layer map.**', '', S, 'T4', '', 'a pointer to PATHS §ANNEX B; the B3 boundary is classical (de la Vallée Poussin)', '', ''),
    (25, 'The clause\'s ingredient is two-altitude', '', S, 'T2', '', '`lam_nonneg_of_nonneg` (SIDE-li-map b515e6b, PrimeLedgerPositivity.lean:68) is stream-level over integers; the sentence calls it a shadow', '', ''),
    (68, 'One half of that residue is now settled in-kernel', '', S, 'T0', '', NA + '`blTerm_nonneg_of_onLine` states the Li term`s sign for a zero already on the line', '', ''),
    (72, 'The universality hypothesis carried by silence_universal', 'the registers clause', R, 'T2', E3 + ', ' + E6, DEPTHS + '; they are not four registers of one open joint',
     'The universality hypothesis carried by silence_universal, the named ConservationHypothesis of the kernel\'s Route 3, the one premise of the reduction analysis, and the balance→positivity distance identified here stand at different depths, and with the C₅ input/output distance of §D.2 they are five: the first, stated for every essential interface, is false (`not_register1`); the second is RH restated (`ch_iff_rh`); the third is undecided (FINDINGS.md:4787); the fourth, in its Weil form, is equivalent to RH (`h2_sign_iff_rh`); the fifth\'s compiled output face holds outright (`register5_output_holds`) -- all at ' + PIN + ', `h2_sign_iff_rh` also at v0.2 = `5c72cad`.', ''),
    (72, 'The universality hypothesis carried by silence_universal', 'the Route 3 clause', R, 'T2', E1, '`ConservationHypothesis` is RH restated (`ch_iff_rh`); Route 3 formalizes RH ⇒ RH, its terminal ENCODES-CONCLUSION (T2)',
     'The named ConservationHypothesis of the kernel\'s Route 3 is RH restated (`ch_iff_rh`, ' + PIN + '), so Route 3 formalizes RH ⇒ RH; as a register it is RH itself, by a rewording lemma.', ''),
    (72, 'Those five are now a single compiled object', '', R, 'T2', E6, '`RegisterPentagon` compiles five faces as Prop definitions with graded edges; ' + DEPTHS,
     '`RegisterPentagon` (SIDE-lv-conservation `v0.7.0` = `2d86182`, carried to `v0.10.0`) carries the five faces (R1 universality, R2 conservation, R3 totality-through-places, R4 positivity, R5 input/output) with the goal-state Prop and graded edges, and the faces stand at different depths -- R1 false as stated (`not_register1`), R2 RH restated (`ch_iff_rh`), R3 undecided, R4 in its Weil form equivalent to RH (`h2_sign_iff_rh`), R5\'s output face a theorem (`register5_output_holds`), at ' + PIN + '; the cross-register equivalences are not compiled, and the one equivalence to RH the corpus compiles is the Weil form\'s.', ''),
    (72, 'This paper\'s home is the **R4 positivity face**', '', 'COND-LAM', 'T2', '', '', '', 'READING (12)'),
    (72, 'On the present bench the joint takes its sharpest form', '', S, 'T1-lit', '', 'the Li form of the joint, a classical statement: Li`s criterion under the channel split (R155)(3)', '', ''),
    (72, 'The joint is one inequality between two exactly computable channels', '', S, 'T1-lit', '', 'the Li form; the two channels are computed on the bench', '', ''),
    (99, 'Nothing in these measurements is new', '', S, 'T3', '', 'numerical channel values at two radii; Keiper`s priority stated', '', ''),
    (109, 'The archimedean-channel input for each', '', S, 'T0', '', NA + '`exists_norm_completedLFunction_le_exp` bounds the growth of Mathlib`s `completedLFunction`', '', ''),
    (131, 'The catalogue\'s exhaustiveness over place-indexed structures is certified', '', R, 'T4', E914 + ', ' + E6,
     'the catalogue`s certified exhaustiveness is a `decide` count (`structural_exhaustiveness_proved`, E-2026-09-14-1); the factoring through the places is R3, undecided (FINDINGS.md:4787), and the registers stand at different depths',
     'The catalogue\'s exhaustiveness over place-indexed structures is certified as a count (`structural_exhaustiveness_proved`: `Fintype.card MechanismClass = 7` by `decide`, E-2026-09-14-1); that every zero-sourcing mechanism factors through the places, and that place-level exclusion reflects to mechanism level, is the third register, which b538\'s census records undecided (FINDINGS.md:4787) -- the registers stand at different depths (`not_register1`, `ch_iff_rh`, `h2_sign_iff_rh`, `register5_output_holds`, ' + PIN + ') -- and this note\'s contribution is to have given the fourth, the balance→positivity distance, a bench, a measured shape, and a name.', ''),
    (146, 'The premise, in the four registers established in §IV', '', R, 'T2', E1 + ', ' + E6, DEPTHS + '; the registers paragraph is at §II (:72), not §IV',
     'The premise`s neighbourhood, in the registers of §II (:72), which stand at different depths: the universality hypothesis of `silence_universal`, false in its universal form (`not_register1`); Route 3\'s `ConservationHypothesis`, RH restated (`ch_iff_rh`); the one premise of the reduction analysis; the balance→positivity distance, whose Weil form is equivalent to RH (`h2_sign_iff_rh`) -- ' + PIN + '.', ''),
    (150, 'Profiles (`#print axioms`, pin `73cee42`', '', H, 'T2', '', 'the dated profile record (2026-07-13), equal to the fresh probe at 73cee42 (relay data/b545_probes.txt)', '', ''),
    (188, '**What this instrument provides.**', '', S, 'T2', '', 'the machine-checked identity is the Li map`s linearity over integer streams, as the sentence says (an identity of the map); B.6(2) :355 says the kernel does not know ζ', '', ''),
    (188, '`lam_one` pins the base case', '', S, 'T2', '', '`lam_one : lam η 1 = η 1` at 73cee42, fresh', '', ''),
    (253, '**What this bracket says, and it is the shape of the work.**', '', H, 'T2', '', 'B.2 at v0.2.0 (R155)(5): the one `sorry` stands at v0.10.0 (T3_StepNineBridge.lean:108)', '', ''),
    (256, '- **h2 : mellin Phi (s / 2) ≠ 0**', '', H, 'T2', '', 'B.2`s statement of lv`s h2 as the bracket states it at v0.2.0 -- what the hypothesis is, accurately; that it is false at every s with re s ≤ 1 is b538`s (`lv_h2_false_on_strip`)', '', ''),
    (258, '**Discharge the premise = supply h1 and h2', '', R, 'T2', E3, 'h2 at Φ is false at every s with re s ≤ 1 (`lv_h2_false_on_strip`), so it cannot be supplied on the strip; the premise`s open form is `h2_sign` (`h2_sign_iff_rh`)',
     'Discharge the premise = supply the premise in its open form: h1 is supplied at T1\'s Φ (`h1_complete_at_Phi`, v0.6.0), and h2 as stated at Φ is false at every s with re s ≤ 1 (`lv_h2_false_on_strip`), because the Mellin integral of Φ is zero there (`mellin_Phi_eq_zero_of_re_le_one`); the open form is the completedRiemannZeta nonvanishing off the line (`lvh2_corrected_iff`), and in the Weil form `h2_sign` (`h2_sign_iff_rh`) -- ' + PIN + '.', ''),
    (274, 'Then h2 is the analytic content', '', R, 'T2', E3, 'as stated at Φ, h2 is C₂ where T1 holds (re s > 1) and false on the strip (`lv_h2_false_on_strip`); the next sentence`s continuation clause says where the content lies',
     'Then h2, as stated, is `mellin Phi (s/2) ≠ 0` for s off the critical line: where T1 holds (re s > 1) it is C₂ at Φ (`C2_halfplane_nonvanishing_at_Phi`), and on the strip it is false (`lv_h2_false_on_strip`, ' + PIN + '); the analytic content is its completedRiemannZeta form (`lvh2_corrected_iff`), which is where the next sentence\'s continuation clause points.', ''),
    (274, '**Note what the bench does not hide', '', S, 'T2', '', 'graded STANDS by the ruling (R155)(4), which quotes its continuation clause; it anticipated b538`s `mellin_Phi_eq_zero_of_re_le_one`', '', 'RULING (R155)(4); READING (6)`s flag'),
    (283, 'Taylor coefficients η_j at s = 1 by circle quadrature', '', S, 'T2', '', 'the method; `lam_add` is the linearity it cites', '', ''),
    (337, 'That is the whole of the measured tension in the joint', '', H, 'T3', '', 'under B.4`s in-place CORRECTION (2026-07-13, :334): retained as the record of a range read too short', '', ''),
    (343, '| SIDE-li-map (Li linear map', '', S, 'T2', '', 'the pin row; `lam_add` at 73cee42, profiles at the pin equal to the fresh probe', '', ''),
    (345, '| SIDE-lv-conservation (ARM-2 instruments)', '', R, 'T2', '', 'the pin cell groups `PartialPositivity.{partialPositivity_finiteRange, blTerm_nonneg_of_onLine}` with `v0.5.0`=`1767bd6`, where the module does not exist; both are at `v0.8.0` = `6efa9e5` (§II :68, the v0.9.4 log)',
     '| SIDE-lv-conservation (ARM-2 instruments) | `h1_complete_at_Phi` `v0.6.0`=`c80bdc2` · `RegisterPentagon` `v0.7.0`=`2d86182` · `PartialPositivity.{partialPositivity_finiteRange, blTerm_nonneg_of_onLine}` `v0.8.0`=`6efa9e5` · `exists_norm_completedLFunction_le_exp` `v0.5.0`=`1767bd6` · `C7_finite_type_false` `v0.5.1`=`bc4751e` | the grades and profiles as the row gives them; the pin cell corrected (`PartialPositivity` is absent at `1767bd6`) |', 'defect (b)'),
    (346, '| SIDE-kernel (route terminals', '', H, 'T2', '', 'a pin record with dated profiles (2026-07-10; W-7, 2026-07-16), accurate to its dates; Route 3`s premise is RH restated (`ch_iff_rh`), which the row does not contradict', '', ''),
    (354, 'Separately, and since this bench was built', '', S, 'T1-lit', '', '`partialPositivity_finiteRange` INTERFACES on its three named premises, as said', '', ''),
    (354, 'Second — and this is the point §C.6 makes', '', S, 'T1-lit', '', 'the certificate`s cutoff is Voros`s threshold (C.7.3)', '', 'OFF-SUBJECT (the verb "register")'),
    (355, '**The Li kernel does not know what ζ is.**', '', S, 'T2', '', '`lam_add` over `Nat → Int` streams, as said', '', ''),
    (356, '**T3 is open.**', '', S, 'T2', '', 'at v0.10.0 the one `sorry` stands (T3_StepNineBridge.lean:108) and T3″ is compiled', '', ''),
    (356, 'Only `T3′` closes it, and only under h1 and h2', '', R, 'T2', E3, 'h2 at Φ is false on the strip (`lv_h2_false_on_strip`), so it is not the premise restated',
     'Only `T3′` closes it, and only under h1 and h2: h1 holds at Φ (`h1_complete_at_Phi`), and h2 at Φ is false at every s with re s ≤ 1 (`lv_h2_false_on_strip`, ' + PIN + '), so T3′ closes nothing on the strip; the premise restated is the completedRiemannZeta form (`lvh2_corrected_iff`), equivalent to RH on the strip.', ''),
    (357, '**h2 is not bookkeeping.**', '', S, 'T2', '', 'graded STANDS by the ruling (R155)(4): B.6 item 4, credited (FINDINGS)', '', 'RULING (R155)(4); READING (6)`s flag'),
    (360, 'The premise remains open, and the honest form of the joint', '', S, 'T1-lit', '', 'the Li form of the joint', '', ''),
    (369, 'The seven classes of Appendix B.3 are now', '', H, 'T2', '', 'C.1 (second sitting): two classes proved at Φ then, eight since (`h1_complete_at_Phi`, v0.6.0); `T3prime_shared_witness` is T2', '', ''),
    (381, '| **C₁** realness', '', S, 'T0', '', NA + '`C1_realness_at_Phi`', '', ''),
    (382, '| **C₂** half-plane Mellin nonvanishing', '', S, 'T0', '', NA + '`C2_halfplane_nonvanishing_at_Phi`, via `completedRiemannZeta_eq_mellinPhi` and Mathlib`s nonvanishing for re s > 1', '', ''),
    (387, '| **C₇** order-≤1 completed continuation', '', S, 'T0', '', NA + '`C7_order_at_Phi`', '', ''),
    (395, 'The correct form is stated in the kernel as', '', H, 'T0', '', 'C.1`s record, OPEN at its date; discharged at v0.4.1 (E.3 :613)', '', ''),
    (429, '- **A computable split at s = 1, and its fusion fact.**', '', S, 'T2', '', '`lam_add`, stream-level', '', ''),
    (430, '- **The inter-channel form of the joint.**', '', S, 'T1-lit', '', 'C.3: Li`s criterion under the split, classical; the model of a verification record (R155)(5)', '', ''),
    (451, '**The growth-class statement\'s correct citation', '', S, 'T4', '', 'literature (C.5), verified via Voros at C.7.2', '', ''),
    (467, 'This survives the arrival of the compiled certificate intact', '', S, 'T1-lit', '', '`partialPositivity_finiteRange`', '', ''),
    (469, '**Consequence.** The discharge path runs through the kernel', '', R, 'T2', E3, 'the kernel`s h2 at Φ is false on the strip (`lv_h2_false_on_strip`); the obligation is `h2_sign` (`h2_sign_iff_rh`)',
     'Consequence. The discharge path does not run through the bench; it does not run through the kernel\'s h1 ∧ h2 at Φ either, since h2 at Φ is false at every s with re s ≤ 1 (`lv_h2_false_on_strip`); the obligation is `h2_sign`, equivalent to RH (`h2_sign_iff_rh`, ' + PIN + ').', ''),
    (496, '**Any polynomial-bound or "stiffness"', '', S, 'T4', '', 'C.7.2, literature verified via Voros', '', ''),
    (496, 'This is now verified, not conjectured', '', S, 'T4', '', 'C.7.2', '', ''),
    (505, '**Caveat — RESOLVED 2026-07-13 (sixth sitting).**', '', H, 'T4', '', 'a caveat recorded and resolved (C.7.3)', '', 'OFF-SUBJECT ("the clause" of Voros`s sentence)'),
    (546, '## D.2 The C₅ input/output split, and the fifth register', '', S, 'T4', '', 'a heading; the claims beneath are graded row by row', '', ''),
    (553, '**The gap between them is the premise\'s fifth register.**', '', R, 'T2', E1 + ', ' + E6, DEPTHS + '; the registers paragraph is at §II (:72), not §IV',
     'The gap between them is the distance the pentagon\'s R5 face records. §II of this paper (:72) lists the registers, which stand at different depths: the universality hypothesis of `silence_universal`, false in its universal form (`not_register1`); Route 3\'s `ConservationHypothesis`, RH restated (`ch_iff_rh`); the one premise of the reduction analysis; the balance→positivity distance, equivalent to RH in its Weil form (`h2_sign_iff_rh`); and the R5 output face as compiled holds outright (`register5_output_holds`) -- ' + PIN + ' -- so the gap is not one register of an equivalent premise.', ''),
    (553, 'It is the **R5 input/output face** of the compiled', '', R, 'T2', E6, '`R5_output_HilbertPolya_to_RH` INTERFACES on a premise that is RH restated, since `Register5_output_HilbertPolya` holds outright (`register5_output_holds`) -- (R151)(2)',
     'It is the R5 input/output face of the compiled `RegisterPentagon` (SIDE-lv-conservation `v0.7.0` = `2d86182`): C₅-input is certified (`C5_input_at_Phi`), and the edge `R5_output_HilbertPolya_to_RH` INTERFACES on a premise that is RH restated, since `Register5_output_HilbertPolya` holds outright (`register5_output_holds`, ' + PIN + '); what the programme disclaims is a Hilbert–Pólya realisation, which that face does not state.', ''),
    (565, '(ii) **The formation-distance statement**', '', R, 'T2', E6, 'the fifth register`s compiled output face holds outright (`register5_output_holds`)',
     '(ii) The formation-distance statement: naming the C₅ input/output gap, and observing that the two stages coincide over 𝔽_q and not over ℚ; the fifth register\'s compiled output face holds outright (`register5_output_holds`, ' + PIN + '), so the gap is not the premise in a fifth register.', ''),
    (571, '- **The critical-line census**', '', S, 'T1-lit', '', 'PATHS II.7; `partialPositivity_finiteRange` T1-lit, `C7_finite_type_false` T0', '', ''),
    (571, 'The census is the register in which', '', S, 'T4', '', 'a cross-reference to PATHS', '', 'OFF-SUBJECT (a figure of speech)'),
    (597, '`C7_entirety_at_Phi`), with', '', S, 'T0', '', NA + '`C7_entirety_at_Phi`', '', ''),
    (598, '`C7_order_at_Phi`, W-8), via', '', S, 'T0', '', NA + '`C7_order_at_Phi`', '', ''),
    (600, '**That refutation is now itself compiled**', '', S, 'T0', '', NA + '`C7_finite_type_false`', '', ''),
    (613, '| ~~`n_one_binding_instance`', '', S, 'T0', '', NA + '`n_one_binding_instance`, γ ≥ 0.53102 about Mathlib`s `eulerMascheroniConstant`', '', ''),
    (614, '| **C₅-output** | **not open', '', R, 'T2', E6, 'the fifth register`s compiled output face holds outright (`register5_output_holds`)',
     '| **C₅-output** | **not open.** Its compiled face holds outright (`register5_output_holds`, ' + PIN + '); what is disclaimed is the Hilbert–Pólya realisation, which that face does not state |', ''),
    (616, 'None of it touches h2', '', S, 'T2', '', 'true of the couplings; lv`s h2 is the hypothesis they do not touch', '', ''),
    (618, 'Its history: the finite-exponential-type form', '', S, 'T0', '', NA + '`C7_order_at_Phi`', '', ''),
    (620, 'The eighth and last class', '', S, 'T0', '', NA + '`C4_modularity_at_Phi`, `h1_complete_at_Phi`', '', ''),
    (620, '`n_one_binding_instance` also landed (`v0.4.1`; γ', '', S, 'T0', '', NA + '`n_one_binding_instance`', '', ''),
    (620, 'What remains untouched is exactly what always was', '', H, 'T2', '', 'a dated bracket-note (2026-07-17): the pass left h2 and C₅-output untouched, as it says (b543 read the monograph`s like sentence so)', '', ''),
    (626, '*v0.9.4 (2026-07-19)', '', H, 'T1-lit', '', 'the version history', '', ''),
    (626, 'The on-line-term nonnegativity is **proved**', '', H, 'T0', '', 'the version history', '', ''),
    (626, 'The four registers of §IV together with', '', H, 'T2', '', 'the version history (its "§IV" names the registers paragraph at §II, :72)', '', ''),
    (626, 'No premise advanced; the joint stands exactly as before', '', H, 'T1-lit', '', 'the version history', '', ''),
    (628, '*v0.9.3 (2026-07-17)', '', H, 'T0', '', 'the version history', '', ''),
    (628, '`n_one_binding_instance` also landed (`v0.4.1`).', '', H, 'T0', '', 'the version history', '', ''),
    (628, 'The E.3 Open table\'s C₄ and γ rows are struck.', '', H, 'T2', '', 'the version history', '', ''),
    (630, '*v0.9.2 (2026-07-15)', '', H, 'T0', '', 'the version history', '', ''),
    (638, 'The gap between them is the premise\'s FIFTH REGISTER', '', H, 'T2', '', 'the version history (b543 read the monograph`s version log so)', '', ''),
    (640, 'Consequence, now verified rather than conjectured', '', H, 'T4', '', 'the version history', '', ''),
    (660, '**b324 asked whether that margin', '', H, 'T4', '', 'b324`s dated record (2026-09-04), accurate to its date', '', ''),
    (660, 'The monograph names *positivity of the Weil functional*', '', H, 'T2', '', 'b324`s record of what the monograph says, accurate to its date; the monograph`s own sentence rests on E-2026-09-25-6', '', ''),
]
SUPP = [
    (41, S, 'T0', 'RH-ANCHOR', 'the target side`s sign is RH in the Weil form: `h2_sign_iff_rh` (SIDE-explicit-formula v0.2 = `5c72cad`; Seam.lean:101 at `81ae175`), the RH-anchor`s head -- this row`s T0 reference (R155)(3), entered in COMPONENT 3`s block'),
    (42, S, 'T4', '', 'with its 2026-08-28 annotation beside it (:57-65): the positive quantity is W_pole + W_∞ (R155)(5)'),
    (251, H, 'T2', '', 'B.2`s sorry census at v0.2.0 (R155)(5); the one `sorry` stands at v0.10.0'),
    (516, S, 'T4', '', 'C.3-C.7`s literature chain, the model of a verification record (R155)(5): every link carries the check that produced it (:527)'),
    (591, H, 'T4', '', 'Appendix E`s pricing of the Hadamard input (R155)(5), superseded by the discharge at v0.4.0, as its own parenthesis says'),
    (117, 'FANO', 'FANO', '', ''),
]


def lam_cond():
    """### READING (12)`s conditional, read off the fresh probe"""
    p = (jl('b545_probes.json').get(LI, {}).get('profiles', {}) or {}).get('LiLinearMap.lam_add')
    if p is None:
        sys.exit('### THE LI-MAP PROBE IS NOT BANKED -- run `probe` first')
    if p == 'does not depend on any axioms':
        return (S, 'T2', '', 'the fresh probe prints `lam_add` axiom-free at 73cee42, as the sentence says; :150 is the line that rests', '')
    return (R, 'T2', '', 'the fresh probe prints `lam_add` at 73cee42 with %s (relay data/b545_probes.txt), as §B.1 :150 prints it, so "axiom-free" does not hold; the edge `R4_channelDecomposition` takes additivity as its hypothesis `lam_additive`' % p.split(': ')[-1],
            'This paper\'s home is the **R4 positivity face**: its `R4_channelDecomposition` edge takes channel additivity as its hypothesis `lam_additive` (RegisterPentagon.lean:253 at SIDE-lv-conservation `v0.10.0`), the additivity that `lam_add` proves at SIDE-li-map `73cee42` over integer streams (DERIVES, profile %s, §B.1 :150 and fresh at b545), and its `R4_positivity_to_RH` edge is the Li-criterion equivalence (INTERFACES, Li\'s criterion as named premise, T1-lit).' % p.split(': ')[-1])


def sentences():
    b = rd(BAL).split(NL)
    rows = split_rows(b)
    sel = [r for r in rows if r['hits']]
    out, used = [], set()
    for r in sel:
        gs = [x for x in SGR if x[0] == r['line'] and x[1] in r['sentence']]
        if not gs:
            sys.exit('### SELECTED SENTENCE WITHOUT A TYPED ROW at :%d: %s' % (r['line'], r['sentence'][:160]))
        if len(set(x[2] for x in gs)) != len(gs):
            sys.exit('### TWO TYPED ROWS FOR ONE CLAUSE at :%d' % r['line'])
        for x in gs:
            line, key, clause, verdict, tier, grounds, reason, rect, flag = x
            if verdict == 'COND-LAM':
                verdict, tier, grounds, reason, rect = lam_cond()
            out.append(dict(line=line, sentence=r['sentence'], clause=clause, hits=r['hits'], terminals=r['terminals'], verdict=verdict,
                            tier=tier, grounds=grounds, reason=reason, rectification=rect, flag=flag, kind='SELECTED',
                            anchor_cited=sorted({a for a in ANCHOR_SHORT if '`%s`' % a in rect})))
            used.add((line, key, clause))
    unused = [(x[0], x[1]) for x in SGR if (x[0], x[1], x[2]) not in used]
    if unused:
        sys.exit('### A TYPED ROW MEETS NO SELECTED SENTENCE: %s' % unused)
    tj = jl('b545_tiers.json')
    supp = []
    for line, verdict, tier, flag, reason in SUPP:
        if verdict == 'FANO':
            if tj.get('fano_compiled'):
                verdict, tier, reason, flag = S, 'T0', ('compiled: `FanoTwoDarkness.second_moment` with `first_moment` and the design counts, SIDE-fano-darkness `0f6ce5b` (public, untagged), [propext, Quot.sound] or fewer, fresh -- in the integer-valued form; the real-valued form follows from the polynomial identity and is not compiled; the Correspondence row is in the tier block'), ''
            else:
                verdict, tier, reason, flag = S, 'T4', 'decide-closable, not compiled', ''
        supp.append(dict(line=line, sentence=b[line - 1].strip(), verdict=verdict, tier=tier, reason=reason, flag=flag, kind='SUPPLEMENTARY',
                         rectification='', grounds='', anchor_cited=[]))
    yields = {n: sum(1 for r in rows if n in r['hits']) for n, _ in PAT}
    cnt = lambda rs: {v: sum(1 for r in rs if r['verdict'] == v) for v in (S, H, R, 'EXCEEDS')}
    tiers_ = lambda rs: {t: sum(1 for r in rs if r['tier'] == t) for t in RANK}
    rests = [r for r in out if r['verdict'] == R]
    by_ground = {}
    for r in rests:
        k = r['grounds'] or 'BALPOS`s own (no filed subject)'
        by_ground[k] = by_ground.get(k, 0) + 1
    anchor_tier_refs = [r for r in out + supp if r['flag'] == 'RH-ANCHOR']
    numerals = len([r for r in rows if re.fullmatch(r'[0-9]+[.]', r['sentence'].strip())])
    res = dict(read=len(rows), numerals=numerals, selected=len(sel), rows=len(out), yields=yields, graded=out, supplementary=supp, counts=cnt(out),
               counts_supp=cnt(supp), tiers=tiers_(out), tiers_supp=tiers_(supp), rests_by_ground=by_ground,
               rectifications=len([r for r in rests if r['rectification']]), anchor_tier_refs=len(anchor_tier_refs),
               anchor_cited_in_rect=sorted({a for r in rests for a in r['anchor_cited']}),
               rect_rows_citing_anchor=len([r for r in rests if r['anchor_cited']]), off_subject=len([r for r in out if r['flag'].startswith('OFF')]))
    put_json('b545_sentences.json', res)
    for n, v in yields.items():
        print('  matcher %-17s yield %d' % (n, v))
    print('  sentences read %d ; selected %d ; graded rows %d (:72 is two) ; supplementary %d' % (len(rows), len(sel), len(out), len(supp)))
    for r in out + supp:
        print('  :%-4d %-9s %-18s %-7s %-30s %s' % (r['line'], r['kind'][:9], r['verdict'], r['tier'], (r['grounds'] or '')[:30], r['sentence'][:90]))
    print('  counts %s ; supplementary %s ; tiers %s ; tiers supp %s' % (res['counts'], res['counts_supp'], res['tiers'], res['tiers_supp']))
    print('  RESTS by ground %s ; rectification rows %d ; anchor tier references %d ; anchor theorems cited in rectifications %s (%d rows)' % (
        by_ground, res['rectifications'], res['anchor_tier_refs'], res['anchor_cited_in_rect'], res['rect_rows_citing_anchor']))


# ------------------------------------------------------------------------------ THE WRITES: BALPOS (COMPONENTS 1-3), FINDINGS, SURR
TIERH = ('### Appendix B.5, tiered under (R149)-(R151) and (R155) -- 2026-09-26, b545 (a new table beneath the bench-pin table at '
         ':339-348, row for row; no byte above this block changes)')
SENTH = ('### The sentence read under (R155)(2) -- 2026-09-26, b545: the sentences naming h2, the registers, the pentagon, Route 3, the '
         'goal state, the clause, the joint or a named terminal, graded; the rows that rest rectified by appended row (no byte above this block changes)')
JOINTH = ('### The joint\'s two forms at the RH-anchor: the Weil form compiled, the Li form a literature theorem -- appended 2026-09-26 by '
          'b545 beneath §II (:53-74); no byte above this block changes')
CREDITH = '## BALANCE_AND_POSITIVITY Appendix B.6(4), 2026-07-13, read against b538: an earlier finding that anticipated the register census'
ACTH = ('## The cascade, act three: BALANCE_AND_POSITIVITY tiered, the joint in two forms, the earlier finding credited, the Fano '
        'theorem\'s kernel status')
HEADING = ('### b545 — the cascade, act three under (R155): BALANCE_AND_POSITIVITY tiered, the joint in two forms, the earlier finding '
           'credited, the Fano theorem found compiled')
LV_DESC = ("The one deliberately open obligation is the clause itself; the kernel's docstrings and the manuscript's Sections 25.8 and 27.3 "
           "state its exact location and status.")


def cell(s):
    return s.replace('|', '/')


def guard_absent(path, heading):
    if heading.encode('utf-8') in open(path, 'rb').read():
        sys.exit('### ALREADY PRESENT IN %s: %s' % (os.path.basename(path), heading[:80]))


def fmt_counts(d):
    return ' · '.join('%s %d' % (k, v) for k, v in d.items())


def write_tiers():
    guard_absent(BAL, TIERH)
    tj = jl('b545_tiers.json')
    L = ['', '<!-- b545 (R155) TIER TABLE, 2026-09-26 -->', '', TIERH, '',
         '*Appended by b545 under the author`s ruling `(R155)`(2). This document has no section headed Correspondence; the table '
         '`THE_LOAD_BEARING_MAP.md` counts among its fourteen (:16-18) is Appendix B.5`s bench-pin table (:339-348). One row per row of B.5, '
         'its terminals beneath it: each re-read at the row`s pin and at the current pin (the statement printed SAME or DIFFERENT), the grade '
         'kept, the tier of `(R149)`(2) as corrected by `(R150)`(3) and `(R151)`(2) with its reason, CARRIED or MOVED against the latest '
         'earlier tier or NEW, and CP-3`s E/I mark (`FINDINGS.md`:5272). A row`s tier is the lowest among the tiers of its terminals. Bank: relay '
         '`data/b545_tiers.json`.*', '',
         '| B.5 row | terminal or object | pin (row) → re-read | statement | grade (kept) | tier | reason | against the earlier tier | E/I (CP-3) |',
         '|:--|:--|:--|:--|:--|:--|:--|:--|:--|']
    for r in tj['rows']:
        for i, t in enumerate(r['terminals']):
            pin = ('%s `%s` → `%s`' % (t['repo'], t['row_pin'], t['now_pin'])) if t['repo'] else '--'
            ag = t['carried'] + ((' -- %s at %s' % (t['earlier'][0], t['earlier'][1])) if t['earlier'] else '')
            L.append('| %s | `%s` | %s | %s | %s | **%s** | %s | %s | %s |' % (
                (':%d -- %s (row tier **%s**)' % (r['line'], cell(r['object']), r['tier'])) if i == 0 else '', cell(t['terminal']), pin, t['same'],
                cell(t['grade']), t['tier'], cell(t['reason']), cell(ag), t['ei']))
    c = tj['counts']
    L += ['', '**Tier counts.** Rows: %s. Terminals and objects: %s. Against the earlier tier: %s. Statements at both pins: SAME %d; '
          '`RegisterPentagon`, a module, changed its file between `v0.7.0` and `v0.10.0` and keeps its tier.'
          % (fmt_counts(c['rows']), fmt_counts(c['terminals']), fmt_counts(c['carried']), c['same']['SAME'])]
    f = tj.get('fano')
    if f:
        pr = f['profiles']
        prof = '; '.join('`%s`: %s' % (k.split('.')[-1], v.replace('depends on axioms: ', '').replace('does not depend on any axioms', 'none'))
                         for k, v in pr.items() if k.split('.')[-1] in ('second_moment', 'first_moment', 'point_line_count', 'pair_line_count',
                                                                        'point_triple_count', 'pair_triple_count'))
        L += ['', '**Correspondence row added under `(R155)`(5): §V`s Fano two-darkness theorem, found compiled.**', '',
              '| claim | terminal | pin | profile (fresh) | grade | tier |', '|:--|:--|:--|:--|:--|:--|',
              '| §V :117 -- every statistic of degree at most two of triple-sums takes the same value over the seven lines as over the twenty-eight '
              'non-line triples | `FanoTwoDarkness.second_moment`, with `first_moment`, `point_line_count`, `pair_line_count`, `point_triple_count`, '
              '`pair_triple_count` | SIDE-fano-darkness `0f6ce5b` (public `main`, untagged; vanilla Lean v4.29.0-rc8) | %s | DERIVES | **T0** -- '
              'for integer point values: `4 · Σ_lines (sum)² = Σ_non-lines (sum)²` and the first-moment twin, the seven lines and the twenty-eight '
              'non-line triples read by hand; §V states real values, and the real-valued form follows from the integer polynomial identity and is not compiled |' % prof]
    L += ['', '*Filed by b545. No byte above this block changes; no grade on a line above it moves.*', '']
    out = append_to(BAL, NL.join(L))
    out['heading_line'] = rd(BAL).split(NL).index(TIERH) + 1
    put_json('b545_write_tiers.json', out)
    print('  BALANCE_AND_POSITIVITY.md tier block : %s' % out)


def write_sentences():
    guard_absent(BAL, SENTH)
    sj = jl('b545_sentences.json')
    rests = [r for r in sj['graded'] if r['verdict'] == R]
    L = ['', '<!-- b545 (R155) SENTENCE READ, 2026-09-26 -->', '', SENTH, '',
         '*Appended by b545 under `(R155)`(2) and (5). Every sentence of this document naming h2, a register, the pentagon, Route 3, the goal '
         'state, the clause, the joint, or a named terminal was read -- %d segments (%d sentences and %d list numerals the splitter cut apart), %d selected, the registers sentence at :72 in two rows '
         '(its registers clause and its Route 3 clause) -- with six lines the ruling or the ferry names (§I :41 and :42, B.2 :251, C.7.4 :516, '
         'E.1 :591, §V :117). Each is graded STANDS / STANDS-AS-HISTORY / RESTS / EXCEEDS with its tier. Bank: relay `data/b545_sentences.json`. '
         'This document is not deposited (:65), so a row that rests is rectified here, by the row beneath it, and draws no erratum; its ground '
         'names the filed erratum whose subject it falls under.*' % (sj['read'], sj['read'] - sj['numerals'], sj['numerals'], sj['selected']), '',
         '**Counts.** %d rows: %s. Supplementary %d: %s. Tiers of the rows: %s; of the supplementary: %s.'
         % (sj['rows'], fmt_counts(sj['counts']), len(sj['supplementary']), fmt_counts(sj['counts_supp']), fmt_counts(sj['tiers']),
            fmt_counts(sj['tiers_supp'])), '',
         '**The six named lines.** ' + ' '.join('**:%d** %s (%s) -- %s.' % (s['line'], s['verdict'], s['tier'], s['reason']) for s in sj['supplementary']), '',
         '**The rows that rest, each with its rectification** (the anchor theorems at SIDE-explicit-formula `81ae175`):', '']
    for r in rests:
        L.append('- **:%d**%s -- RESTS; ground: %s. *"%s"*' % (r['line'], (' (%s)' % r['clause']) if r['clause'] else '',
                                                             r['grounds'] or 'this document`s own (no filed erratum`s subject)', r['sentence']))
        L.append('  - reads: %s.' % r['reason'])
        L.append('  - rectification: *"%s"*' % r['rectification'])
    L += ['', '*Filed by b545. No byte above this block changes; nothing deposits; nothing here is a statement about RH.*', '']
    out = append_to(BAL, NL.join(L))
    out['heading_line'] = rd(BAL).split(NL).index(SENTH) + 1
    out['rests_written'] = len(rests)
    put_json('b545_write_sentences.json', out)
    print('  BALANCE_AND_POSITIVITY.md sentence block : %s' % out)


def joint():
    guard_absent(BAL, JOINTH)
    L = ['', '<!-- b545 (R155) THE JOINT IN TWO FORMS, 2026-09-26 -->', '', JOINTH, '',
         '*Under the author`s ruling `(R155)`(3).*', '',
         '**The Weil form, compiled.** The target side of §I`s table (:41, "Σ_ρ h(γ_ρ) ... ≥ 0 ⟺ RH") is the Weil form of the obligation: '
         '`h2_sign`, the sign `0 ≤ poleTerm k - primeSum k + archTerm k` over the class `classK`. SIDE-explicit-formula compiles it '
         'equivalent to Mathlib`s `RiemannHypothesis` both ways: `h2_sign_iff_rh : h2_sign ↔ RiemannHypothesis` (v0.2 = `5c72cad`; '
         '`Seam.lean`:101 at `81ae175`, a fresh `#check` at b545, profile [propext, Classical.choice, Quot.sound]). It is the T0 reference of '
         '§I`s target-side row, and the one T0 RH-anchor reference this keystone carries.', '',
         '**The Li form, a literature theorem.** This keystone`s joint, RH ⟺ λ_Z(n) ≥ −λ_A(n) for every n (:21, :72, :360, :430), is Li`s '
         'criterion under the channel split -- Bombieri–Lagarias 1999 and Voros 2006, verified at source in Appendix C.3 and C.7. Its '
         'equivalence to RH is not compiled in the federation: the pentagon`s `R4_positivity_to_RH` (SIDE-lv-conservation `v0.10.0`, '
         '`RegisterPentagon.lean`:266) INTERFACES on Li`s criterion as a named premise. It is T1-lit, and the sentence stands as a classical statement.', '',
         '**The bridge between the two.** The Li coefficients are Weil positivity written in a basis (Bombieri–Lagarias; Appendix D.1): '
         'classical, and not compiled. b324`s owed bridging statement -- the archimedean margin at a lawful test function against the Li '
         'margin at an index n (the cross-reference above, :662) -- stays owed. It is on the trails as W-ORD-MARGIN-BRIDGE, the trail '
         '`OPEN_TRAILS.md` carries as W-ORD-LI-WEIL-BRIDGE (:3548, b324`s statement given that ID there), now with the Weil-form obligation compiled and the Li-form '
         'obligation T1-lit stated beside it.', '',
         '*Filed by b545. No byte above this block changes; no grade on a line above it moves; nothing here is a statement about RH.*', '']
    out = append_to(BAL, NL.join(L))
    out['heading_line'] = rd(BAL).split(NL).index(JOINTH) + 1
    put_json('b545_write_joint.json', out)
    print('  BALANCE_AND_POSITIVITY.md joint block : %s' % out)


def credit():
    guard_absent(FIND, CREDITH)
    b = rd(BAL).split(NL)
    s357 = next(s['sentence'] for s in jl('b545_sentences.json')['graded'] if s['line'] == 357)
    s274 = next(s['sentence'] for s in jl('b545_sentences.json')['graded'] if s['line'] == 274 and s['sentence'].startswith('**Note'))
    if not (s357 in ' '.join(b[356].split()) and s274.split('**')[1] in b[273]):
        sys.exit('### THE QUOTED LINES ARE NOT AT :357 AND :274')
    lvq = [r for r in jl('b539_sentences.json')['selected'] if r['sentence'] == LV_DESC]
    if len(lvq) != 1:
        sys.exit('### b539`S ROW FOR THE LV DESCRIPTION NOT FOUND ONCE')
    L = ['', CREDITH, '',
         '*Filed at b545 on the author`s ruling `(R155)`(4). The keystone is `phase1.5/spectral/BALANCE_AND_POSITIVITY.md` (not deposited); '
         'the later description is lv-conservation`s, deposited (Zenodo 21539068).*', '',
         '**The sentence, at its lines.** The ruling quotes one sentence; the keystone carries it on two lines of 2026-07-13:', '',
         '- B.6 item 4, `BALANCE_AND_POSITIVITY.md`:357: *"%s"*' % s357,
         '- B.3, `BALANCE_AND_POSITIVITY.md`:274: *"%s"*' % s274, '',
         '**The later description it anticipated**, lv-conservation`s deposited description as b539 banked it (relay `data/b539_sentences.json`; '
         'source `data/b499_fetchback_21539068.json` metadata.description): *"%s"* -- b539 graded it %s: %s.' % (LV_DESC, lvq[0]['grade'], lvq[0]['reason']), '',
         '**The relation.** In July the keystone already said that lv`s h2 is a statement whose content lies outside the half-plane where the '
         'Mellin identity T1 holds, so that in the strip "the T1 identity itself needs continuation" -- which is b538`s finding that the clause '
         'as stated is false on the strip in Mathlib`s sense (`mellin_Phi_eq_zero_of_re_le_one`, `lv_h2_false_on_strip`, SIDE-explicit-formula '
         '`81ae175`). The later description "h1 complete, h2 open" took that h2 for the open clause itself, a wider context than the earlier '
         'finding allowed, and b538`s census and E-2026-09-25-3 returned to what B.3 had said.', '',
         '**Graded STANDS, as the ruling grades it; the seat`s read beside it.** Both lines are graded STANDS under `(R155)`(4). Read literally, '
         '"RH-strength on the half-plane where T1 holds" names a statement which on that half-plane (re s > 1) is C₂ at Φ, proved in the same '
         'appendix`s second sitting (`C2_halfplane_nonvanishing_at_Phi`, SIDE-lv-conservation `v0.10.0` `CouplingsAtPhi.lean`:205; T0, not RH); '
         'the clause that anticipated b538 is :274`s "outside it the T1 identity itself needs continuation". This is held for the author`s word, '
         'and no grade moves.', '',
         '*Cross-referenced from THE_UNCONDITIONAL_SURROUND`s b539 tier table (:211) by an appended line. Nothing deposits; nothing here is a '
         'statement about RH.*', '']
    out = append_to(FIND, NL.join(L))
    hl = rd(FIND).split(NL).index(CREDITH) + 1
    out['heading_line'] = hl
    line = ('**Cross-reference, appended 2026-09-26 (b545), to the b539 tier table at :211:** lv-conservation`s deposited sentence "The one '
            'deliberately open obligation is the clause itself; ..." (b539`s row, RESTS on E-2026-09-25-3) was anticipated on 2026-07-13 by '
            'BALANCE_AND_POSITIVITY B.3 (:274) and B.6 item 4 (:357); the credit is at `FINDINGS.md`:%d, *BALANCE_AND_POSITIVITY Appendix B.6(4), '
            '2026-07-13, read against b538*. Nothing above this line is edited.' % hl)
    if 'b545' in rd(SURR):
        sys.exit('### SURR ALREADY CARRIES A b545 LINE')
    so = append_to(SURR, line + NL)
    put_json('b545_credit.json', dict(findings=out, surr=so, surr_line=len(rd(SURR).rstrip(NL).split(NL))))
    print('  FINDINGS credit : %s ; SURR : %s' % (out, so))


def findings():
    guard_absent(FIND, ACTH)
    tj, sj, cj, fh = jl('b545_tiers.json'), jl('b545_sentences.json'), jl('b545_credit.json'), jl('b545_fano_hits.json')
    wt, ws, wj = jl('b545_write_tiers.json'), jl('b545_write_sentences.json'), jl('b545_write_joint.json')
    c = tj['counts']
    moved = [t for r in tj['rows'] for t in r['terminals'] if t['carried'].startswith('MOVED')]
    L = ['', ACTH, '',
         '*Filed at b545 on the author`s ruling `(R155)`. Banks: relay `data/b545_tiers.json`, `data/b545_sentences.json`, `data/b545_fano_hits.json`, '
         '`data/b545_probes.json`, `data/b545_anchor.txt`. The keystone`s appended blocks are at `BALANCE_AND_POSITIVITY.md`:%d (the tier table), '
         ':%d (the sentence read), :%d (the joint in two forms).*' % (wt['heading_line'], ws['heading_line'], wj['heading_line']), '',
         '**The table.** The keystone has no section headed Correspondence; the table `THE_LOAD_BEARING_MAP.md` counts among its fourteen is '
         'Appendix B.5`s bench-pin table, :339-348. Six rows and seventeen terminals or objects, each re-read at the row`s pin and the current '
         'pin: rows %s; terminals and objects %s; %s; statements SAME at both pins %d. MOVED: %s.'
         % (fmt_counts(c['rows']), fmt_counts(c['terminals']), fmt_counts(c['carried']), c['same']['SAME'],
            '; '.join('%s, %s: %s' % (t['terminal'], t['carried'], t['reason']) for t in moved) or 'none'), '',
         '**The sentences.** %d segments read (%d sentences, %d list numerals), %d selected, %d rows (:72 in two); %s. Supplementary %d: %s. RESTS by ground: %s. '
         '%d rectification rows appended; no erratum drafted or filed. Tiers of the rows: %s.'
         % (sj['read'], sj['read'] - sj['numerals'], sj['numerals'], sj['selected'], sj['rows'], fmt_counts(sj['counts']), len(sj['supplementary']), fmt_counts(sj['counts_supp']),
            '; '.join('%s %d' % (k, v) for k, v in sj['rests_by_ground'].items()), sj['rectifications'], fmt_counts(sj['tiers'])), '',
         '**The joint in two forms.** The Weil form is `h2_sign`, compiled both ways against Mathlib`s `RiemannHypothesis` (`h2_sign_iff_rh`, '
         'v0.2 = `5c72cad`): the T0 reference of §I`s target-side row, the one T0 RH-anchor reference in the keystone. The Li form, RH ⟺ λ_Z(n) '
         '≥ −λ_A(n) for every n, is Li`s criterion under the channel split, a literature theorem not compiled (T1-lit), and its sentences stand. '
         'The rectification rows cite the anchor theorems as grounds (%s, in %d rows); they are not tier references.'
         % (', '.join('`%s`' % a for a in sj['anchor_cited_in_rect']), sj['rect_rows_citing_anchor']), '',
         '**The earlier finding credited** at `FINDINGS.md`:%d, with the seat`s read of its clause held for the author`s word.' % cj['findings']['heading_line'], '',
         '**The Fano theorem`s kernel status: COMPILED.** §V`s two-darkness theorem is compiled in SIDE-fano-darkness at `0f6ce5b` (public '
         '`main`, untagged, vanilla Lean v4.29.0-rc8): `FanoTwoDarkness.second_moment` and `first_moment` ([propext, Quot.sound]) state the '
         'moment identities for integer point values over the seven lines and the twenty-eight non-line triples; `point_line_count`, '
         '`pair_line_count`, `point_triple_count`, `pair_triple_count` state the 2-(7,3,1) frequencies, by `decide`. T0 in the integer-valued '
         'form; §V`s real-valued form follows from the integer polynomial identity and is not compiled. The search read %d repositories at '
         '%d revisions (%d .lean files); %d needle hits, hand-read; the Fano incidence appears in other kernels (SIDE-kernel `Kernel/Trivium.lean`, '
         '`Bridge/FanoSteane.lean`; SIDE-cosmo; SIDE-structural-error-correction; SIDE-substrate-cluster) and the moment theorem only in '
         'SIDE-fano-darkness. That repository is one of %d outside b542`s enumeration (%s), so CP-2`s census of b544 did not count them.'
         % (len(fh['repos']), fh['revisions'], fh['files'], len(fh['hits']), len(fh['outside_b542']), ', '.join(fh['outside_b542'])), '',
         '**(R155)(1), entered.** b544`s census is entered as it closed; the reading "few" is withdrawn as the navigator`s; '
         '`side_exclusion_bridge` concludes re = 1/2 from the hypothesis `RHHypothesis` and is correctly premised; `RHHypothesis` and '
         '`SimplicityHypothesis` are Part IV`s conditionals, entered as T1-open premises of the geometric clause`s kind, distinct from '
         '`h2_sign`; `PWSetup`, `EF_lit`, `GammaFacts`, `HCount`, `LocalCount` and `ZetaSeam` are proved instances, not premises. b544`s trail '
         'line (`OPEN_TRAILS.md`:11097, "no I row concludes re = 1/2") is corrected by this act`s trail: one I row does, `side_exclusion_bridge` '
         '(`FINDINGS.md`:5457).', '',
         '**Next keystone:** FACES_OF_H2_AT_FINITE_INSTANCE with FACES_LEDGER.', '',
         '*Nothing deposits; nothing at Zenodo written; no kernel edited; nothing here is a statement about RH.*', '']
    out = append_to(FIND, NL.join(L))
    out['heading_line'] = rd(FIND).split(NL).index(ACTH) + 1
    put_json('b545_findings.json', out)
    print('  FINDINGS act entry : %s' % out)


# ------------------------------------------------------------------------------ THE SCORES, THE DESK, THE COMPONENTS, THE TRAIL
PRIOR_PP = 'a0f73df'
WRITE_OK = {'phase1.5/spectral/BALANCE_AND_POSITIVITY.md', 'FINDINGS.md', 'OPEN_TRAILS.md', 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md'}


def gitc(r, *a):
    return subprocess.run(['git', '-C', r] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout.strip()


def w(v):
    return 'VACUOUS' if v is None else ('HELD' if v else 'REFUTED')


def scores():
    tj, sj, cj = jl('b545_tiers.json'), jl('b545_sentences.json'), jl('b545_credit.json')
    g_ = {(r['line'], r['clause']): r for r in sj.get('graded', [])}
    committed = gitc(PP, 'log', '-1', '--pretty=%s').startswith('b545 --')
    base = 'HEAD~1' if committed else 'HEAD'
    bal_old = subprocess.run(['git', '-C', PP, 'show', '%s:phase1.5/spectral/BALANCE_AND_POSITIVITY.md' % base], capture_output=True).stdout
    bal_new = open(BAL, 'rb').read().replace(b'\r\n', b'\n')
    written = sorted(x for x in gitc(PP, 'diff', '--name-only', PRIOR_PP).split(NL) if x) if not committed else \
        sorted(x for x in gitc(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x)
    needle = 'https://' + 'zenodo' + '.org'
    zen = [x for x in os.listdir(T) if x.startswith('b545_') and needle in rd(os.path.join(T, x))]
    t = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    tok = sum(open(os.path.join(d0, f), 'rb').read().count(t) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b545_')) if t else None
    kernels = {k: gitc(os.path.join('D:', os.sep, k), 'status', '--porcelain', '--untracked-files=no') == ''
               for k in ('SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-explicit-formula', 'SIDE-global-section', 'SIDE-li-map', 'SIDE-fano-darkness')}
    errata_same = gitc(PP, 'hash-object', 'ERRATA.md') == gitc(PP, 'rev-parse', '%s:ERRATA.md' % PRIOR_PP)
    reg = g_.get((72, 'the registers clause'), {})
    r3 = g_.get((72, 'the Route 3 clause'), {})
    li = next((r for r in sj.get('graded', []) if r['line'] == 72 and r['sentence'].startswith('On the present bench')), {})
    s357 = next((r for r in sj.get('graded', []) if r['line'] == 357), {})
    anchor_rows = [r for r in sj.get('graded', []) + sj.get('supplementary', []) if r['flag'] == 'RH-ANCHOR']
    lam = (jl('b545_probes.json').get(LI, {}).get('profiles', {}) or {}).get('LiLinearMap.lam_add')
    r72 = next((r for r in sj.get('graded', []) if r['line'] == 72 and r['sentence'].startswith('This paper')), {})
    terms = [t_ for r in tj.get('rows', []) for t_ in r['terminals'] if t_['repo']]
    return dict(
        n1=len(anchor_rows) == 1 and anchor_rows[0]['line'] == 41 and 'h2_sign_iff_rh' in anchor_rows[0]['reason'],
        n1_rows=[(r['line'], r['kind']) for r in anchor_rows], n1_apart=(sj.get('rect_rows_citing_anchor'), sj.get('anchor_cited_in_rect')),
        n2=li.get('verdict') == S and li.get('tier') == 'T1-lit',
        n3=reg.get('verdict') == R and r3.get('verdict') == R and errata_same and all(r.get('rectification') for r in (reg, r3)),
        n3_rows=[(r['clause'] or r['sentence'][:32], r['verdict']) for r in sj.get('graded', []) if r['line'] == 72],
        n4=s357.get('verdict') == S and bool(cj.get('findings', {}).get('heading_line')),
        n5=not tj.get('fano_compiled'),
        n6=(bal_new.startswith(bal_old) and len(bal_new) > len(bal_old) and not zen and tok == 0 and all(kernels.values())
            and set(written) <= WRITE_OK and errata_same),
        bal_prefix=bal_new.startswith(bal_old), written=written, zen=zen, token=tok, kernels=kernels, errata_same=errata_same,
        s1=bool(lam) and 'propext' in lam and 'Quot.sound' in lam and r72.get('verdict') == R,
        s2=(not [t_ for t_ in terms if t_['carried'].startswith('MOVED')]) and len([t_ for t_ in terms if t_['carried'] == 'NEW']) >= 2,
        s2_new=[t_['terminal'] for t_ in terms if t_['carried'] == 'NEW'], s2_moved_rows=[r['line'] for r in tj.get('rows', []) for t_ in r['terminals'] if t_['carried'].startswith('MOVED')],
        s3=bool(tj.get('fano_compiled')))


def desk():
    sc = scores()
    N, SS = ('n1', 'n2', 'n3', 'n4', 'n5', 'n6'), ('s1', 's2', 's3')
    L = ['=' * 104, 'b545 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '', '### THE NAVIGATOR`S SIX.', '-' * 104,
         '  **(N1)** ### **%s.** -- tier cells naming an RH-anchor terminal as a row`s T0 reference: %s (READING (7)`s count); apart, the '
         'rectification rows citing anchor theorems as grounds: %s rows, %s.' % (w(sc['n1']), sc['n1_rows'], sc['n1_apart'][0], sc['n1_apart'][1]),
         '  **(N2)** ### **%s.** -- :72 "On the present bench the joint takes its sharpest form": STANDS, T1-lit.' % w(sc['n2']),
         '  **(N3)** ### **%s.** -- :72`s rows %s ; ERRATA unchanged %s ; no erratum drafted.' % (w(sc['n3']), sc['n3_rows'], sc['errata_same']),
         '  **(N4)** ### **%s.** -- :357 graded STANDS by the ruling, the credit written; READING (6)`s flag in the same line: read literally the '
         'clause is C₂ at Φ (proved), and the anticipation is :274`s continuation clause -- held for the author`s word.' % w(sc['n4']),
         '  **(N5)** ### **%s.** -- the Fano theorem is compiled: SIDE-fano-darkness `0f6ce5b`, `FanoTwoDarkness.second_moment` (integer point values).' % w(sc['n5']),
         '  **(N6)** ### **%s.** -- BALPOS`s committed bytes a prefix of its new bytes %s ; PLACE-papers files written %s ; tools naming the platform %s ; '
         'token %s ; kernels clean %s.' % (w(sc['n6']), sc['bal_prefix'], sc['written'], sc['zen'] or 'NONE', sc['token'], sc['kernels']),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- `lam_add` at 73cee42 prints [propext, Quot.sound]; :72`s "axiom-free" RESTS; :150 STANDS-AS-HISTORY.' % w(sc['s1']),
         '  **(S2)** ### **%s.** -- B.5 terminals MOVED: none ; NEW terminals: %s ; the manuscript row :%s prints MOVED (not a terminal).'
         % (w(sc['s2']), sc['s2_new'], sc['s2_moved_rows']),
         '  **(S3)** ### **%s.** -- the Fano theorem found compiled in SIDE-fano-darkness.' % w(sc['s3']),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in N].count(True), [sc[k] for k in N].count(False), [sc[k] for k in SS].count(True), [sc[k] for k in SS].count(False)),
         '', '### THIS ACT`S OWN DEFECTS.'] + ([l for l in rd(os.path.join(D, 'b545_defects.txt')).rstrip(NL).split(NL) if l]
                                              if os.path.exists(os.path.join(D, 'b545_defects.txt')) else ['    NONE RECORDED.']) + ['=' * 104]
    put_txt('b545_desk_notes.txt', L)
    put_json('b545_scores.json', sc)
    print(NL.join(L))


def components():
    L = ['=' * 132, 'b545 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '', '### THE PURPOSE STATEMENT (BALANCE_AND_POSITIVITY.md:21-27), PRINTED BEFORE ANY EDIT:']
    L += ['  ' + l for l in rd(os.path.join(D, 'b545_reads.txt')).split(NL) if l.startswith('  :2') and ':21 ' <= l[2:6] <= ':27 '][:7]
    L += ['', '### THE RH-ANCHOR:'] + ['  ' + l for l in rd(os.path.join(D, 'b545_anchor.txt')).rstrip(NL).split(NL)]
    L += ['', '### THE PROBES:'] + ['  ' + l for l in rd(os.path.join(D, 'b545_probes.txt')).rstrip(NL).split(NL) if 'axioms' in l or l.startswith('###')]
    L += ['', '### COMPONENT 1 -- THE TIERS:'] + ['  ' + l for l in rd(os.path.join(D, 'b545_tiers.txt')).rstrip(NL).split(NL)]
    sj = jl('b545_sentences.json')
    L += ['', '### COMPONENT 2 -- THE SENTENCES : yields %s ; read %d ; selected %d ; rows %d ; counts %s ; supplementary %s ; RESTS by ground %s'
          % (sj['yields'], sj['read'], sj['selected'], sj['rows'], sj['counts'], sj['counts_supp'], sj['rests_by_ground'])]
    L += ['  :%-4d %-13s %-18s %-7s %s' % (r['line'], r['kind'], r['verdict'], r['tier'], r['sentence'][:110]) for r in sj['graded'] + sj['supplementary']]
    L += ['', '### THE WRITES : tiers %s ; sentences %s ; joint %s ; credit %s ; findings %s' % tuple(
        json.dumps(jl(n), ensure_ascii=False) for n in ('b545_write_tiers.json', 'b545_write_sentences.json', 'b545_write_joint.json', 'b545_credit.json', 'b545_findings.json'))]
    fh = jl('b545_fano_hits.json')
    L += ['', '### COMPONENT 5 -- THE FANO SEARCH : repositories %d ; revisions %d ; files %d ; hits %d ; by repository %s' % (
        len(fh['repos']), fh['revisions'], fh['files'], len(fh['hits']), fh['by_repo']), '  every hit : relay data/b545_fano_search.txt',
          '### THE UNDECLARED READ : relay data/b545_fano_lsremote.txt', '### THE BRANCHES : see data/b545_branches.txt', '=' * 132]
    put_txt('b545_components.txt', L)
    print(NL.join(L[:12]))


def trail():
    sc, tj, sj, fj = scores(), jl('b545_tiers.json'), jl('b545_sentences.json'), jl('b545_findings.json')
    cj, wt, ws, wj = jl('b545_credit.json'), jl('b545_write_tiers.json'), jl('b545_write_sentences.json'), jl('b545_write_joint.json')
    body = ['', HEADING, '',
            '**(R155) ratified.** (1) b544`s census entered as it closed; "few" withdrawn as the navigator`s; `side_exclusion_bridge` correctly '
            'premised on `RHHypothesis`; `RHHypothesis` and `SimplicityHypothesis` T1-open premises of the geometric clause`s kind, distinct from '
            '`h2_sign`; the six setup structures proved instances. (2) BALANCE_AND_POSITIVITY is the cascade`s next keystone, rectified by appended '
            'row. (3) The joint in two forms. (4) B.6(4) credited. (5) The registers paragraph and Route 3 mention rest; the named lines graded; '
            'the Fano theorem graded by its kernel status.', '',
            '**Entered:** BALANCE_AND_POSITIVITY.md:%d (B.5 tiered, with the Fano Correspondence row), :%d (the sentence read), :%d (the joint in '
            'two forms); FINDINGS.md:%d (the credit) and :%d (the act); THE_UNCONDITIONAL_SURROUND.md:%d (the cross-reference line).'
            % (wt['heading_line'], ws['heading_line'], wj['heading_line'], cj['findings']['heading_line'], fj['heading_line'], cj['surr_line']), '',
            '**The table:** B.5, rows %s; %s. **The sentences:** %d rows %s; supplementary %s; %d rectification rows; no erratum.'
            % (fmt_counts(tj['counts']['rows']), fmt_counts(tj['counts']['carried']), sj['rows'], fmt_counts(sj['counts']),
               fmt_counts(sj['counts_supp']), sj['rectifications']), '',
            '| # | ID | kind | the item | price | trigger |', '|:--|:--|:--|:--|:--|:--|',
            '| **1** | `W-ORD-MARGIN-BRIDGE` | **RESULT or RULING** | b324`s bridging statement, re-entered under `(R155)`(3): *a formula carrying '
            'the archimedean margin at a lawful test function to the Li margin at an index n, or a proof that no such formula exists* -- the same '
            'trail this ledger carries as `W-ORD-LI-WEIL-BRIDGE` (:3548; fired at b398, `(M)` refuted at b399, "two objects on their families, one '
            'question at the window" at b400, :4698), one trail under two IDs. Now stated beside it: the Weil-form obligation is compiled '
            '(`h2_sign_iff_rh`, T0) and the Li-form obligation is T1-lit (Li`s criterion, not compiled). | unpriced; b324 filed it as the arc`s most '
            'valuable open item | **THE AUTHOR\'S WORD** |', '',
            '**The Fano theorem:** found compiled (SIDE-fano-darkness `0f6ce5b`, `FanoTwoDarkness.second_moment`, integer point values); '
            'W-ORD-FANO-DECIDE is not filed. SIDE-fano-darkness is one of eight repositories outside b542`s enumeration.', '',
            '**A correction to b544`s record:** `OPEN_TRAILS.md`:11097 reads "no I row concludes re = 1/2"; one does -- `side_exclusion_bridge`, '
            'under `RHHypothesis` (`FINDINGS.md`:5457), as `(R155)`(1) enters it. b544`s line is not edited.', '',
            '**Next:** FACES_OF_H2_AT_FINITE_INSTANCE with FACES_LEDGER.', '',
            '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s · (N6) %s.** The seat`s own: (S1) %s, (S2) %s, (S3) %s. (N4) is held by the ruling`s '
            'grade, the seat`s read of :357`s clause held for the author`s word.' % tuple(w(sc[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
            '**No kernel lane opened at this act.** Nothing deposits; nothing at Zenodo written; no kernel edited; no monograph byte changed; ERRATA '
            'untouched; the ceiling unchanged; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN; nothing here is a statement about RH.', '']
    text = re.sub(r"(?<=[A-Za-z0-9)])`s\b", "'s", NL.join(body))
    if outside_bt(text):
        sys.exit('### UNBALANCED BACKTICKS IN THE TRAIL')
    before = open(OT, 'rb').read()
    if HEADING.encode('utf-8') in before:
        sys.exit('### ALREADY PRESENT')
    open(OT, 'ab').write(text.encode('utf-8'))
    after = open(OT, 'rb').read()
    out = dict(added=len(after) - len(before), prefix=after.startswith(before), headings=after.decode('utf-8').count(HEADING))
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(headings)d heading' % out)
    put_json('b545_trail_notes.json', out)


if __name__ == '__main__':
    fn = {'reads': reads, 'anchor': anchor, 'select': select, 'fano': fano, 'probe': probe, 'tiers': tiers, 'sentences': sentences,
          'write_tiers': write_tiers, 'write_sentences': write_sentences, 'joint': joint, 'credit': credit, 'findings': findings,
          'components': components, 'desk': desk, 'trail': trail}
    if len(sys.argv) < 2 or sys.argv[1] not in fn:
        sys.exit('usage: %s %s' % (sys.argv[0], ' | '.join(fn)))
    fn[sys.argv[1]]()
