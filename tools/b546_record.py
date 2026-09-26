# -*- coding: utf-8 -*-
"""b546_record.py -- CP-2 EXTENDED TO THE EIGHT; THE TWO FORMS; THE CREDIT; THE GEOMETRIES: THE RECORD, UNDER (R156).
### `python tools/b546_record.py reads | eight | probe_eight | premises | index | amend | spiral | forms_probe | mathlib | forms |
### credit | geometry | components | desk | trail`

### FINDINGS takes five appends, OPEN_TRAILS one, BALANCE_AND_POSITIVITY one line, SPIRAL_MAP one block. TECHNE-Core`s names
### never leave memory; a name of the eight equal to one of them is masked (READING (14)). This file deletes nothing.
"""
import hashlib, io, json, math, os, re, subprocess, sys, time
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
import b542_record as Q
import b544_probe_part as P
import b544_record as R4
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
FIND, OT = os.path.join(PP, 'FINDINGS.md'), os.path.join(PP, 'OPEN_TRAILS.md')
BAL = os.path.join(PP, 'phase1.5', 'spectral', 'BALANCE_AND_POSITIVITY.md')
SPIRAL = os.path.join(PP, 'SPIRAL_MAP.md')
SCR = os.environ.get('B546_SCRATCH', '')
PRIV = Q.PRIV
NL = chr(10)
EIGHT = ['SIDE-carrier-spec', 'SIDE-class-number-anomaly', 'SIDE-cosmo', 'SIDE-dirichlet-mod-24', 'SIDE-fano-darkness',
         'SIDE-formation-procedure', 'SIDE-local-cosmic-interface', 'SIDE-quaternionic-dark-sector']
MASK = '<a name shared with TECHNE-Core>'
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
    return Q.g(repo, *a)


def outside_bt(text):
    return sum(l.count('`') % 2 for l in text.split(NL))


_PRIV = None


def priv_names():
    global _PRIV
    if _PRIV is None:
        import b542_checks as K542
        _PRIV = set(K542.techne_private_names())
    return _PRIV


def mask(text):
    for n in priv_names():
        text = re.sub(r'(?<![A-Za-z0-9_])' + re.escape(n) + r'(?![A-Za-z0-9_])', MASK, text)
    return text


def append_to(path, text):
    text = re.sub(r"(?<=[A-Za-z0-9)])`s\b", "'s", text)
    if outside_bt(text):
        sys.exit('### UNBALANCED BACKTICKS IN THE APPEND TO %s' % path)
    if mask(text) != text:
        sys.exit('### A TECHNE-Core NAME WOULD BE WRITTEN -- REFUSED')
    before = open(path, 'rb').read()
    add = text.encode('utf-8')
    if not before.endswith(b'\n'):
        add = b'\n' + add
    open(path, 'ab').write(add)
    after = open(path, 'rb').read()
    return dict(file=os.path.relpath(path, PP), before=len(before), added=len(after) - len(before), prefix=after.startswith(before))


def heading_line(path, h):
    return rd(path).split(NL).index(h) + 1


def guard_absent(path, h):
    if h.encode('utf-8') in open(path, 'rb').read():
        sys.exit('### ALREADY PRESENT IN %s: %s' % (os.path.basename(path), h[:80]))


# ------------------------------------------------------------------------------ THE READS
PPREADS = [(SPIRAL, [(32, 230)], 'SPIRAL_MAP`s kernel tables, whole (sections 1-3)'),
           (FIND, [(4955, 4957), (5272, 5276), (5461, 5470), (5478, 5480)], 'CP-2, CP-3, the credit, b545`s entry'),
           (BAL, [(274, 274), (357, 357), (498, 512), (764, 772)], 'the two clauses, C.7.3`s Voros sentences, the two-forms block'),
           (OT, [(3548, 3548), (11103, 11122)], 'W-ORD-LI-WEIL-BRIDGE and b545`s merged entry')]


def reads():
    L = ['b546 -- THE ORDERED READS, CITED BY PATH AND LINE', '']
    base = os.path.join('D:', os.sep)
    dirs = sorted(d for d in os.listdir(base) if d.startswith('SIDE-') and os.path.isdir(os.path.join(base, d)))
    listed = [r for r, _, _ in Q.REPOS]
    sp = rd(SPIRAL)
    L.append('### the SIDE-* directories on D:\\ (%d), against b542`s list (tools/b542_record.py REPOS :80-101) and SPIRAL_MAP.md' % len(dirs))
    for d in dirs:
        isgit = subprocess.run(['git', '-C', os.path.join(base, d), 'rev-parse', '--git-dir'], capture_output=True).returncode == 0
        L.append('  %-34s git %-5s in b542 %-5s SPIRAL_MAP lines naming it %d' % (d, isgit, d in listed, sp.count(d)))
    for p, spans, what in PPREADS:
        t = rd(p).split(NL)
        L += ['', '### %s -- %s' % (os.path.relpath(p, PP).replace(os.sep, '/'), what)]
        for a, z in spans:
            L += ['  :%d %s' % (i + 1, t[i][:700]) for i in range(a - 1, min(z, len(t)))]
    L += ['', '### relay tools/b542_record.py:80-101 -- b542`s REPOS'] + ['  :%d %s' % (i + 1, l) for i, l in enumerate(rd(os.path.join(T, 'b542_record.py')).split(NL)) if 79 <= i <= 100]
    L += ['', '### relay data/b522_results.json'] + ['  ' + l for l in rd(os.path.join(D, 'b522_results.json')).split(NL)]
    L += ['', '### relay data/b523_results.json'] + ['  ' + l for l in rd(os.path.join(D, 'b523_results.json')).split(NL)]
    L += ['', '### relay data/b506_c2_results.json -- found (the completed Q0 bank`s zeros off the line, t < 150)']
    for x in jl('b506_c2_results.json')['found']:
        L.append('  sigma %.10f  t %.10f  col %s' % (x['rho'][0], x['rho'][1], x['col']))
    t = g('SIDE-li-map', 'show', '73cee42:LiLinearMap.lean').replace(chr(13), '').split(NL)
    L += ['', '### SIDE-li-map 73cee42 LiLinearMap.lean:56-60'] + ['  :%d %s' % (i + 1, t[i]) for i in range(55, 60)]
    L += ['', '### relay data/b545_probes.txt (lam_add`s profile at 73cee42)'] + ['  ' + l for l in rd(os.path.join(D, 'b545_probes.txt')).split(NL) if 'lam_add' in l]
    put_txt('b546_reads.txt', [mask(l) for l in L])
    print('  reads banked : %d lines' % len(L))


# ------------------------------------------------------------------------------ COMPONENT 1: THE EIGHT (READINGS (1)-(5))
def union_decls():
    pins = [(r, cited or 'HEAD') for r, cited, _ in Q.REPOS] + [(r, 'HEAD') for r in EIGHT]
    decls = []
    for r, pin in pins:
        files = sorted(f for f in g(r, 'ls-tree', '-r', '--name-only', pin).split(NL) if f.endswith('.lean'))
        for f in files:
            raw = g(r, 'show', '%s:%s' % (pin, f))
            ns = P.namespaces(raw)
            for x in Q.scan_file(raw, [], set()):
                x.update(repo=r, pin=pin, file=f, namespace=ns[x['line'] - 1] if x['line'] - 1 < len(ns) else '',
                         private=bool(re.match(r'^\s*(?:@\[[^\]]*\]\s*)?(?:\w+\s+)*private\s', x['statement'])))
                decls.append(x)
    return decls


def eight():
    t0 = time.time()
    ds, fednames = P.classify(union_decls())
    old = jl('b544_decls.json')
    oldsub = {(x['repo'], x['file'], x['line']): x['subject'] for x in old['decls']}
    moved = []
    from collections import Counter
    per = {}
    for x in ds:
        per.setdefault(x['repo'], Counter())[x['subject']] += 1
        k = (x['repo'], x['file'], x['line'])
        if x['repo'] not in EIGHT and k in oldsub and oldsub[k] != x['subject']:
            moved.append(dict(repo=x['repo'], file=x['file'], line=x['line'], was=oldsub[k], now=x['subject'],
                              name=('(private)' if x['repo'] == PRIV else x['full'])))
    oldn = [x for x in ds if x['repo'] not in EIGHT]
    new = [x for x in ds if x['repo'] in EIGHT]
    heads = {r: dict(head=g(r, 'rev-parse', 'HEAD').strip(), tags=[t for t in g(r, 'tag').split() if t],
                     clean=g(r, 'status', '--porcelain', '--untracked-files=no').strip() == '') for r in EIGHT}
    rows = [{k: (mask(x[k]) if isinstance(x[k], str) else x[k]) for k in ('repo', 'pin', 'file', 'line', 'kw', 'name', 'full', 'namespace', 'private', 'statement', 'zeta', 'prog', 'subject')}
            for x in new]
    res = dict(count_union=len(ds), count_old_here=len(oldn), count_old_b544=old['count'], count_eight=len(new),
               subjects_old_b544=old['subjects'], subjects_old_union=dict(Counter(x['subject'] for x in oldn)),
               subjects_eight=dict(Counter(x['subject'] for x in new)), per_repo_eight={r: dict(per.get(r, {})) for r in EIGHT},
               moved=moved, heads=heads, seconds=round(time.time() - t0, 1), masked=sum(1 for x in rows if MASK in x['full']), decls=rows)
    put_json('b546_eight.json', res)
    print('  union %d declarations ; old repositories here %d (b544 %d) ; the eight %d ; %.0f s' % (len(ds), len(oldn), old['count'], len(new), res['seconds']))
    print('  old subjects b544 %s' % old['subjects'])
    print('  old subjects under the union %s ; moved %d' % (res['subjects_old_union'], len(moved)))
    for m in moved[:40]:
        print('    moved %s %s:%d %s -> %s %s' % (m['repo'], m['file'], m['line'], m['was'], m['now'], m['name']))
    print('  the eight %s' % res['subjects_eight'])
    for r in EIGHT:
        print('    %-32s HEAD %s tags %s clean %s %s' % (r, heads[r]['head'][:10], heads[r]['tags'], heads[r]['clean'], res['per_repo_eight'][r]))
    print('  masked names %d' % res['masked'])
    for x in rows:
        if x['subject'] == 'ZETA':
            print('    ZETA %s %s:%d %s %s %s' % (x['repo'], x['file'], x['line'], x['kw'], x['full'], x['zeta']))


def vacuous(name, bank):
    """### READINGS (4)-(5) applied to the eight`s ZETA terminals -- when there are none, the component says VACUOUS and banks it"""
    ej = jl('b546_eight.json')
    z = [x for x in ej['decls'] if x['subject'] == 'ZETA']
    res = dict(component=name, zeta_rows=len(z), verdict=('VACUOUS -- the eight add no ZETA row, so nothing is %s' % bank) if not z else 'NOT VACUOUS')
    put_json('b546_%s.json' % name, res)
    print('  %s : %s' % (name, res['verdict']))
    if z:
        sys.exit('### THE EIGHT CARRY ZETA ROWS -- this component must run in full, not as a vacuous bank')


def probe_eight():
    vacuous('probe_eight', 'probed')


def premises():
    vacuous('premises', 'tested for premises')


def index():
    vacuous('index', 'marked E/I')


# ------------------------------------------------------------------------------ COMPONENT 2: THE TWO FORMS, FRESH (READING (9))
PRINT_ANY = re.compile(r"'(.+?)'[ \t]+(does not depend on any axioms|depends on axioms: \[[^\]]*\])")
FORMS = [('SIDE-explicit-formula', ['SIDEExplicitFormula.Seam'], ['SIDEExplicitFormula.B321.h2_sign_iff_rh']),
         ('SIDE-lv-conservation', ['SIDELvConservation.PartialPositivity'],
          ['SIDELvConservation.PartialPositivity.blTerm_nonneg_of_onLine', 'SIDELvConservation.PartialPositivity.partialPositivity_finiteRange',
           'SIDELvConservation.PartialPositivity.lowFinset_mem_iff'])]


def forms_part():
    """### the author`s word after the host memory stop: one repository per foreground run, each banked as it prints, in the order
    ### lam_add, h2_sign_iff_rh, then the lv three. `python tools/b546_record.py forms_part li | ef | lv | stmts`"""
    part = sys.argv[2]
    res = jl('b546_forms_probe.json') or {}
    txtp = os.path.join(D, 'b546_forms_probe.txt')
    L = rd(txtp).rstrip(NL).split(NL) if os.path.exists(txtp) else ['b546 -- THE TWO FORMS, FRESH `#print axioms` (READING (9)), one repository per foreground run']
    if part == 'li':
        tc = 'leanprover/lean4:v4.29.0-rc8'
        s = g('SIDE-li-map', 'show', '73cee42:LiLinearMap.lean').replace(chr(13), '') + NL + '#print axioms LiLinearMap.lam_add' + NL + '#check @LiLinearMap.lam_add' + NL
        t0 = time.time()
        r = subprocess.run(['lean', '+' + tc, '--stdin'], input=s, capture_output=True, text=True, encoding='utf-8', errors='replace')
        out = (r.stdout + r.stderr).replace(chr(13), '')
        res['SIDE-li-map'] = dict(head='73cee42', clean=True, exit=r.returncode, seconds=round(time.time() - t0, 1),
                                  profiles={m.group(1): m.group(2) for m in PRINT_ANY.finditer(re.sub(r'\n\s+', ' ', out))})
        L += ['', '### SIDE-li-map 73cee42 LiLinearMap.lean by stdin (%s) ; exit %d ; %.0f s' % (tc, r.returncode, time.time() - t0)] + ['  ' + l for l in out.split(NL) if l.strip()]
    elif part in ('ef', 'lv'):
        repo, mods, names = FORMS[0] if part == 'ef' else FORMS[1]
        head = g(repo, 'rev-parse', 'HEAD').strip()
        dirty = g(repo, 'status', '--porcelain', '--untracked-files=no').strip()
        src = ['import ' + m for m in mods] + [''] + ['#print axioms ' + n for n in names] + ['#check @' + n for n in names]
        p = os.path.join(SCR, 'b546_forms_%s.lean' % repo)
        io.open(p, 'w', encoding='utf-8', newline=NL).write(NL.join(src) + NL)
        t0 = time.time()
        r = subprocess.run(['lake', 'env', 'lean', p], cwd=os.path.join('D:', os.sep, repo), capture_output=True, text=True, encoding='utf-8', errors='replace')
        out = (r.stdout + r.stderr).replace(chr(13), '')
        res[repo] = dict(head=head, clean=not dirty, exit=r.returncode, seconds=round(time.time() - t0, 1),
                         profiles={m.group(1): m.group(2) for m in PRINT_ANY.finditer(re.sub(r'\n\s+', ' ', out))})
        L += ['', '### %s HEAD %s (tree %s) ; exit %d ; %.0f s' % (repo, head, 'clean' if not dirty else 'DIRTY', r.returncode, time.time() - t0)]
        L += ['  ' + l for l in out.split(NL) if l.strip()]
    elif part == 'stmts':
        cmp = []
        for repo, path, name, pins in [('SIDE-explicit-formula', 'SIDEExplicitFormula/Seam.lean', 'h2_sign_iff_rh', ['5c72cad', 'HEAD']),
                                       ('SIDE-lv-conservation', 'SIDELvConservation/PartialPositivity.lean', 'blTerm_nonneg_of_onLine', ['v0.8.0', 'v0.10.0', 'HEAD']),
                                       ('SIDE-lv-conservation', 'SIDELvConservation/PartialPositivity.lean', 'partialPositivity_finiteRange', ['v0.8.0', 'v0.10.0', 'HEAD']),
                                       ('SIDE-lv-conservation', 'SIDELvConservation/PartialPositivity.lean', 'lowFinset_mem_iff', ['v0.8.0', 'v0.10.0', 'HEAD'])]:
            ss = {p: stmt_at(repo, p, path, name) for p in pins}
            base = ss[pins[-1]]
            cmp.append(dict(repo=repo, name=name, statements=ss, same={p: (ss[p] == base) if ss[p] else None for p in pins}))
            L.append('  statement %-32s %s' % (name, {p: ('SAME' if ss[p] == base else ('ABSENT' if ss[p] is None else 'DIFFERENT')) for p in pins}))
        res['statements'] = cmp
    put_json('b546_forms_probe.json', res)
    put_txt('b546_forms_probe.txt', L)
    print(NL.join(L[-14:]))


def stmt_at(repo, rev, path, name):
    t = g(repo, 'show', '%s:%s' % (rev, path)).replace(chr(13), '').split(NL)
    i = next((k for k, l in enumerate(t) if re.match(r'^(theorem|lemma)\s+%s\b' % re.escape(name), l)), None)
    if i is None:
        return None
    buf = []
    for l in t[i:i + 40]:
        buf.append(l)
        if ':=' in l:
            break
    return ' '.join(' '.join(buf).split()).split(':=')[0]


def forms_probe():
    L, res = ['b546 -- THE TWO FORMS, FRESH `#print axioms` (READING (9))'], {}
    for repo, mods, names in FORMS:
        head = g(repo, 'rev-parse', 'HEAD').strip()
        dirty = g(repo, 'status', '--porcelain', '--untracked-files=no').strip()
        src = ['import ' + m for m in mods] + [''] + ['#print axioms ' + n for n in names] + ['#check @' + n for n in names]
        p = os.path.join(SCR, 'b546_forms_%s.lean' % repo)
        io.open(p, 'w', encoding='utf-8', newline=NL).write(NL.join(src) + NL)
        t0 = time.time()
        r = subprocess.run(['lake', 'env', 'lean', p], cwd=os.path.join('D:', os.sep, repo), capture_output=True, text=True, encoding='utf-8', errors='replace')
        out = (r.stdout + r.stderr).replace(chr(13), '')
        prof = {m.group(1): m.group(2) for m in PRINT_ANY.finditer(re.sub(r'\n\s+', ' ', out))}
        res[repo] = dict(head=head, clean=not dirty, exit=r.returncode, seconds=round(time.time() - t0, 1), profiles=prof)
        L += ['', '### %s HEAD %s (tree %s) ; exit %d ; %.0f s' % (repo, head, 'clean' if not dirty else 'DIRTY', r.returncode, time.time() - t0)]
        L += ['  ' + l for l in out.split(NL) if l.strip()]
    # ### lam_add at 73cee42: vanilla Lean, the file fed to stdin -- no file written
    tc = 'leanprover/lean4:v4.29.0-rc8'
    s = g('SIDE-li-map', 'show', '73cee42:LiLinearMap.lean').replace(chr(13), '') + NL + '#print axioms LiLinearMap.lam_add' + NL + '#check @LiLinearMap.lam_add' + NL
    r = subprocess.run(['lean', '+' + tc, '--stdin'], input=s, capture_output=True, text=True, encoding='utf-8', errors='replace')
    out = (r.stdout + r.stderr).replace(chr(13), '')
    res['SIDE-li-map'] = dict(head='73cee42', clean=True, exit=r.returncode, profiles={m.group(1): m.group(2) for m in PRINT_ANY.finditer(re.sub(r'\n\s+', ' ', out))})
    L += ['', '### SIDE-li-map 73cee42 LiLinearMap.lean by stdin (%s) ; exit %d' % (tc, r.returncode)] + ['  ' + l for l in out.split(NL) if l.strip()]
    # ### the statements across pins, by text
    def stmt(repo, rev, path, name):
        t = g(repo, 'show', '%s:%s' % (rev, path)).replace(chr(13), '').split(NL)
        i = next((k for k, l in enumerate(t) if re.match(r'^(theorem|lemma)\s+%s\b' % re.escape(name), l)), None)
        if i is None:
            return None
        buf = []
        for l in t[i:i + 40]:
            buf.append(l)
            if ':=' in l:
                break
        return ' '.join(' '.join(buf).split()).split(':=')[0]
    cmp = []
    for repo, path, name, pins in [('SIDE-explicit-formula', 'SIDEExplicitFormula/Seam.lean', 'h2_sign_iff_rh', ['5c72cad', 'HEAD']),
                                   ('SIDE-lv-conservation', 'SIDELvConservation/PartialPositivity.lean', 'blTerm_nonneg_of_onLine', ['v0.8.0', 'v0.10.0', 'HEAD']),
                                   ('SIDE-lv-conservation', 'SIDELvConservation/PartialPositivity.lean', 'partialPositivity_finiteRange', ['v0.8.0', 'v0.10.0', 'HEAD']),
                                   ('SIDE-lv-conservation', 'SIDELvConservation/PartialPositivity.lean', 'lowFinset_mem_iff', ['v0.8.0', 'v0.10.0', 'HEAD'])]:
        ss = {p: stmt(repo, p, path, name) for p in pins}
        base = ss[pins[-1]]
        cmp.append(dict(repo=repo, name=name, statements=ss, same={p: (ss[p] == base) if ss[p] else None for p in pins}))
        L.append('  statement %-32s %s' % (name, {p: ('SAME' if ss[p] == base else ('ABSENT' if ss[p] is None else 'DIFFERENT')) for p in pins}))
    res['statements'] = cmp
    put_json('b546_forms_probe.json', res)
    put_txt('b546_forms_probe.txt', L)
    print(NL.join(L))


MLDIR = os.path.join('D:', os.sep, 'SIDE-explicit-formula', '.lake', 'packages', 'mathlib')
ML_NEEDLES = [('Li coefficient (an identifier)', r'(?<![A-Za-z])(?:li|Li)(?:Coeff|Coefficient|_coeff|Criterion|_criterion|Seq|Number)\w*|\bliCoeff'),
              ('Li (the word, in any text)', r'(?<![A-Za-z])Li(?![A-Za-z])'),
              ('Keiper', r'(?i)keiper'),
              ('logDeriv of the completed zeta', r'logDeriv[^\n]{0,60}completedRiemannZeta|logDeriv[^\n]{0,60}riemannZeta|logDeriv[^\n]{0,40}(?:Λ|xi)'),
              ('deriv of the completed zeta', r'deriv[^\n]{0,40}completedRiemannZeta'),
              ('riemannZeta at 1 (pole / residue / constant term)', r'riemannZeta_residue|tendsto_riemannZeta_sub_one_div|riemannZeta_one\b|zeta_sub_one|residue[^\n]{0,40}riemannZeta|riemannZeta[^\n]{0,60}eulerMascheroni|eulerMascheroni[^\n]{0,60}riemannZeta'),
              ('xi / riemannXi', r'riemannXi|RiemannXi|\bxi\b[^\n]{0,30}[Zz]eta'),
              ('Stieltjes constants', r'(?i)stieltjes'),
              ('Taylor coefficients of zeta', r'(?i)taylor[^\n]{0,40}zeta|iteratedDeriv[^\n]{0,40}(?:riemannZeta|completedRiemannZeta)'),
              ('explicit formula / Guinand / Weil', r'(?i)explicit formula|explicitFormula|guinand|weil[^\n]{0,30}(?:formula|criterion|explicit)')]


ML_V2 = [('riemannZeta at 1, v2 (a zeta function on the line)', r'(?:riemannZeta|completedRiemannZeta|hurwitzZeta|LSeries)[^\n]{0,80}(?:residue|sub_one|one_sub|eulerMascheroni|tendsto|pole|\(1\)|_one\b)|(?:residue|eulerMascheroni|pole)[^\n]{0,80}(?:riemannZeta|completedRiemannZeta)'),
         ('Stieltjes constants, v2', r'(?i)stieltjes[ _]?const'),
         ('explicit formula, v2 (with zeta, primes or von Mangoldt)', r'(?i)guinand|weil[^\n]{0,30}(?:formula|criterion|explicit)|explicit formula[^\n]{0,80}(?:zeta|prime|L-function|mangoldt)|(?:zeta|prime|mangoldt)[^\n]{0,80}explicit formula')]


def mathlib():
    global ML_NEEDLES
    ML_NEEDLES = ML_NEEDLES + [x for x in ML_V2 if x not in ML_NEEDLES]
    head = subprocess.run(['git', '-C', MLDIR, 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()
    files = []
    for dp, dn, fs in os.walk(os.path.join(MLDIR, 'Mathlib')):
        files += [os.path.join(dp, f) for f in fs if f.endswith('.lean')]
    hits = {n: [] for n, _ in ML_NEEDLES}
    for f in files:
        t = rd(f)
        for i, l in enumerate(t.split(NL), 1):
            for n, p in ML_NEEDLES:
                if re.search(p, l):
                    hits[n].append(dict(file=os.path.relpath(f, MLDIR).replace(os.sep, '/'), line=i, text=l.strip()[:220]))
    L = ['b546 -- THE MATHLIB SEARCH (READING (9)): the checkout SIDE-explicit-formula builds against, %s ; %d .lean files under Mathlib/' % (head, len(files))]
    for n, p in ML_NEEDLES:
        L.append('')
        L.append('### %s : %d hits ; needle %s' % (n, len(hits[n]), p))
        L += ['  %s:%d %s' % (h['file'], h['line'], h['text']) for h in hits[n][:60]]
        if len(hits[n]) > 60:
            L.append('  ... %d more (all in data/b546_mathlib.json)' % (len(hits[n]) - 60))
    put_json('b546_mathlib.json', dict(head=head, files=len(files), needles=ML_NEEDLES, hits=hits, counts={n: len(v) for n, v in hits.items()}))
    put_txt('b546_mathlib.txt', L)
    for n, _ in ML_NEEDLES:
        print('  %-52s %d' % (n, len(hits[n])))


# ------------------------------------------------------------------------------ COMPONENT 1 (c), (d): THE AMENDMENTS AND THE ROWS
CP2A = '## Amendment to the T0 inventory (CP-2, FINDINGS.md:4955): the eight repositories the enumeration missed, under (R156)(3)'
CP3A = '## Amendment to the inequality index (CP-3, FINDINGS.md:5272): the eight repositories the enumeration missed, under (R156)(3)'
SPIRALH = '## 2B. Kernels added by b546 under (R156)(3) -- eight repositories on disk that no row of this map named (appended 2026-09-26; no byte above changes)'
PURPOSE_LINE = {'SIDE-carrier-spec': 2, 'SIDE-class-number-anomaly': 2, 'SIDE-cosmo': 2, 'SIDE-dirichlet-mod-24': 2, 'SIDE-formation-procedure': 2,
                'SIDE-local-cosmic-interface': 2, 'SIDE-quaternionic-dark-sector': 2}


def fmt(d):
    return ' · '.join('%s %d' % (k, d.get(k, 0)) for k in ('ZETA', 'ARITHMETIC-OR-LOGIC', 'PROGRAMME-TYPE'))


def aol_eight():
    """### the eight`s ARITHMETIC-OR-LOGIC terminals, profiled only from a relay bank (READING (4)): the terminal table`s PROFILED rows and b545`s probes"""
    ej = jl('b546_eight.json')
    prof = {}
    for x in jl('terminal_table.json').get('rows', []):
        if x.get('profile_state') == 'PROFILED':
            prof[(x['repo'], x['name'].split('.')[-1])] = x['profile']
    for repo, v in jl('b545_probes.json').items():
        for full, p in (v.get('profiles') or {}).items():
            if p:
                prof[(repo, full.split('.')[-1])] = p
    rows = []
    for x in ej['decls']:
        if x['subject'] == 'ARITHMETIC-OR-LOGIC' and x['kw'] in ('theorem', 'lemma'):
            v = prof.get((x['repo'], x['name'].split('.')[-1]))
            rows.append(dict(repo=x['repo'], file=x['file'], line=x['line'], full=x['full'], profile=v, t0=R4.prof_class(v) in ('none', 'std3-or-fewer')))
    return rows


def amend():
    guard_absent(FIND, CP2A)
    ej = jl('b546_eight.json')
    old = jl('b544_decls.json')
    t0 = jl('b544_t0.json')
    moved = ej['moved']
    who = {}
    for m in moved:
        st = next((x['statement'] for x in old['decls'] if (x['repo'], x['file'], x['line']) == (m['repo'], m['file'], m['line'])), '')
        toks = set(t.split('.')[-1] for t in re.findall(r'[A-Za-z_][A-Za-z0-9_₀.]*', st))
        who[m['name']] = sorted(set(y['name'].split('.')[-1] for y in ej['decls'] if y['kw'] in P.BODYKW) & toks)
    new_tot = {k: ej['subjects_old_union'].get(k, 0) + ej['subjects_eight'].get(k, 0) for k in ('ZETA', 'ARITHMETIC-OR-LOGIC', 'PROGRAMME-TYPE')}
    a8 = aol_eight()
    a8t0 = [r for r in a8 if r['t0']]
    L = ['', CP2A, '',
         '*Appended by b546; no byte of the entry at :4955 changes. The eight SIDE-* repositories on D:\\ outside b542`s list '
         '(`tools/b542_record.py` REPOS :80-101) are each unlisted in SPIRAL_MAP.md -- no row, no mention under another name -- so each '
         'is read at HEAD. b544`s engine was run over b542`s list and the eight together, the subject test reading the federation names '
         'of the union. Bank: relay `data/b546_eight.json`.*', '',
         '| repository | HEAD | tags | ZETA | ARITHMETIC-OR-LOGIC | PROGRAMME-TYPE |', '|:--|:--|:--|--:|--:|--:|']
    for r in EIGHT:
        c = ej['per_repo_eight'][r]
        L.append('| %s | `%s` | %s | %d | %d | %d |' % (r, ej['heads'][r]['head'][:7], ', '.join(ej['heads'][r]['tags']) or '--',
                                                      c.get('ZETA', 0), c.get('ARITHMETIC-OR-LOGIC', 0), c.get('PROGRAMME-TYPE', 0)))
    L += ['',
          '**The counts, old beside new.** Declarations: b544 %d; now %d (the old repositories %d, the eight %d). Subjects of the old '
          'repositories at b544: %s; under the union: %s -- %d row moved (%s). The eight: %s. The federation now: %s.'
          % (ej['count_old_b544'], ej['count_union'], ej['count_old_here'], ej['count_eight'], fmt(ej['subjects_old_b544']),
             fmt(ej['subjects_old_union']), len(moved),
             '; '.join('`%s` at %s %s:%d, %s to %s, because `%s` is now also defined in one of the eight' % (m['name'], m['repo'], m['file'], m['line'], m['was'], m['now'], ', '.join(who[m['name']]) or '?') for m in moved),
             fmt(ej['subjects_eight']), fmt(new_tot)), '',
          '**The ZETA terminals are unchanged.** The eight add no ZETA row: the fresh probe, the premise test and the E/I mark of '
          'READINGS (4)-(5) had no row to read -- VACUOUS, and said so (relay `data/b546_probe_eight.json`, `data/b546_premises.json`). '
          'The ZETA inventory stays 295 terminals, 245 premise-free at the standard three.', '',
          '**The arithmetic-or-logic terminals.** b544 listed %d premise-free at the standard three of %d (%d with no banked profile). '
          'The eight carry %d arithmetic-or-logic terminals; %d have a profile in a relay bank, all at the standard three or fewer, and '
          'enter the list: %s. The rest have no banked profile and are not profiled here.'
          % (len(t0['arithmetic_or_logic']), t0['aol_total'], t0['aol_unprofiled'], len(a8), len(a8t0),
             ', '.join('`%s` (%s)' % (r['full'], r['profile'].replace('depends on axioms: ', '').replace('does not depend on any axioms', 'no axioms')) for r in a8t0)), '',
          '**SIDE-fano-darkness`s `FanoTwoDarkness.second_moment`** (`0f6ce5b`) enters as b545 graded it: T0, the second-moment identity '
          'for integer point values, [propext, Quot.sound], premise-free; its subject by the rule is ARITHMETIC-OR-LOGIC (a statement '
          'about `Int`).', '']
    out2 = append_to(FIND, NL.join(L))
    out2['heading_line'] = heading_line(FIND, CP2A)
    L3 = ['', CP3A, '',
          '*Appended by b546; no byte of the entry at :5272 changes.*', '',
          '**The index is unchanged.** Its rows are the ZETA declarations and the window modules; the eight add no ZETA declaration and '
          'carry no window file, so the index keeps its %d rows (I %d, E %d), and its one I row concluding re = 1/2 stays '
          '`SIDEBridge.side_exclusion_bridge`, under `RHHypothesis`. The E/I mark had no row of the eight to read -- VACUOUS, and said so '
          '(relay `data/b546_index.json`).' % (jl('b544_index.json')['counts']['rows'], jl('b544_index.json')['counts']['I'], jl('b544_index.json')['counts']['E']), '']
    out3 = append_to(FIND, NL.join(L3))
    out3['heading_line'] = heading_line(FIND, CP3A)
    put_json('b546_amend.json', dict(cp2=out2, cp3=out3, new_totals=new_tot, aol_eight=len(a8), aol_eight_t0=[r['full'] for r in a8t0], moved_why=who))
    print('  CP-2 amendment :%d ; CP-3 amendment :%d ; new totals %s ; aol eight %d, t0 %d %s' % (out2['heading_line'], out3['heading_line'], new_tot, len(a8), len(a8t0), who))


def spiral():
    guard_absent(SPIRAL, SPIRALH)
    ej = jl('b546_eight.json')
    a8 = aol_eight()
    L = ['', '<!-- b546 (R156)(3) ROWS, 2026-09-26 -->', '', SPIRALH, '',
         '*Appended by b546 under the author`s ruling `(R156)`(3). b545`s Fano search found these eight git repositories on D:\\ outside '
         'b542`s enumeration; none is named anywhere in this map. Each row: the repository, its purpose quoted from its README, its pin '
         '(HEAD, with its tags), and a profile summary from this act`s banks (relay `data/b546_eight.json`). Adding a row confers no '
         'grade.*', '',
         '| Kernel | Pin | Purpose (its README) | Profile summary (b546) |', '|---|---|---|---|']
    for r in EIGHT:
        c = ej['per_repo_eight'][r]
        if r == 'SIDE-fano-darkness':
            purpose = '(no README; its file header) Fano Two-Darkness -- the incidence certificate'
        else:
            lines = [l.strip() for l in g(r, 'show', 'HEAD:README.md').replace(chr(13), '').split(NL) if l.strip()]
            purpose = lines[PURPOSE_LINE[r] - 1] if len(lines) >= PURPOSE_LINE[r] else '--'
            purpose = re.sub(r'\*\*', '', purpose).split('. ')[0].rstrip('.') + '.'
        prof = ('%d declarations: ZETA %d, arithmetic-or-logic %d, programme-type %d; no ZETA row, so no probe'
                % (sum(c.values()), c.get('ZETA', 0), c.get('ARITHMETIC-OR-LOGIC', 0), c.get('PROGRAMME-TYPE', 0)))
        banked = [x for x in a8 if x['repo'] == r and x['t0']]
        if banked:
            prof += '; banked profiles: %d terminals at the standard three or fewer (b545`s probes)' % len(banked)
        L.append('| `%s` *(added by b546)* | HEAD `%s`%s | %s | %s |' % (r, ej['heads'][r]['head'][:7],
                                                                   (' · tags ' + ', '.join(ej['heads'][r]['tags'])) if ej['heads'][r]['tags'] else ' · untagged',
                                                                   purpose.replace('|', '/'), prof))
    L += ['', '*Filed by b546. No byte above this block changes.*', '']
    out = append_to(SPIRAL, NL.join(L))
    out['heading_line'] = heading_line(SPIRAL, SPIRALH)
    out['rows'] = len(EIGHT)
    put_json('b546_spiral.json', out)
    print('  SPIRAL_MAP block :%d ; %s' % (out['heading_line'], out))


# ------------------------------------------------------------------------------ COMPONENT 2: THE TWO FORMS ENTRY
FORMSH = ('## Weil`s criterion and Li`s criterion in the federation: the Weil form compiled, the Li form cited, the compiled Li-side '
          'pieces named, the bridge priced')


def pshort(v):
    return (v or 'NOT PRINTED').replace('depends on axioms: ', '').replace('does not depend on any axioms', 'no axioms')


def forms():
    FH = FORMSH.replace('`s', "'s")
    guard_absent(FIND, FH)
    fp, mj = jl('b546_forms_probe.json'), jl('b546_mathlib.json')
    ef, lv, li = fp['SIDE-explicit-formula'], fp['SIDE-lv-conservation'], fp['SIDE-li-map']
    for k, v in (('ef', ef), ('lv', lv), ('li', li)):
        if v['exit'] != 0 or not v['profiles']:
            sys.exit('### THE %s PROBE DID NOT PRINT -- the entry is not written' % k)
    same = {c['name']: c['same'] for c in fp['statements']}
    c = mj['counts']
    L = ['', FORMSH, '',
         '*Filed at b546 on the author`s ruling `(R156)`(1). Every profile below is a fresh `#print axioms` of this act (relay '
         '`data/b546_forms_probe.txt`); the Mathlib searched is the checkout SIDE-explicit-formula builds against, `%s` (relay '
         '`data/b546_mathlib.txt`).*' % mj['head'][:12], '',
         '**The Weil form, compiled.** `SIDEExplicitFormula.B321.h2_sign_iff_rh : h2_sign ↔ RiemannHypothesis` -- SIDE-explicit-formula '
         'v0.2 = `5c72cad` (Seam.lean`s blob identical at `81ae175`, probed at `81ae175`, tree clean): %s. Both directions, no premise; '
         '`h2_sign` is the sign `0 ≤ poleTerm k - primeSum k + archTerm k` over `classK`.' % pshort(ef['profiles'].get('SIDEExplicitFormula.B321.h2_sign_iff_rh')), '',
         '**The Li form, cited.** RH ⟺ (∀ n ≥ 1, λ_n ≥ 0) is Li 1997 and Bombieri–Lagarias 1999. No declaration of the federation states '
         'it: the pentagon`s `R4_positivity_to_RH` takes the criterion as its hypothesis. It is T1-lit.', '',
         '**The Li-side pieces that are compiled, named as what they are.**',
         '- `LiLinearMap.lam_add` (SIDE-li-map `73cee42`): the Li map`s linearity over integer coefficient streams, `lam (η + η′) n = lam η n + lam η′ n`; %s; no zeta in its statement.' % pshort(li['profiles'].get('LiLinearMap.lam_add')),
         '- `PartialPositivity.blTerm_nonneg_of_onLine` (SIDE-lv-conservation, v0.8.0; statement %s at v0.10.0 and HEAD `2f71068`): each Bombieri–Lagarias term of a zero on the line is nonnegative; %s.'
         % ('the same' if all(v in (True,) for v in same['blTerm_nonneg_of_onLine'].values() if v is not None) else 'CHANGED', pshort(lv['profiles'].get('SIDELvConservation.PartialPositivity.blTerm_nonneg_of_onLine'))),
         '- `PartialPositivity.partialPositivity_finiteRange` (v0.10.0): λ_n ≥ 0 for 1 ≤ n ≤ N₀(T), under `VerifiedZerosTo T` (numerical), `ExplicitFormulaDecomp` and `TailBoundPremise` (literature); %s. T1-lit.'
         % pshort(lv['profiles'].get('SIDELvConservation.PartialPositivity.partialPositivity_finiteRange')),
         '- `PartialPositivity.lowFinset_mem_iff` (v0.10.0): the finite set of zeros below height T, the finite-set conjunct; %s.'
         % pshort(lv['profiles'].get('SIDELvConservation.PartialPositivity.lowFinset_mem_iff')), '',
         '**The bridge, priced -- W-ORD-LI-WEIL-BRIDGE (OPEN_TRAILS.md:3548), under which W-ORD-MARGIN-BRIDGE is merged.** The Li '
         'coefficients are the values of the Weil functional at the Li test family, through the Guinand–Weil explicit formula '
         '(Bombieri–Lagarias 1999, Theorem 2, as Voros §4 cites it). *What Mathlib holds toward it* (`%s`, %d files searched): ζ’s pole at 1 '
         '(`riemannZeta_residue_one`) and its constant term γ (`tendsto_riemannZeta_sub_one_div`), and the zeros as a closed discrete set, '
         'finite in every compact (`riemannZetaZeros`, `IsCompact.inter_riemannZetaZeros_finite`); and nothing past that: Li coefficient '
         '(an identifier) %d hits, Keiper %d, the logarithmic derivative of the completed zeta %d, a ξ %d, Taylor coefficients of zeta %d, '
         'Stieltjes constants %d, an explicit formula for ζ %d (the one v2 hit is a finite Fourier formula on `ZMod`). *What the kernel would '
         'need*, in lemmas: (i) the Li test function g_n on (0, ∞) and its Mellin transform 1 − (1 − 1/s)^n; (ii) the kernel`s explicit '
         'formula, compiled for compactly supported C² test functions, extended to g_n, which is not compactly supported -- a limit over '
         'the class with the order-≤1 growth (compiled) and the zero count (the kernel`s `HCount`) as the dominating bounds; (iii) λ_n '
         'defined as the zero sum Σ_ρ [1 − (1 − 1/ρ)^n] with its convergence; (iv) RH ⟹ λ_n ≥ 0 from `blTerm_nonneg_of_onLine` and (iii); '
         '(v) the converse, Bombieri–Lagarias`s multiset lemma, the one step of real analytic content. With (iii)-(v) the Li form is T0 '
         'against `RiemannHypothesis` on its own; with (i)-(ii) as well, λ_n is tied to the compiled Weil form, which is the bridge. A sixth, '
         'the Hadamard product of ξ, is needed only if λ_n is to be the Taylor coefficient of log ξ at 1 rather than the zero sum. Priced '
         'here; not attempted.'
         % (mj['head'][:12], mj['files'], c['Li coefficient (an identifier)'], c['Keiper'], c['logDeriv of the completed zeta'], c['xi / riemannXi'],
            c['Taylor coefficients of zeta'], c['Stieltjes constants, v2'], c['explicit formula, v2 (with zeta, primes or von Mangoldt)']), '',
         '*Nothing deposits; nothing here is a statement about RH.*', '']
    out = append_to(FIND, NL.join(L))
    out['heading_line'] = heading_line(FIND, FH)
    put_json('b546_forms.json', out)
    print('  FINDINGS two-forms entry :%d ; %s' % (out['heading_line'], out))


# ------------------------------------------------------------------------------ COMPONENT 3: THE CREDIT CORRECTED
CREDIT_F = ('**The credit at :5461, corrected by appended line, 2026-09-26 (b546, `(R156)`(2)).** The credit attaches to :274`s clause, '
            '"outside it the T1 identity itself needs continuation" -- the sentence that anticipated b538. :357`s "RH-strength on the '
            'half-plane where T1 holds" is C₂ at Φ, proved (`C2_halfplane_nonvanishing_at_Phi`, SIDE-lv-conservation `v0.10.0`), and '
            'STANDS as that. The entry at :5461 is not edited.')
CREDIT_B = ('**Line appended 2026-09-26 by b546 under `(R156)`(2), beside the sentence read`s rows for :274 and :357 (the block at '
            ':704).** B.6(4)`s credit attaches to :274`s clause, "outside it the T1 identity itself needs continuation", which '
            'anticipated b538; :357`s "RH-strength on the half-plane where T1 holds" is C₂ at Φ, proved (`C2_halfplane_nonvanishing_at_Phi`), '
            'and STANDS as that. Nothing above this line is edited.')


def credit():
    guard_absent(FIND, poss(CREDIT_F[:60]))
    f0, b0 = rd(FIND).split(NL), rd(BAL).split(NL)
    before = dict(find_5461=f0[5460], find_tail=f0[-2:], bal_274=b0[273][:200], bal_357=b0[356], bal_tail=b0[-2:])
    o1 = append_to(FIND, NL + CREDIT_F + NL)
    o2 = append_to(BAL, NL + CREDIT_B + NL)
    f1, b1 = rd(FIND).split(NL), rd(BAL).split(NL)
    after = dict(find_5461=f1[5460], find_line=len(f1) - 1, bal_274=b1[273][:200], bal_357=b1[356], bal_line=len(b1) - 1)
    put_json('b546_credit.json', dict(findings=o1, balpos=o2, before=before, after=after))
    print('  BEFORE : :5461 %s' % before['find_5461'][:120])
    print('           BALPOS :357 %s' % before['bal_357'][:120])
    print('  AFTER  : :5461 %s (unchanged %s) ; the FINDINGS line at :%d' % (after['find_5461'][:60], before['find_5461'] == after['find_5461'], after['find_line']))
    print('           BALPOS :357 unchanged %s ; :274 unchanged %s ; the BALPOS line at :%d' % (before['bal_357'] == after['bal_357'], before['bal_274'] == after['bal_274'], after['bal_line']))


def poss(t):
    return re.sub(r"(?<=[A-Za-z0-9)])`s\b", "'s", t)


# ------------------------------------------------------------------------------ COMPONENT 4: THE DETECTION GEOMETRIES
GEOH = ('## Two detection geometries for one obligation: the Weil-side width and order at Q0 against the Li-side index threshold')


def geometry():
    guard_absent(FIND, GEOH)
    res, reach, r523 = jl('b522_results.json'), jl('b522_reach.json'), jl('b523_results.json')
    cells = [json.loads(l) for l in rd(os.path.join(D, 'b522_cells.jsonl')).split(NL) if l.strip()]
    g0 = sorted(set(c['gamma0'] for c in cells))
    found = jl('b506_c2_results.json')['found']
    z0 = min(found, key=lambda x: abs(x['rho'][1] - g0[0]))
    top = max(found, key=lambda x: x['rho'][1])
    b = rd(BAL).split(NL)
    v500, v507 = b[499], b[506]
    n0, ntop = 2 * g0[0] ** 2, 2 * top['rho'][1] ** 2
    neg, pos = res['q']['h2_neg'], res['q']['h2_pos']
    def runs(xs):
        xs = sorted(int(x) for x in xs)
        out, s = [], xs[0]
        for a, bb in zip(xs, xs[1:] + [None]):
            if bb != a + 1:
                out.append('%d' % s if s == a else '%d-%d' % (s, a))
                s = bb
        return ', '.join(out)
    L = ['', GEOH, '',
         '*Filed at b546 on the author`s ruling `(R156)`(4). Graded READING: an observation read from the banks, not a theorem. Banks: '
         'relay `data/b522_results.json`, `data/b522_reach.json`, `data/b522_cells.jsonl`, `data/b523_results.json`, `data/b506_c2_results.json`; '
         'Voros`s sentences from BALANCE_AND_POSITIVITY.md:500 and :507. Nothing about ζ’s zeros is claimed.*', '',
         '**The Weil side, at Q0 (the Epstein control, disc −23, h = 3), read from b522 and b523.** The window`s order p = %d; the ordinate '
         'γ₀ = %s (the Q0 zero there: σ = %.6f, t = %.6f, from the completed bank). Widths in reach (the tail within the quadrature bound): '
         '%s; out of reach: %s. The Q0 quantity is negative beyond its bound at widths %s (%d widths) and positive at %s; the narrowest '
         'negative width is a = %s, and b523`s audit keeps all %d negative cells under the full bound. **The negative widths do not form '
         'one run from a = 34: the widths 36-38 are positive.** The detection width is read per zero (R131); b522`s bank carries one '
         'off-line pair, so it shows the cost at one distance from the line and one height, and cannot show how the cost varies with the '
         'distance or with the local density -- that shape is the reading of the power-window route (b533-b534), not a measurement here.'
         % (res['p'], ', '.join('%.6f' % x for x in g0), z0['rho'][0], z0['rho'][1], runs(res['within']), runs(res['outside']), runs(neg), len(neg),
            runs(pos), int(res['q']['narrowest']), r523['neg_full']), '',
         '**The Li side, Voros`s threshold, verbatim** (BALANCE_AND_POSITIVITY.md:500): %s -- and with the radical the second extraction '
         'recovered (:507): %s. So an off-line zero at height T registers for n ≳ 2T², a cost set by the height alone.' % (v500.lstrip('> '), v507.lstrip('> ')), '',
         '**The numbers.** At T = %.6f, 2T² = %.2f, about %d. The highest off-line zero of the Q0 bank below 150 is at t = %.6f (σ = %.6f), '
         'where 2T² = %.1f, about %d. (The Q0 zeros are Epstein zeros, not ζ’s; the arithmetic is the threshold`s formula at those heights.)'
         % (g0[0], n0, round(n0), top['rho'][1], top['rho'][0], ntop, round(ntop)), '',
         '**The observation, as a reading.** The programme holds two instruments on the one obligation. On the Weil side the cost of '
         'detecting an off-line zero is a window of width and order, which the power-window route reads as governed by the zero`s distance '
         'from the line and the local zero density at its height; on the Li side it is an index, governed by the height alone, n ≳ 2T². The '
         'two forms detect the same zero at costs of different shape; the bridge of W-ORD-LI-WEIL-BRIDGE, if compiled, would express one '
         'cost in the other`s variable.', '',
         '**What would refute it.** A compiled bridge showing the two costs to be one function of the zero`s coordinates. Short of that, '
         'the Weil side`s dependence on the distance is not measured in the banks read here (one pair), so the reading rests on b533-b534`s '
         'route for that part.', '',
         '*Nothing deposits; nothing here is a statement about RH.*', '']
    out = append_to(FIND, NL.join(L))
    out['heading_line'] = heading_line(FIND, GEOH)
    put_json('b546_geometry.json', dict(write=out, p=res['p'], gamma0=g0, z0=z0['rho'], top=top['rho'], n0=n0, ntop=ntop, neg=neg, pos=pos,
                                        within=res['within'], outside=res['outside'], narrowest=res['q']['narrowest'], survivors=r523['neg_full'],
                                        voros500=v500, voros507=v507,
                                        reach=[dict(a=x['a'], tail_over_Bprime=x['tail_over_Bprime'], within=x['within']) for x in reach['table']]))
    print('  FINDINGS geometries :%d ; 2T^2 %.2f (%d) and %.1f (%d) ; narrowest %s ; negative %s ; positive %s' % (out['heading_line'], n0, round(n0), ntop, round(ntop), res['q']['narrowest'], runs(neg), runs(pos)))


# ------------------------------------------------------------------------------ THE SCORES, THE DESK, THE COMPONENTS, THE TRAIL
LINK = ('https://www.space.com/astronomy/james-webb-space-telescope/james-webb-space-telescope-looks-back-in-time-finds-our-ancient-'
        'universe-wasnt-as-pure-as-we-thought')
BRAIN = ('- **Research-arc line, 2026-09-26 (a brainstorm, queued; not an act; `(R156)`(5)).** Source: %s -- bears on two Phase 2 objects: '
         'SIDE-cosmo`s Ω_b = 4/81 (Størmer) and the T₇ CMB pre-registered null. The cascade`s focus does not move.' % LINK)
PRIOR_PP = 'da94298'
WRITE_OK = {'FINDINGS.md', 'OPEN_TRAILS.md', 'phase1.5/spectral/BALANCE_AND_POSITIVITY.md', 'SPIRAL_MAP.md'}
HEADING = ('### b546 — CP-2 extended to the eight repositories, the two forms stated, the B.6(4) clause, the detection geometries '
           'entered, under (R156)')


def gitc(r, *a):
    return subprocess.run(['git', '-C', r] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout.strip()


def w(v):
    return 'VACUOUS' if v is None else ('HELD' if v else 'REFUTED')


def scores():
    ej, mj, gj = jl('b546_eight.json'), jl('b546_mathlib.json'), jl('b546_geometry.json')
    committed = gitc(PP, 'log', '-1', '--pretty=%s').startswith('b546 --')
    base = 'HEAD~1' if committed else 'HEAD'
    pref = {}
    for f in sorted(WRITE_OK):
        old = subprocess.run(['git', '-C', PP, 'show', '%s:%s' % (base, f)], capture_output=True).stdout
        new = open(os.path.join(PP, f), 'rb').read().replace(b'\r\n', b'\n')
        pref[f] = new.startswith(old)
    written = sorted(x for x in gitc(PP, 'diff', '--name-only', PRIOR_PP).split(NL) if x) if not committed else \
        sorted(x for x in gitc(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x)
    needle = 'https://' + 'zenodo' + '.org'
    zen = [x for x in os.listdir(T) if x.startswith('b546_') and needle in rd(os.path.join(T, x))]
    t = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    tok = sum(open(os.path.join(d0, f), 'rb').read().count(t) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b546_')) if t else None
    kernels = {k: gitc(os.path.join('D:', os.sep, k), 'status', '--porcelain', '--untracked-files=no') == ''
               for k in ['SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-explicit-formula', 'SIDE-global-section', 'SIDE-li-map'] + EIGHT}
    zeta8 = ej.get('subjects_eight', {}).get('ZETA', 0)
    sp = jl('b546_spiral.json')
    c = mj.get('counts', {})
    return dict(
        n1=zeta8 <= 5, n1_zeta=zeta8,
        n2=sp.get('rows', 0) >= 1, n2_rows=sp.get('rows', 0),
        n3=c.get('Li coefficient (an identifier)') == 0 and c.get('Keiper') == 0, n3_hits={k: c.get(k) for k in ('Li coefficient (an identifier)', 'Li (the word, in any text)', 'Keiper')},
        n4=round(gj.get('n0', 0)) == 531 and gj.get('narrowest') == 34.0 and jl('b522_results.json').get('p') == 7, n4_vals=(gj.get('n0'), gj.get('narrowest')),
        n5=all(pref.values()) and not zen and tok == 0 and all(kernels.values()) and set(written) <= WRITE_OK,
        prefixes=pref, written=written, zen=zen, token=tok, kernels=kernels,
        s1=zeta8 >= 1 and all(x['repo'] == 'SIDE-carrier-spec' for x in ej.get('decls', []) if x['subject'] == 'ZETA'),
        s2=c.get('riemannZeta at 1, v2 (a zeta function on the line)', 0) > 0 and c.get('Taylor coefficients of zeta') == 0 and c.get('xi / riemannXi') == 0
        and any('riemannZeta_residue_one' in h['text'] for h in mj.get('hits', {}).get('riemannZeta at 1, v2 (a zeta function on the line)', []))
        and any('tendsto_riemannZeta_sub_one_div' in h['text'] for h in mj.get('hits', {}).get('riemannZeta at 1, v2 (a zeta function on the line)', [])),
        s3=len(ej.get('moved', [])) <= 5, s3_moved=len(ej.get('moved', [])))


def desk():
    sc = scores()
    N, SS = ('n1', 'n2', 'n3', 'n4', 'n5'), ('s1', 's2', 's3')
    gj = jl('b546_geometry.json')
    L = ['=' * 104, 'b546 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '', '### THE NAVIGATOR`S FIVE.', '-' * 104,
         '  **(N1)** ### **%s.** -- the ZETA rows the eight add : %d.' % (w(sc['n1']), sc['n1_zeta']),
         '  **(N2)** ### **%s.** -- unlisted repositories given a SPIRAL_MAP row : %d of 8.' % (w(sc['n2']), sc['n2_rows']),
         '  **(N3)** ### **%s.** -- Mathlib hits : %s (the word "Li" is authors` names and the dilogarithm, hand-read).' % (w(sc['n3']), sc['n3_hits']),
         '  **(N4)** ### **%s.** -- 2T² at T = 16.290216 : %.2f ; narrowest negative width at p = 7 : %s ; in the same line: the negative widths are '
         '34-35 and 39-60, and 36-38 are positive.' % (w(sc['n4']), sc['n4_vals'][0] or 0, sc['n4_vals'][1]),
         '  **(N5)** ### **%s.** -- prefixes kept %s ; PLACE-papers files written %s ; tools naming the platform %s ; token %s ; kernels clean %s.'
         % (w(sc['n5']), sc['prefixes'], sc['written'], sc['zen'] or 'NONE', sc['token'], sc['kernels']),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- the eight add %d ZETA rows.' % (w(sc['s1']), sc['n1_zeta']),
         '  **(S2)** ### **%s.** -- Mathlib: riemannZeta_residue_one and tendsto_riemannZeta_sub_one_div present; Taylor coefficients 0; a xi 0.' % w(sc['s2']),
         '  **(S3)** ### **%s.** -- old rows whose subject moved under the union : %d.' % (w(sc['s3']), sc['s3_moved']),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in N].count(True), [sc[k] for k in N].count(False), [sc[k] for k in SS].count(True), [sc[k] for k in SS].count(False)),
         '', '### THIS ACT`S OWN DEFECTS.'] + ([l for l in rd(os.path.join(D, 'b546_defects.txt')).rstrip(NL).split(NL) if l]
                                              if os.path.exists(os.path.join(D, 'b546_defects.txt')) else ['    NONE RECORDED.']) + ['=' * 104]
    put_txt('b546_desk_notes.txt', L)
    put_json('b546_scores.json', sc)
    print(NL.join(L))


def components():
    L = ['=' * 132, 'b546 -- THE COMPONENTS, AS THEY RAN.', '=' * 132]
    ej = jl('b546_eight.json')
    L += ['### COMPONENT 1 -- THE EIGHT : ' + json.dumps({k: v for k, v in ej.items() if k != 'decls'}, ensure_ascii=False)]
    for n in ('b546_probe_eight.json', 'b546_premises.json', 'b546_index.json', 'b546_amend.json', 'b546_spiral.json'):
        L.append('### %s : %s' % (n, json.dumps(jl(n), ensure_ascii=False)))
    L += ['', '### COMPONENT 2 -- THE PROBES:'] + ['  ' + l for l in rd(os.path.join(D, 'b546_forms_probe.txt')).rstrip(NL).split(NL)]
    L += ['### THE MATHLIB SEARCH : ' + json.dumps(jl('b546_mathlib.json').get('counts'), ensure_ascii=False), '### THE ENTRY : ' + json.dumps(jl('b546_forms.json'))]
    L += ['### COMPONENT 3 -- THE CREDIT : ' + json.dumps(jl('b546_credit.json'), ensure_ascii=False)]
    gj = jl('b546_geometry.json')
    L += ['### COMPONENT 4 -- THE GEOMETRIES : ' + json.dumps({k: v for k, v in gj.items() if k != 'reach'}, ensure_ascii=False)]
    L += ['  a %5.1f  tail/B` %10.3f  within %s' % (x['a'], x['tail_over_Bprime'], x['within']) for x in gj.get('reach', [])]
    L += ['### COMPONENT 5 -- held at the seal (READING (12)); released on the author`s word (data/b546_author_word.txt); the line is in the trail: ' + BRAIN,
          '### THE BRANCHES : see data/b546_branches.txt', '=' * 132]
    put_txt('b546_components.txt', [mask(l) for l in L])
    print(NL.join(L[:5]))


def trail():
    sc, ej, am, sp = scores(), jl('b546_eight.json'), jl('b546_amend.json'), jl('b546_spiral.json')
    fo, cr, ge = jl('b546_forms.json'), jl('b546_credit.json'), jl('b546_geometry.json')
    body = ['', HEADING, '',
            '**(R156) ratified.** (1) The two forms: the Weil form compiled (`h2_sign_iff_rh`), the Li form cited (T1-lit), the compiled '
            'Li-side pieces named, the bridge priced. (2) The B.6(4) credit attached to :274`s clause. (3) CP-2 and CP-3 extended to the eight. '
            '(4) The detection geometries entered as a READING. (5) The brainstorm line -- held at the seal, released on the author`s word, below. (6) FACES_OF_H2_AT_FINITE_INSTANCE next.', '',
            '**Entered:** FINDINGS.md:%d (CP-2 amended), :%d (CP-3 amended), :%d (the two forms), :%d (the credit line), :%d (the geometries); '
            'SPIRAL_MAP.md:%d (eight rows added); BALANCE_AND_POSITIVITY.md:%d (the credit line).'
            % (am['cp2']['heading_line'], am['cp3']['heading_line'], fo['heading_line'], cr['after']['find_line'], ge['write']['heading_line'],
               sp['heading_line'], cr['after']['bal_line']), '',
            '**The eight:** all unlisted in SPIRAL_MAP; %d declarations, ZETA 0; the federation now %s. The ZETA inventory and the index are '
            'unchanged; one old row moved subject (`formationTotal` now also defined among the eight).'
            % (ej['count_eight'], ' · '.join('%s %d' % (k, v) for k, v in am['new_totals'].items())), '',
            '**Component 5 -- held at the seal (READING (12)), released on the author`s word** (relay `data/b546_author_word.txt`), which '
            'supplied the link verbatim. The one research-arc line, and nothing else from the thread:', '',
            BRAIN, '',
            '**W-ORD-LI-WEIL-BRIDGE** (:3548; W-ORD-MARGIN-BRIDGE merged under it) is priced at FINDINGS.md:%d in lemmas and not attempted; '
            'its trigger stays THE AUTHOR\'S WORD.' % fo['heading_line'], '',
            '**Next:** FACES_OF_H2_AT_FINITE_INSTANCE with FACES_LEDGER.', '',
            '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s.** The seat`s own: (S1) %s, (S2) %s, (S3) %s.'
            % tuple(w(sc[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 's1', 's2', 's3')),
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
    put_json('b546_trail_notes.json', out)


if __name__ == '__main__':
    fn = {'reads': reads, 'eight': eight, 'probe_eight': probe_eight, 'premises': premises, 'index': index, 'forms_probe': forms_probe,
          'mathlib': mathlib, 'amend': amend, 'spiral': spiral, 'forms': forms, 'credit': credit, 'geometry': geometry,
          'components': components, 'desk': desk, 'trail': trail, 'forms_part': forms_part}
    if len(sys.argv) < 2 or sys.argv[1] not in fn:
        sys.exit('usage: %s %s' % (sys.argv[0], ' | '.join(fn)))
    fn[sys.argv[1]]()
