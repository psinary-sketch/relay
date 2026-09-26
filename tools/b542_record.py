# -*- coding: utf-8 -*-
"""b542_record.py -- E-2026-09-25-5 FILED; THE INHERITANCE CENSUS ACROSS THE FEDERATION: THE RECORD, UNDER (R152).
### `python tools/b542_record.py reads | file | census | engines | probe | findings | rows | components | desk | trail`

### The federation is READ at its cited pins through `git show`, never checked out and never written. ERRATA takes one append and
### one bullet; FINDINGS one append; OPEN_TRAILS one; the correspondence ledger one row per INHERITS-kind terminal through the
### carried `corr_row.py`. TECHNE-Core is private: its statements are read in memory and no name or statement of it is written
### anywhere -- its rows are keyed by module and line and carry a hand-written shape. This file deletes nothing.
"""
import hashlib, io, json, os, re, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
ERR = os.path.join(PP, 'ERRATA.md')
FIND = os.path.join(PP, 'FINDINGS.md')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
SMAP = os.path.join(PP, 'SPIRAL_MAP.md')
LIVE = os.path.join(PP, 'day1', 'A_Place_to_Stand.md')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
CORR = os.path.join(SIDE, 'CORRESPONDENCE.md')
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
SCR = os.environ.get('B542_SCRATCH', '')
NL = chr(10)
PRIV = 'TECHNE-Core'
V3 = dict(rows=235, decls=5293, digest='39745dcde31d352736f347604a7d3362d9f8d409044e795309d11cea40129e72')
FTITLE = ("## The inheritance census: every compiled statement in the federation that mentions a zero of zeta or xi, by kind, "
          "with the per-class dichotomy for SIDE-kernel's seven classes")
HEADING = ('### b542 — E-2026-09-25-5 filed; the inheritance census across the federation under (R152): every compiled statement '
           'naming a zero of zeta or xi, by kind; the seven-class dichotomy')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rd(p):
    return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')


def jl(n):
    p = os.path.join(D, n)
    return json.loads(rd(p)) if os.path.exists(p) else {}


def put_json(n, obj):
    io.open(os.path.join(D, n), 'w', encoding='utf-8', newline=NL).write(json.dumps(obj, indent=1, ensure_ascii=False) + NL)


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
    return dict(file=os.path.relpath(path, PP) if path.startswith(PP) else path, before=len(before), added=len(after) - len(before),
                prefix=after.startswith(before))


def md5(p):
    return hashlib.md5(open(p, 'rb').read()).hexdigest()


def rpath(r):
    return os.path.join('D:', os.sep, 'MY-DOwnloads', PRIV) if r == PRIV else os.path.join('D:', os.sep, r)


def g(r, *a):
    return subprocess.run(['git', '-C', rpath(r)] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


# ------------------------------------------------------------------------------ the population (READING (1))
# (repo, cited pin or None for WORKING-HEAD, where the pin is cited: a needle that must stand on one SPIRAL_MAP line with the name)
REPOS = [
    ('SIDE-kernel', 'v1.5', 'SIDE-kernel v1.5 (`0e5233f`)'), ('SIDE-interfaces', 'v0.1.3', '| `SIDE-interfaces` | v0.1.3 |'),
    ('SIDE-effects', 'afa9ccf', '`afa9ccf`'), ('SIDE-archimedean', 'v0.1.0', '| `SIDE-archimedean` | v0.1.0 (`8019d9d`)'),
    ('SIDE-frobenius', 'v0.1.0', '| `SIDE-frobenius` | v0.1.0 (`2efe9f2`)'), ('SIDE-rcurve', 'v0.1.0', '| `SIDE-rcurve` | v0.1.0 (`d5f33b4`)'),
    ('SIDE-spinor', 'v0.1.0', '| `SIDE-spinor` | v0.1.0 (`b235bc6`)'), ('SIDE-simplicity', 'v0.1.0', '| `SIDE-simplicity` | v0.1.0 (`54ba4f3`)'),
    ('SIDE-window', 'v0.4.0', 'v0.4.0 (`1bd2865`)'), ('SIDE-global-section', None, None), ('SIDE-li-map', None, None),
    ('SIDE-trivium', None, '| `SIDE-trivium` | — |'), ('SIDE-grh-transfer', 'v0.4.0', '| `SIDE-grh-transfer` | v0.4.0 (`68ec127a`'),
    ('SIDE-explicit-formula', None, 'created `SIDE-explicit-formula` by vendoring'),
    ('SIDE-lv-conservation', 'v0.10.0', '| `SIDE-lv-conservation` | deposit-pin **v0.10.0** (`93c27ec`)'),
    ('SIDE-meta', 'v0.3', '| `SIDE-meta` | v0.3 |'), ('SIDE-bijection', 'v0.2.0', '| `SIDE-bijection` | v0.2.0 |'),
    ('SIDE-t7-topology-cmb', 'v0.3', '| `SIDE-t7-topology-cmb` | v0.3 (`8eb0d5a`)'), ('SIDE-omega-b', 'v0.1', '| `SIDE-omega-b` | v0.1 |'),
    ('SIDE-substrate-cluster', 'v0.4', '| `SIDE-substrate-cluster` | v0.4 |'), ('SIDE-coupling', 'v0.1', '| `SIDE-coupling` | v0.1 |'),
    ('SIDE-class-coupling', 'v0.1', '| `SIDE-class-coupling` | v0.1 |'), ('SIDE-formation-arithmetic', 'v0.1', '| `SIDE-formation-arithmetic` | v0.1 |'),
    ('SIDE-residual-bridge', 'v0.1', '| `SIDE-residual-bridge` | v0.1 |'), ('SIDE-orchestrator', 'v0.1', '| `SIDE-orchestrator` | v0.1 |'),
    ('SIDE-constants', '545dde2', '| `SIDE-constants` | (`545dde2`'), ('SIDE-spinor-calibration', None, 'SIDE-spinor-calibration'),
    ('SIDE-spinor-calibration-mathlib', 'v0.1.0', '`SIDE-spinor-calibration-mathlib` v0.1.0'), ('SIDE-dark-interface', None, '`SIDE-dark-interface`'),
    ('SIDE-silence-principle', None, '`SIDE-silence-principle`'), ('SIDE-structural-error-correction', None, 'SIDE-structural-error-correction'),
    ('SIDE-cubit-axis', None, 'SIDE-cubit-axis'), ('SIDE-compression', None, 'SIDE-compression'),
    ('SIDE-yang-mills-formation', 'v0.1.1', '| `SIDE-bsd-*` / `SIDE-yang-mills-formation` | v0.1.1 |'),
    ('SIDE-bsd-formation-transfer', 'v0.1.1', '| `SIDE-bsd-*` / `SIDE-yang-mills-formation` | v0.1.1 |'),
    ('SIDE-bsd-multiplicity', 'v0.1.1', '| `SIDE-bsd-*` / `SIDE-yang-mills-formation` | v0.1.1 |'),
    (PRIV, None, None)]
NOT_READ = [('SIDE-interface-split', 'SPIRAL_MAP.md:274 -- removed at b390, a future kernel; ls-remote NOT FOUND'),
            ('SIDE-orchestrator-<a>-<b>', 'SPIRAL_MAP.md:160 -- a naming convention, not a repository')]

# ------------------------------------------------------------------------------ the census engine (READING (2)), probe v3 carried
NEEDLES = [('IsNontrivialZero', r'(?<![A-Za-z0-9_])IsNontrivialZero(?![A-Za-z0-9_])'),
           ('is_xi_zero', r'(?<![A-Za-z0-9_])is_xi_zero(?![A-Za-z0-9_])'),
           ('riemannZeta _ = 0', r'((?<![A-Za-z0-9_])riemannZeta(?![A-Za-z0-9_₀])|(?<![A-Za-z_])ζ(?![A-Za-z_₀\'′]))[^=≠\n]{0,80}(=|≠)\s*0(?![.0-9])'),
           ('completedRiemannZeta _ = 0', r'(?<![A-Za-z0-9_])completedRiemannZeta(?![A-Za-z0-9_₀])[^=≠\n]{0,80}(=|≠)\s*0(?![.0-9])'),
           ('completedRiemannZeta₀ _ = 0', r'(?<![A-Za-z0-9_])completedRiemannZeta₀[^=≠\n]{0,80}(=|≠)\s*0(?![.0-9])'),
           ('zetaZeroConfig', r'(?<![A-Za-z0-9_])zetaZeroConfig(?![A-Za-z0-9_])'),
           ('ZeroLoc', r'(?<![A-Za-z0-9_])ZeroLoc(?![A-Za-z0-9_])'),
           ('mellin Phi', r'mellin\s+\(?Phi\b'),
           ('zero structure field', r'^\s+zero\s*:')]
DOCNEEDLE = re.compile(r'zero of')
DECL = re.compile(r'^\s*(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable|partial|unsafe|nonrec|scoped)\s+)*(theorem|lemma|def|structure|class|instance|abbrev|axiom|opaque|inductive)\b')
KW = r'(theorem|lemma|def|structure|class|instance|abbrev|axiom|opaque|inductive)'
BODY = ('def', 'abbrev', 'structure', 'class', 'inductive', 'opaque', 'instance')
PROPLIKE = re.compile(r':\s*(Prop|Set\s+ℂ|Set\s+\(?ℂ|Type|ZeroConfig|Zeta23\.ZeroConfig|Finset\s+ℂ)\s*(:=|where)')


def blank_all_comments(text):
    res, i, n, depth, start = list(text), 0, len(text), 0, None
    while i < n:
        if depth == 0 and text[i] == '"':
            j = i + 1
            while j < n and text[j] != '"' and text[j] != NL:
                j += 2 if text[j] == '\\' else 1
            i = j + 1
            continue
        if text.startswith('/-', i):
            if depth == 0:
                start = i
            depth += 1
            i += 2
            continue
        if depth and text.startswith('-/', i):
            depth -= 1
            i += 2
            if depth == 0:
                for k in range(start, i):
                    if res[k] != NL:
                        res[k] = ' '
            continue
        if depth == 0 and text.startswith('--', i):
            j = text.find(NL, i)
            j = n if j < 0 else j
            for k in range(i, j):
                res[k] = ' '
            i = j
            continue
        i += 1
    return ''.join(res)


def stmt_end(L, Lc, i):
    depth = 0
    for j in range(i, min(len(L), i + 80)):
        s = Lc[j]
        if j > i and (DECL.match(s) or L[j].strip() == ''):
            return j - 1, 'next', None
        if j > i and s.lstrip().startswith('|') and depth <= 0:
            return j - 1, 'bar', None
        k = 0
        while k < len(s):
            c = s[k]
            if c in '([{⟨':
                depth += 1
            elif c in ')]}⟩':
                depth -= 1
            elif s.startswith(':=', k) and depth <= 0:
                return j, ':=', k
            elif s.startswith('where', k) and depth <= 0 and (k == 0 or not (s[k - 1].isalnum() or s[k - 1] == '_')) and not s[k + 5:k + 6].isalnum():
                return j, 'where', k
            k += 1
    return min(len(L), i + 80) - 1, 'cap', None


def body_end(L, Lc, i):
    for j in range(i + 1, min(len(L), i + 60)):
        if DECL.match(Lc[j]) or L[j].strip() == '' or (L[j][:1] not in (' ', '\t', '|') and L[j].strip()):
            return j - 1
    return min(len(L), i + 60) - 1


def decls_of(L, Lc):
    out = []
    for i, l in enumerate(Lc):
        m = DECL.match(l)
        if not m:
            continue
        kw = m.group(1)
        nm = re.search(KW + r'\s+([^\s:({\[]+)', l)
        name = nm.group(2) if nm else '(anonymous)'
        if kw in BODY:
            e, how, cut = body_end(L, Lc, i), 'body', None
        else:
            e, how, cut = stmt_end(L, Lc, i)
        out.append((i, e, kw, name, how, cut))
    return out


def scan_file(raw, extra, defines_nonzero):
    raw = raw.replace('\r', '')
    L, Lc = raw.split(NL), blank_all_comments(raw).split(NL)
    docmap = {}
    for m in re.finditer(r'/--.*?-/', raw, re.S):
        b = raw.count(NL, 0, m.end())
        j = b + 1
        while j < len(L) and (L[j].strip() == '' or L[j].strip().startswith('@[')):
            j += 1
        docmap[j] = m.group(0)
    xs = [x for x in extra if x not in defines_nonzero]
    pats = NEEDLES + [('via ' + x, r'(?<![A-Za-z0-9_])(?:[A-Za-z0-9_]+\.)*' + re.escape(x) + r'(?![A-Za-z0-9_₀])') for x in xs]
    rows = []
    for (a, e, kw, name, how, cut) in decls_of(L, Lc):
        segl = Lc[a:e + 1]
        if cut is not None:
            segl = segl[:-1] + [segl[-1][:cut]]
        seg = NL.join(segl)
        short = name.split('.')[-1]
        ns = set()
        for n, p in pats:
            if n == 'via ' + short and len(re.findall(p, seg, re.M)) <= 1:
                continue
            if re.search(p, seg, re.M):
                ns.add(n)
        if a in docmap and DOCNEEDLE.search(docmap[a]):
            ns.add('docstring "zero of"')
        rows.append(dict(line=a + 1, end_line=e + 1, kw=kw, name=name, needles=sorted(ns), end=how,
                         statement=NL.join(L[a:e + 1]) if cut is None else NL.join(L[a:e] + [L[e][:cut + 2]])))
    return rows


def scan(r, pin, extra, nonzero):
    rows = []
    for f in sorted(f for f in g(r, 'ls-tree', '-r', '--name-only', pin).split(NL) if f.endswith('.lean')):
        for x in scan_file(g(r, 'show', '%s:%s' % (pin, f)), extra, nonzero.get((r, f), set())):
            x.update(repo=r, pin=pin, file=f)
            rows.append(x)
    return rows


def derived_of(rows):
    out = set()
    for x in rows:
        if x['kw'] in BODY and any(not n.startswith('docstring') for n in x['needles']):
            if PROPLIKE.search(x['statement'].replace(NL, ' ')) or (x['kw'] in ('structure', 'class') and 'zero structure field' not in x['needles']):
                out.add(x['name'].split('.')[-1])
    return out


def run_census():
    extra = {'RiemannHypothesis'}
    for rnd in range(6):
        nonzero, allrows = {}, []
        for r, cited, _ in REPOS:
            allrows += scan(r, cited or 'HEAD', sorted(extra), {})
        for x in allrows:
            if not x['needles'] and x['kw'] in BODY:
                nonzero.setdefault((x['repo'], x['file']), set()).add(x['name'].split('.')[-1])
        allrows = []
        for r, cited, _ in REPOS:
            allrows += scan(r, cited or 'HEAD', sorted(extra), nonzero)
        rows = [x for x in allrows if x['needles']]
        new = derived_of(rows) | {'RiemannHypothesis'}
        if new == extra:
            break
        extra = new
    origin = {}
    for x in rows:
        if x['kw'] in BODY:
            origin.setdefault(x['name'].split('.')[-1], set()).add(x['repo'])
    return rows, sorted(extra), len(allrows), rnd, origin


def key_digest(rows):
    keys = sorted('%s|%s|%d|%s' % (r['repo'], r['file'], r['line'], ','.join(r['needles'])) for r in rows)
    return hashlib.sha256(NL.join(keys).encode()).hexdigest()


# ------------------------------------------------------------------------------ READING (4): the residue, by hand
RESIDUE = {
    ('SIDE-kernel', 'Kernel/Focus.lean', 'focus'): 'the imaginary part of completedRiemannZeta₀ on the line equals 0 -- a value, not a zero',
    ('SIDE-kernel', 'Kernel/SpectralCannonFull.lean', 'spectral_cannon'): 'the real part of the derivative of completedRiemannZeta₀ on the line equals 0 -- a value',
    ('SIDE-kernel', 'Kernel/ThomBridge.lean', 'focus_from_antisymmetry'): 'the imaginary part of completedRiemannZeta₀ on the line -- a value',
    ('SIDE-kernel', 'Kernel/ThomBridge.lean', 'c1_closing'): 'the imaginary part of completedRiemannZeta₀ on the line -- a value',
    ('SIDE-kernel', 'Kernel/Voice1Ext.lean', 'simplicity_forward'): 'a zero of the derivative, not of the function',
    ('SIDE-kernel', 'Kernel/Voice1Ext.lean', 'simplicity_backward'): 'a zero of the derivative, not of the function',
    ('SIDE-kernel', 'Kernel/Voice1Ext.lean', 'simplicity_iff'): 'a zero of the derivative, not of the function',
    ('SIDE-kernel', 'legacy/CodimProbe.lean', 'focus_on_critical_line'): 'legacy/: the imaginary part on the line -- a value',
    ('SIDE-kernel', 'legacy/SchwarzReflection_PR.lean', 'completedRiemannZeta₀_im_eq_zero_on_half'): 'legacy/: the imaginary part on the line -- a value',
    ('SIDE-global-section', 'Core/AggregationCircularityShadow.lean', 'Grp'): 'a group`s additive identity field named zero',
    ('SIDE-global-section', 'Core/AggregationCircularityShadow.lean', 'boolGrp'): 'a group`s additive identity field named zero',
}

# ------------------------------------------------------------------------------ READING (5): the kinds, typed from the pre-seal read
REASON = dict(
    DEF='a definition: no hypothesis and conclusion', PREM='the conclusion rests on a named premise equivalent to or restating RH',
    PROP='a relation between propositions about all the zeros', ANAL='an analytic identity, bound, sum, count or finiteness over the zeros',
    LOC='locates the zero (the strip, a trivial zero, a ball), not a constraint stated about zeta at it',
    FREE='a nonvanishing statement (a zero-free region)', MELLIN='a statement about the Mellin factor of Phi, not about a zero of xi or zeta',
    VAC='the conclusion follows from the hypotheses alone', CHAR='characterizes multiplicity or simplicity at a zero',
    ALG='algebra about a real sigma; the zero is only in the docstring', OBJ='INHERITS-SHAPE ON completedRiemannZeta₀, which is neither xi nor zeta',
    SEAM='asserts or builds the seam structure whose fields are INHERITS-kind', DEFEQ='unfolds a definition (rfl or simp)',
    ZSET='the zero sets of two functions agree', TRIV='concludes True', FORCES='FORCES', INHERITS='INHERITS')
K, E, EF, LV, GRH = 'SIDE-kernel', 'SIDE-explicit-formula', 'SIDE-explicit-formula', 'SIDE-lv-conservation', 'SIDE-grh-transfer'
C3N = 'C3 (functional equation): 1 − conj ρ is a zero'
GR = {
    (K, 'Bridge/ConservationBridge.lean', 'conservation_activates_balance'): ('NEITHER', 'PREM', 'INHERITS-shaped for C2 (the Euler balance at the zero`s real part) only under ConservationHypothesis, which is RH restated (ch_iff_rh); its conclusion is about sigma, not about xi'),
    (K, 'Bridge/ConservationBridge.lean', 'structural_exhaustiveness_proved'): ('NEITHER', 'PREM', ''),
    (K, 'Bridge/ConservationBridge.lean', 'riemann_hypothesis'): ('NEITHER', 'PREM', 'Route 3'),
    (K, 'Bridge/SIDEBridge.lean', 'xi_none_produces'): ('NEITHER', 'PREM', 'under RHHypothesis and SimplicityHypothesis; object completedRiemannZeta₀'),
    (K, 'Bridge/SIDEBridge.lean', 'side_exclusion_bridge'): ('NEITHER', 'PREM', 're = 1/2 is taken from RHHypothesis (RH restated for completedRiemannZeta₀), not derived'),
    (K, 'Bridge/TheBridgeComplete.lean', 'voice3_fe_zeros'): ('NEITHER', 'OBJ', 'the constraint is C3`s (1 − s is a zero), stated of completedRiemannZeta₀'),
    (K, 'Bridge/TheBridgeComplete.lean', 'voice7_zero_symmetry'): ('NEITHER', 'OBJ', 'the same statement as voice3_fe_zeros under C7`s name: C3`s constraint, not the Hadamard product'),
    (K, 'Bridge/Voice3_FE.lean', 'fe_forces_half'): ('NEITHER', 'VAC', 'both sides are 0 by the two hypotheses; object completedRiemannZeta₀; the name says forces, the statement does not'),
    (K, 'Kernel/AnalyticBridge.lean', 'simple_iff_order_one'): ('NEITHER', 'CHAR', 'object completedRiemannZeta₀'),
    (K, 'Kernel/Focus.lean', 'euler_closing'): ('NEITHER', 'FREE', 'riemannZeta s ≠ 0 for 1 ≤ re s (Mathlib)'),
    (K, 'Kernel/Integration.lean', 'rh_from_structural_exhaustiveness'): ('NEITHER', 'PREM', ''),
    (K, 'Kernel/Integration.lean', 'structural_exhaustiveness_from_rh'): ('NEITHER', 'PREM', ''),
    (K, 'Kernel/Integration.lean', 'structural_exhaustiveness_iff_rh'): ('NEITHER', 'PROP', 'StructuralExhaustiveness is RH restated'),
    (K, 'Kernel/PerpendicularCrossing.lean', 'proved_infrastructure'): ('NEITHER', 'FREE', 'its H3 conjunct; the other conjuncts are values of completedRiemannZeta₀'),
    (K, 'Kernel/ThomBridge.lean', 'c4_closing'): ('NEITHER', 'FREE', 'a zero-free half-plane under C4`s name, not a constraint at a zero'),
    (K, 'Kernel/Voice3b.lean', 'offLine_of_codim_two'): ('NEITHER', 'ALG', 'its conclusion is sigma ≠ 1/2'),
    (K, 'Kernel/Voice6.lean', 'c6_rests_at_half'): ('NEITHER', 'ALG', ''),
    (K, 'Kernel/XiDef.lean', 'rh_implies_mathlib_rh'): ('NEITHER', 'PREM', 'its hypothesis is RH restated through OffLineZero'),
    (K, 'legacy/CodimProbe.lean', 'euler_closing'): ('NEITHER', 'FREE', 'legacy/'),
    (K, 'legacy/CodimProbe.lean', 'zeros_in_strip'): ('NEITHER', 'LOC', 'legacy/'),
    (GRH, 'SIDEGRHTransfer/CharacterSymmetry.lean', 'paired_reflection_axis_invariant_iff'): ('FORCES', 'FORCES', 'an iff; its forward direction: if reflection keeps every point with re = sigma at re = sigma, sigma = 1/2 -- algebra, no zero in the statement (a docstring row); class: C3 for L-functions'),
    (GRH, 'SIDEGRHTransfer/CharacterTransfer.lean', 'twisted_balance_at_unramified_prime'): ('FORCES', 'FORCES', 'an iff; the twisted Euler balance forces s = 1/2 -- algebra about a real s, no zero in the statement (a docstring row); class: C2 for L-functions'),
}
_P = [('H2Bridge.lean', 'ch_imp_rh', 'PROP'), ('H2Bridge.lean', 'rh_imp_ch', 'PROP'), ('H2Bridge.lean', 'ch_iff_rh', 'PROP'),
      ('H2Bridge.lean', 'ch_imp_config', 'PROP'), ('H2Bridge.lean', 'ch_imp_h2_sign', 'PROP'), ('H2Bridge.lean', 'h2_sign_imp_ch_iff', 'PROP'),
      ('PowerLimit.lean', 'dominant_summable', 'ANAL'), ('PowerLimit.lean', 'fR_norm_le', 'ANAL'), ('PowerLimit.lean', 'fR_bound', 'ANAL'),
      ('PowerLimit.lean', 'rest_tendsto_zero', 'ANAL'), ('PowerLimit.lean', 'mem_sT', 'ANAL'), ('PowerLimit.lean', 'zeroSide_eventually_neg', 'ANAL'),
      ('PowerLimit.lean', 'zeroSideNeg_holds', 'ANAL'), ('PowerLimit.lean', 'h2_sign_imp_rh_strip_of', 'PROP'),
      ('PowerLimit.lean', 'h2_sign_imp_rh_strip', 'PROP'), ('PowerLimit.lean', 'rh_strip_imp_h2_sign', 'PROP'),
      ('PowerLimit.lean', 'h2_sign_iff_rh_strip', 'PROP'), ('PowerLimit.lean', 'h2_sign_imp_rh_of_seam', 'PROP'),
      ('PowerLimit.lean', 'ch_iff_h2_sign_of_seam', 'PROP'), ('PowerWindow.lean', 'dominant_exists', 'ANAL'),
      ('PowerWindow.lean', 'rh_imp_rh_strip', 'PROP'), ('RHChain.lean', 'rh_imp_h2_sign', 'PROP'), ('RHChain.lean', 'rh_imp_cell_form', 'PREM'),
      ('RegisterDepth.lean', 'mellin_Phi_eq_zero_of_re_le_one', 'MELLIN'), ('RegisterDepth.lean', 'lv_h2_false_on_strip', 'MELLIN'),
      ('RegisterDepth.lean', 'lvh2_corrected_iff', 'PROP'), ('RegisterDepth.lean', 'zeta_zeros_countable', 'ANAL'),
      ('RegisterDepth.lean', 'xi_zero_re_countable', 'ANAL'), ('RegisterDepth.lean', 'register5_output_holds', 'ANAL'),
      ('RestBound.lean', 'rest_bound_zeta', 'ANAL'), ('Seam.lean', 'zeta_zero_re_nonpos', 'LOC'), ('Seam.lean', 'rh_strip_imp_rh_holds', 'PROP'),
      ('Seam.lean', 'h2_sign_imp_rh_holds', 'PROP'), ('Seam.lean', 'h2_sign_iff_rh', 'PROP'), ('Seam.lean', 'h2_sign_imp_ch_holds', 'PROP'),
      ('Seam.lean', 'ch_iff_h2_sign', 'PROP')]
for f, n, c in _P:
    GR[(EF, 'SIDEExplicitFormula/' + f, n)] = ('NEITHER', c, '')
_Z = [('FromPNTPlus/ZetaBounds.lean', 'ZetaZeroFree', 'FREE'), ('FromPNTPlus/ZetaBounds.lean', 'ZetaNoZerosOn1Line', 'FREE'),
      ('FromPNTPlus/ZetaBounds.lean', 'ZetaNoZerosInBox', 'FREE'), ('FromPNTPlus/ZetaBounds.lean', 'LogDerivZetaHoloOn', 'ANAL'),
      ('RvM/CountByIntegral.lean', 'completedRiemannZeta_eq_zero_iff_of_re_pos', 'ZSET'),
      ('RvM/CountByIntegral.lean', 'completedRiemannZeta_ne_zero_of_one_le_re', 'FREE'),
      ('RvM/CountByIntegral.lean', 'completedRiemannZeta_ne_zero_of_re_nonpos', 'FREE'),
      ('RvM/CountByIntegral.lean', 'completedRiemannZeta_eq_zero_iff', 'ZSET'),
      ('RvM/CountByIntegral.lean', "rectangleIntegral'_logDeriv_completedZeta_eq_Ncount", 'ANAL'),
      ('RvM/LocalCount.lean', 'riemannZeta_zeros_finite_of_isCompact', 'ANAL'), ('RvM/LocalCount.lean', 'zetaZeroConfig_local_count', 'ANAL'),
      ('RvM/ZetaGrowth.lean', 'riemannZeta_ne_zero_of_two_le_re', 'FREE'), ('Statement.lean', 'IsNontrivialZero.not_trivial', 'LOC'),
      ('Statement.lean', 'RH_implies_on_line', 'PREM'), ('Statement.lean', 'RH_implies_all_on_line', 'PREM'), ('Statement.lean', 'trivial_chain', 'ANAL'),
      ('Statement/Seam.lean', 'riemannZeta_zeros_locallyFinite', 'ANAL'), ('Statement/Seam.lean', 'ZetaSeam.finite_window_holds', 'ANAL'),
      ('Statement/Seam.lean', 'ZetaSeam.of_reflect', 'SEAM'), ('Statement/SeamClosed.lean', 'zetaSeam', 'SEAM'),
      ('Statement/SeamClosed.lean', 'zerosIn_finite', 'ANAL'), ('Tail/Count.lean', 'sum_mult_le_of_windows', 'ANAL'),
      ('WeilEF/Contour.lean', 'rectangle_identity', 'ANAL'), ('WeilEF/FullLine.lean', 'completedZeta_ne_zero_on_horizontals', 'FREE'),
      ('WeilEF/FullLineAssembly.lean', 'full_line_identity', 'ANAL'), ('WeilEF/GoodHeights.lean', 'isNontrivialZero_of_mem_closedBall', 'LOC'),
      ('WeilEF/GoodHeights.lean', 'sum_mult_six_windows', 'ANAL'), ('WeilEF/GoodHeights.lean', 'card_le_sum_mult', 'ANAL'),
      ('WeilEF/GoodHeights.lean', 'good_heights_at', 'FREE'), ('WeilEF/GoodHeights.lean', 'good_heights', 'FREE'),
      ('WeilEF/Horizontal.lean', 'horizontal_vanish', 'ANAL'), ('WeilEF/Landau.lean', 'zeta_logDeriv_partial_fraction', 'ANAL'),
      ('WeilEF/Main.lean', 'EF_lit_zeta', 'ANAL'), ('WeilEF/Main.lean', 'EF_lit_zetaZeroConfig', 'ANAL'),
      ('WeilEF/XiLogDeriv.lean', 'logDeriv_completedZeta', 'ANAL'), ('WeilEF/XiLogDeriv.lean', 'completedZeta_zeros_strip', 'ZSET'),
      ('WeilEF/ZeroSumLimit.lean', 'zero_sum_limit', 'ANAL'), ('WeilEF/ZeroSummability.lean', 'zero_sum_inv_sq', 'ANAL'),
      ('WeilEF/ZeroSummability.lean', 'EF_zero_sum_summable', 'ANAL')]
for f, n, c in _Z:
    GR[(EF, 'Zeta23/' + f, n)] = ('NEITHER', c, '')
for n in ('zetaZeros_carrier', 'zetaZeros_mult', 'zetaZeros_simple', 'zetaZeros_window', 'zetaZeros_N', 'zetaZeros_Nd', 'zetaZeros_N0',
          'zetaZeros_N0star', 'zetaZeros_N0s', 'zetaZeros_Ns'):
    GR[(EF, 'Zeta23/Statement.lean', n)] = ('NEITHER', 'DEFEQ', '')
for n in ('zetaZeroConfig_carrier', 'zetaZeroConfig_mult', 'zetaZeroConfig_N', 'zetaZeroConfig_N0star', 'zetaZeroConfig_N0s', 'zetaZeroConfig_Nd'):
    GR[(EF, 'Zeta23/Statement/SeamClosed.lean', n)] = ('NEITHER', 'DEFEQ', '')
GR[(EF, 'Zeta23/ZetaReflect.lean', 'zeta_reflect_zero')] = ('INHERITS', 'INHERITS', 'class ' + C3N + ' (reflect ρ = 1 − conj ρ, Defs.lean:124); grade by statement DERIVES; does not force re = 1/2')
GR[(EF, 'Zeta23/ZetaReflect.lean', 'zeta_mult_reflect')] = ('INHERITS', 'INHERITS', 'class ' + C3N + ', its multiplicity twin; grade by statement DERIVES; does not force re = 1/2')
GR[(EF, 'Zeta23/Statement/Seam.lean', 'ZetaSeam.one_le_mult_holds')] = ('INHERITS', 'INHERITS', 'class none of C1-C7: the order of vanishing at a zero is at least one; grade by statement DERIVES; does not force re = 1/2')
_L = [('PartialPositivity.lean', 'blTerm_nonneg_of_onLine', 'ANAL'), ('PartialPositivity.lean', 'finite_setOf_abs_im_le', 'ANAL'),
      ('PartialPositivity.lean', 'mem_lowFinset', 'DEFEQ'), ('PartialPositivity.lean', 'lowFinset_mem_iff', 'DEFEQ'),
      ('PartialPositivity.lean', 'partialPositivity_finiteRange', 'ANAL'), ('RegisterPentagon.lean', 'goalState_of_h1_h2', 'MELLIN'),
      ('RegisterPentagon.lean', 'goalState_sevenClasses_of_h2', 'MELLIN'), ('RegisterPentagon.lean', 'R2_conservationHypothesis_to_RH', 'PROP'),
      ('RegisterPentagon.lean', 'R4_positivity_to_RH', 'PROP'), ('RegisterPentagon.lean', 'R5_output_HilbertPolya_to_RH', 'PROP'),
      ('RegisterPentagon.lean', 'certifiedInput_not_zeroRealizing', 'ANAL'), ('T2_SDarkness.lean', 'completedRiemannZeta_eq_mellinPhi', 'MELLIN'),
      ('T2_SDarkness.lean', 'T2d_zero_iff_mellinPhi_zero', 'MELLIN'), ('T3_StepNineBridge.lean', 'T3a_zeroLoc_is_function_of_Phi', 'MELLIN'),
      ('T3_StepNineBridge.lean', 'T3prime_shared_witness', 'MELLIN'), ('ZeroCarrier.lean', 'xiCarrier_eq_zero_iff_riemannZeta', 'ZSET'),
      ('ZeroCarrier.lean', 'finite_strip_box_riemannZeta_zeros', 'ANAL')]
for f, n, c in _L:
    GR[(LV, 'SIDELvConservation/' + f, n)] = ('NEITHER', c, '')

# TECHNE-Core (READING (8)): module and line -> kind, reason, a hand-written shape. No name of it appears in this file.
TP = 'TECHNE/Core/Instance/'
TECHNE = {
    ('ArtinSkeleton.lean', 34): ('NEITHER', 'PROP', 'theorem: (a GRH-form proposition) → (a conjecture proposition)'),
    ('ArtinSkeleton.lean', 48): ('NEITHER', 'DEF', 'abbrev: an alias of a zero-location type'),
    ('CramerSkeleton.lean', 50): ('NEITHER', 'TRIV', 'theorem: (a GRH-form proposition) → True'),
    ('DedekindZeta.lean', 46): ('NEITHER', 'DEF', 'structure: a real parameter with a zeta-zero predicate as a field'),
    ('DedekindZeta.lean', 50): ('NEITHER', 'DEF', 'instance: on-target sigma = 1/2 and off-target sigma ≠ 1/2 on that type'),
    ('DedekindZeta.lean', 69): ('NEITHER', 'DEF', 'def: a class-production predicate defined as False'),
    ('DedekindZeta.lean', 75): ('NEITHER', 'DEF', 'instance: a system whose production field is that False predicate'),
    ('DedekindZeta.lean', 90): ('NEITHER', 'DEF', 'def: an exhaustiveness proposition'),
    ('DedekindZeta.lean', 94): ('NEITHER', 'DEF', 'def: every location is on target (a BOTH-shaped definiens)'),
    ('DedekindZeta.lean', 100): ('NEITHER', 'DEF', 'def: a class exclusion discharged by unfolding the False predicate'),
    ('DedekindZeta.lean', 114): ('NEITHER', 'PROP', 'theorem: (an exhaustiveness proposition) → (every location on target)'),
    ('DedekindZeta.lean', 167): ('NEITHER', 'PROP', 'theorem: (a second exhaustiveness proposition) → (every location on target)'),
    ('DirichletGRH.lean', 44): ('NEITHER', 'DEF', 'def: a zero predicate whose body names no L-function (∃ t, ∃ a True witness, sigma ≠ 1/2 → False)'),
    ('DirichletGRH.lean', 59): ('NEITHER', 'DEF', 'structure: a real parameter with a zeta-zero field standing in for an L-function zero'),
    ('DirichletGRH.lean', 66): ('NEITHER', 'DEF', 'instance: on-target and off-target predicates as above'),
    ('DirichletGRH.lean', 85): ('NEITHER', 'DEF', 'def: a class-production predicate defined as False'),
    ('DirichletGRH.lean', 90): ('NEITHER', 'DEF', 'instance: a system whose production field is that False predicate'),
    ('DirichletGRH.lean', 105): ('NEITHER', 'DEF', 'def: an exhaustiveness proposition'),
    ('DirichletGRH.lean', 111): ('NEITHER', 'DEF', 'def: every location is on target (a BOTH-shaped definiens)'),
    ('DirichletGRH.lean', 117): ('NEITHER', 'DEF', 'def: a class exclusion discharged by unfolding the False predicate'),
    ('DirichletGRH.lean', 131): ('NEITHER', 'PROP', 'theorem: (an exhaustiveness proposition) → (every location on target)'),
    ('DirichletGRH.lean', 187): ('NEITHER', 'PROP', 'theorem: (a second exhaustiveness proposition) → (every location on target)'),
    ('KernelBridge.lean', 66): ('NEITHER', 'ZSET', 'theorem: two zero-at-real-part predicates are equivalent'),
    ('KernelBridge.lean', 83): ('NEITHER', 'PREM', 'theorem: (SIDE-kernel`s RH-restated premise) → (an exhaustiveness proposition)'),
    ('KernelBridge.lean', 95): ('NEITHER', 'PREM', 'theorem: (SIDE-kernel`s RH-restated premise) → (a local RH proposition)'),
    ('Xi.lean', 53): ('NEITHER', 'DEF', 'def: a nontrivial zeta zero at real part sigma'),
    ('Xi.lean', 63): ('NEITHER', 'DEF', 'structure: a real parameter with that zero predicate as a field'),
    ('Xi.lean', 67): ('NEITHER', 'DEF', 'instance: on-target and off-target predicates as above'),
    ('Xi.lean', 83): ('NEITHER', 'DEF', 'def: a class-production predicate defined as False'),
    ('Xi.lean', 86): ('NEITHER', 'DEF', 'instance: a system whose production field is that False predicate'),
    ('Xi.lean', 105): ('NEITHER', 'DEF', 'def: every location is on target (a BOTH-shaped definiens)'),
    ('Xi.lean', 110): ('NEITHER', 'DEF', 'def: a class exclusion discharged by unfolding the False predicate'),
    ('Xi.lean', 123): ('NEITHER', 'PROP', 'theorem: (an exhaustiveness proposition) → (every location on target)')}

# ------------------------------------------------------------------------------ READING (6): the dichotomy, SIDE-kernel v1.5
CLASSES = [
    ('C1_schwarz', 'conj ρ is a zero (R152)(4)', None, 'c1_exclusion', 'σ = 1 − σ (conjugation fixed point)',
     'ABSENT: no census statement concludes that conj ρ is a zero; the kernel`s c1_closing is a value statement (RESIDUE)'),
    ('C2_euler', 'the Euler balance at ρ.re (R152)(4)', 'conservation_activates_balance', 'c2_exclusion', '−σ = −(1 − σ) (the balance exponent)',
     'CONDITIONAL: conservation_activates_balance concludes the balance only under ConservationHypothesis, RH restated (ch_iff_rh) -- NEITHER, not T0'),
    ('C3_functional_eq', '1 − conj ρ is a zero (R152)(4)', 'zeta_reflect_zero', 'c3_exclusion', '1 − σ = σ (reflection fixed point)',
     'zeta_reflect_zero and zeta_mult_reflect (Zeta23, about zeta): INHERITS; the kernel`s own voice3_fe_zeros is INHERITS-SHAPE ON completedRiemannZeta₀'),
    ('C4_modular', 'as the kernel states it', None, 'c4_exclusion', '1 − σ = σ (the S-action fixed point)',
     'ABSENT: the kernel`s c4_closing is a zero-free half-plane (re ≥ 1), not a constraint at a zero'),
    ('C5_spectral', 'as the kernel states it', None, 'c5_exclusion', 'σ − 1/2 = 0 (the spectral offset)',
     'ABSENT: Register5_output is a definition; register5_output_holds holds trivially (b538) and constrains no zero'),
    ('C6_cauchy_riemann', 'the Cauchy–Riemann equations at ρ (R152)(4)', None, 'c6_exclusion', 'zero_codimension σ = 1 (model level)',
     'ABSENT: TheBridgeComplete.lean:239-242 names xi-faithfulness MANUSCRIPT-RESIDENT'),
    ('C7_hadamard', 'ρ appears in the Hadamard product (R152)(4)', None, 'c7_exclusion', 'hadamard_contrib σ = hadamard_contrib (1/2), hadamard_contrib := 0',
     'ABSENT: voice7_zero_symmetry states C3`s constraint on completedRiemannZeta₀ under C7`s name; ZetaSeam.one_le_mult_holds is the order of vanishing, not the product'),
]


def census():
    rows, derived, decls, rnd, origin = run_census()
    dig = key_digest(rows)
    priv_names = sorted(n for n, rs in origin.items() if rs == {PRIV})
    pub_derived = [x for x in derived if x not in priv_names]
    yields = {}
    for x in rows:
        for n in x['needles']:
            k = n if not (n.startswith('via ') and n[4:] in priv_names) else 'via (a TECHNE-Core name)'
            yields[k] = yields.get(k, 0) + 1
    out, residue, missing = [], [], []
    for x in rows:
        if x['repo'] == PRIV:
            f = x['file'][len(TP):] if x['file'].startswith(TP) else x['file']
            t = TECHNE.get((f, x['line']))
            if not t:
                missing.append(('TECHNE-Core', x['file'], x['line']))
                continue
            out.append(dict(repo=PRIV, pin='WORKING-HEAD', file=x['file'], line=x['line'], kw=x['kw'], kind=t[0], reason=t[1], note=t[2],
                            statement='(shape) ' + t[2], private=True))
            continue
        k = (x['repo'], x['file'], x['name'])
        if k in RESIDUE:
            residue.append(dict(repo=x['repo'], pin=x['pin'], file=x['file'], line=x['line'], name=x['name'], needles=x['needles'], reason=RESIDUE[k],
                                statement=x['statement']))
            continue
        if k in GR:
            kind, code, note = GR[k]
        elif x['kw'] in BODY:
            kind, code, note = 'NEITHER', 'DEF', ''
        else:
            missing.append(k)
            continue
        out.append(dict(repo=x['repo'], pin=x['pin'], file=x['file'], line=x['line'], end_line=x['end_line'], kw=x['kw'], name=x['name'],
                        needles=x['needles'], kind=kind, reason=code, note=note, statement=x['statement'], private=False))
    if missing:
        sys.exit('### UNTYPED THEOREM ROWS OR UNSHAPED TECHNE ROWS: %s' % missing)
    unused = [k for k in list(GR) + list(RESIDUE) if not any((r['repo'], r['file'], r.get('name')) == k for r in out + residue)]
    if unused:
        sys.exit('### TYPED ENTRIES MEETING NO CANDIDATE: %s' % unused)
    kinds = {k: sum(1 for r in out if r['kind'] == k) for k in ('INHERITS', 'FORCES', 'BOTH', 'NEITHER')}
    per = {}
    for r in out:
        per.setdefault(r['repo'], {k: 0 for k in ('rows', 'INHERITS', 'FORCES', 'BOTH', 'NEITHER')})
        per[r['repo']]['rows'] += 1
        per[r['repo']][r['kind']] += 1
    pins = []
    smap = rd(SMAP).split(NL)
    for r, cited, cite in REPOS:
        sha = g(r, 'rev-parse', (cited or 'HEAD') + '^{commit}').strip()
        head = g(r, 'rev-parse', 'HEAD').strip()
        live = (g(r, 'ls-remote', 'origin', 'refs/heads/main').split() or [''])[0]
        line = next((i + 1 for i, l in enumerate(smap) if cite and cite in l and (r in l or r.startswith('SIDE-bsd'))), None) if cite else None
        pins.append(dict(repo=r, cited=cited or 'WORKING-HEAD', sha=sha, head=head, live=live, live_eq_head=(live == head), map_line=line,
                         local=os.path.isdir(os.path.join(rpath(r), '.git')), rows=per.get(r, {}).get('rows', 0)))
    res = dict(v3=V3, run4=dict(rows=len(rows), decls=decls, digest=dig, rounds=rnd + 1), lineage_equal=(dig == V3['digest'] and len(rows) == V3['rows'] and decls == V3['decls']),
               needles=[n for n, _ in NEEDLES] + ['docstring "zero of"'], widenings=['(a) ≠ 0 and Zeta23`s local ζ', '(b) derived names, fixed point'],
               derived_public=pub_derived, derived_private_count=len(priv_names), yields=yields, pins=pins, not_read=NOT_READ,
               candidates=len(rows), residue=residue, rows=out, kinds=kinds, per_repo=per)
    put_json('b542_census.json', res)
    print('  ### needles : %s' % res['needles'])
    print('  ### derived names (public) : %s ; TECHNE-Core-only derived names : %d, not printed' % (pub_derived, len(priv_names)))
    print('  ### yields : %s' % yields)
    for p in pins:
        print('    %-34s pin %-12s %s  HEAD %s  live %s %s  map :%s  rows %d' % (p['repo'], p['cited'], p['sha'][:8], p['head'][:8], p['live'][:8],
                                                                             'EQ' if p['live_eq_head'] else 'DIFFER', p['map_line'], p['rows']))
    print('  ### NOT READ : %s' % NOT_READ)
    print('  ### lineage : v3 %s ; run 4 %s ; EQUAL %s' % (V3, res['run4'], res['lineage_equal']))
    print('  ### candidates %d ; residue %d ; rows %d ; kinds %s' % (len(rows), len(residue), len(out), kinds))
    print('  ### per repository : %s' % per)
    for r in out:
        if r['kind'] in ('INHERITS', 'FORCES', 'BOTH'):
            print('    %-9s %s %s:%d %s -- %s' % (r['kind'], r['repo'], r['file'], r['line'], r['name'], r['note']))
    dichotomy()


def kernel_forces():
    """the kernel`s FORCES cells, read at v1.5: produces_offline and each cN_exclusion, verbatim"""
    t = g('SIDE-kernel', 'show', 'v1.5:Bridge/TheBridgeComplete.lean').replace('\r', '').split(NL)
    out = {}
    po = next(i for i, l in enumerate(t) if l.startswith('noncomputable def produces_offline'))
    for c, _, _, ex, _, _ in CLASSES:
        pl = next(i for i in range(po, po + 12) if ('| .%s =>' % c) in t[i])
        body = t[pl] + ((' ' + t[pl + 1].strip()) if t[pl].rstrip().endswith('=>') else '')
        el = next(i for i, l in enumerate(t) if l.startswith('theorem %s ' % ex))
        out[c] = dict(produces_offline_line=pl + 1, produces_offline=body.strip(), exclusion_line=el + 1, exclusion=t[el].strip())
    return out


def dichotomy():
    cj = jl('b542_census.json')
    kf = kernel_forces()
    inh = {r['name']: r for r in cj['rows'] if r['kind'] == 'INHERITS'}
    table, fired = [], []
    for c, inh_c, inh_row, ex, force_c, cell in CLASSES:
        row = inh.get(inh_row) if inh_row else None
        same = (c == 'C2_euler')
        t0_inh = bool(row) and row['kind'] == 'INHERITS'
        table.append(dict(cls=c, inherits_constraint=inh_c, inherits_cell=cell, inherits_row=(('%s:%d %s' % (row['file'], row['line'], row['name'])) if row else
                                                                                                    ('ConservationBridge.lean:34 conservation_activates_balance (NEITHER, PREM)' if c == 'C2_euler' else 'ABSENT')),
                          forces_constraint=force_c, forces_cell='%s (TheBridgeComplete.lean:%d) through produces_offline :%d `%s`' % (
                              ex, kf[c]['exclusion_line'], kf[c]['produces_offline_line'], kf[c]['produces_offline'].lstrip('| ').strip()),
                          forces_grade=('FORCES by reading, T2 (definition-encoded: hadamard_contrib := 0)' if c == 'C7_hadamard' else
                                        'FORCES by reading, algebra about σ, names no zero (outside the census)'),
                          same_constraint=same, inherits_t0=t0_inh))
        if same and t0_inh:
            fired.append(c)
    res = dict(table=table, stop_fired=fired, forces_read=kf)
    put_json('b542_dichotomy.json', res)
    print('  ### THE SEVEN-CLASS DICHOTOMY (SIDE-kernel v1.5):')
    for d in table:
        print('    %-18s INHERITS [%s] %s' % (d['cls'], d['inherits_constraint'], d['inherits_row']))
        print('    %-18s FORCES   [%s] %s ; same constraint %s' % ('', d['forces_constraint'], d['forces_cell'], d['same_constraint']))
    print('  ### STOP (one constraint, both columns at T0) : %s' % ('FIRED ' + str(fired) if fired else 'NOT FIRED'))


# ------------------------------------------------------------------------------ the ordered reads
def reads():
    L = ['b542 -- THE ORDERED READS, CITED BY PATH AND LINE', '']
    d = rd(os.path.join(D, 'b541_erratum_draft.md'))
    L += ['### relay data/b541_erratum_draft.md : %d lines ; md5 %s ; rows %d' % (len(d.rstrip(NL).split(NL)), md5(os.path.join(D, 'b541_erratum_draft.md')),
                                                                              d.count('  - replacement: *"')),
          '  :1 ' + d.split(NL)[0]]
    e = rd(ERR).split(NL)
    a = next(i for i, l in enumerate(e) if l.startswith('<!-- b337 partition -->'))
    b = next(i for i, l in enumerate(e) if l.startswith('**INTERNAL-RECORD**'))
    L += ['', '### ERRATA.md partition block, :%d-:%d' % (a + 1, b + 1)] + ['  :%d %s' % (i + 1, e[i][:220]) for i in range(a, b + 1)]
    s = rd(SMAP).split(NL)
    L += ['', '### SPIRAL_MAP.md kernel tables (every line naming a SIDE- repository in a table row) and the rules read']
    L += ['  :%d %s' % (i + 1, l[:220]) for i, l in enumerate(s) if l.startswith('|') and 'SIDE-' in l and i < 300]
    L += ['  :%d %s' % (i + 1, s[i][:400]) for i in (262, 273)]
    for rel, lo, hi in (('Bridge/TheBridgeComplete.lean', 150, 252), ('Kernel/PoissonExhaustion.lean', 1, 10 ** 6),
                        ('Kernel/Integration.lean', 211, 229), ('Bridge/ConservationBridge.lean', 1, 10 ** 6), ('Kernel/XiDef.lean', 32, 42)):
        t = g('SIDE-kernel', 'show', 'v1.5:' + rel).replace('\r', '').split(NL)
        L += ['', '### SIDE-kernel v1.5 %s:%d-%d' % (rel, lo, min(hi, len(t)))] + ['  :%d %s' % (i + 1, t[i]) for i in range(lo - 1, min(hi, len(t)))]
    t = g('SIDE-lv-conservation', 'show', 'v0.10.0:SIDELvConservation/T3_StepNineBridge.lean').replace('\r', '').split(NL)
    L += ['', '### SIDE-lv-conservation v0.10.0 SIDELvConservation/T3_StepNineBridge.lean:44-70'] + ['  :%d %s' % (i + 1, t[i]) for i in range(43, 70)]
    m = rd(LIVE).split(NL)
    for h, stop in (('## 10.1 The Syllogism', '## 10.2'), ('## 15.4 Exhaustiveness', '## 15.5')):
        a = next(i for i, l in enumerate(m) if l.startswith(h))
        b = next(i for i in range(a + 1, len(m)) if m[i].startswith(stop))
        L += ['', '### day1/A_Place_to_Stand.md (v5.13) :%d-%d' % (a + 1, b)] + ['  :%d %s' % (i + 1, m[i]) for i in range(a, b) if m[i].strip()]
    io.open(os.path.join(D, 'b542_reads.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print('  reads banked : %d lines' % len(L))


# ------------------------------------------------------------------------------ COMPONENT 1
STATUS5 = ("**Filed 2026-09-25 by b542, the inheritance-census act, on the author's ruling (R152)(1), as drafted at relay "
           "data/b541_erratum_draft.md, its bytes unchanged; the heading's words \"DRAFT, NOT FILED\" and the Status line's \"DRAFT. Not "
           "filed.\" are the draft's, retained as drafted. Its two new kinds stand in its heading's own words: \"name terminals and a file no "
           "kernel holds\" (ProductFormula_Prime.lean and four terminals no version of SIDE-kernel holds) and \"read ... the perpendicular "
           "crossing past their compiled statements\" (four sentences that call the derivative of completedRiemannZeta₀ ξ′).**")
BULLET5 = ("- `E-2026-09-25-5` — *DEPOSIT-FACING; RETAINED AT MONOGRAPH v1.1.2* (appended to this list by b542 under `(R152)`(1))")
KIND_WORDS = ('name terminals and a file no kernel holds', 'the perpendicular crossing past their compiled statements')


def file():
    raw = open(ERR, 'rb').read()
    if b'## E-2026-09-25-5 ' in raw:
        sys.exit('### E-2026-09-25-5 IS ALREADY IN ERRATA -- REFUSING TO FILE IT TWICE.')
    draft = io.open(os.path.join(D, 'b541_erratum_draft.md'), encoding='utf-8').read()
    words = {w: (w in draft.split(NL)[0]) for w in KIND_WORDS}
    if not all(words.values()):
        sys.exit('### THE HEADING DOES NOT CARRY BOTH KINDS: %s' % words)
    lines = raw.decode('utf-8').split(NL)
    k = next(i for i, l in enumerate(lines) if l.startswith('- `E-2026-09-25-4` —'))
    before_lines = list(lines)
    lines = lines[:k + 1] + [BULLET5] + lines[k + 1:]
    open(ERR, 'wb').write(NL.join(lines).encode('utf-8'))
    kept = [l for i, l in enumerate(lines) if i != k + 1] == before_lines
    w = append_to(ERR, NL + draft.rstrip(NL) + NL + NL + STATUS5 + NL)
    t = rd(ERR).split(NL)
    first = next(i for i, l in enumerate(t) if l.startswith('## E-2026-09-25-5 ')) + 1
    last = next(i for i, l in enumerate(t) if l.startswith('**Filed 2026-09-25 by b542')) + 1
    entry = NL.join(t[first - 1:last])
    res = dict(bullet_line=k + 2, prior_lines_kept=kept, append=w, entry_lines=[first, last], entry_equals_draft=(draft.rstrip(NL) in entry),
               backticks_outside_code=outside_bt(entry), backticks=entry.count('`'), heading_kind_words=words)
    put_json('b542_file.json', res)
    print('  bullet at ERRATA.md:%d (prior lines kept %s) ; E-2026-09-25-5 at ERRATA.md:%d-%d ; draft carried %s ; backticks %d, outside code %d ; kind words %s'
          % (k + 2, kept, first, last, res['entry_equals_draft'], res['backticks'], res['backticks_outside_code'], words))


# ------------------------------------------------------------------------------ READING (7)
ENGINES = [('SIDE-interfaces', 'v0.1.3', 'Interfaces/ConnectionRequiresStructure.lean', 'theorem parametric_mechanism_theorem'),
           ('SIDE-effects', 'afa9ccf', 'SIDEEffects/Phase15/SIDEFramework.lean', 'theorem SIDE_exclusion')]


def engines():
    out = []
    for r, pin, f, head in ENGINES:
        t = g(r, 'show', '%s:%s' % (pin, f)).replace('\r', '').split(NL)
        a = next(i for i, l in enumerate(t) if l.startswith(head))
        Lc = blank_all_comments(NL.join(t)).split(NL)
        e, how, cut = stmt_end(t, Lc, a)
        st = NL.join(t[a:e] + [t[e][:cut + 2]]) if cut is not None else NL.join(t[a:e + 1])
        zero = any(re.search(p, st) for _, p in NEEDLES) or bool(re.search(r'is_xi_zero|IsNontrivialZero|riemannZeta|completedRiemannZeta|xi', st))
        out.append(dict(repo=r, pin=pin, file=f, line=a + 1, statement=st, takes_zero=zero,
                        kind='NEITHER', reason='stated over abstract types (a function P, a map f, a point a0 / a type X, a predicate P, a catalogue)'))
    put_json('b542_engines.json', dict(engines=out, any_takes_zero=any(x['takes_zero'] for x in out)))
    for x in out:
        print('  %s %s %s:%d  takes a zero of xi: %s ; kind %s' % (x['repo'], x['pin'], x['file'], x['line'], x['takes_zero'], x['kind']))
        print('    ' + x['statement'].replace(NL, NL + '    '))


# ------------------------------------------------------------------------------ READING (10): the probe
PROBE = ['Zeta23.zeta_reflect_zero', 'Zeta23.zeta_mult_reflect', 'Zeta23.ZetaSeam.one_le_mult_holds']


def probe():
    src = ['import Zeta23.ZetaReflect', 'import Zeta23.Statement.Seam', ''] + ['#print axioms ' + n for n in PROBE]
    p = os.path.join(SCR, 'b542_probe.lean')
    io.open(p, 'w', encoding='utf-8', newline=NL).write(NL.join(src) + NL)
    head = subprocess.run(['git', '-C', KER, 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()
    r = subprocess.run(['lake', 'env', 'lean', p], cwd=KER, capture_output=True, text=True, encoding='utf-8', errors='replace')
    txt = r.stdout.replace(chr(13), '')
    joined = re.sub(r'\n\s+', ' ', txt)
    prof = {}
    for n in PROBE:
        m = re.search(r"'%s' depends on axioms: \[([^\]]*)\]" % re.escape(n), joined)
        prof[n] = [x.strip() for x in m.group(1).split(',')] if m else None
    std = {'propext', 'Classical.choice', 'Quot.sound'}
    res = dict(head=head, exit=r.returncode, stdout=txt, profiles=prof, std3_or_fewer={n: (v is not None and set(v) <= std) for n, v in prof.items()})
    put_json('b542_probe.json', res)
    io.open(os.path.join(D, 'b542_probe.txt'), 'w', encoding='utf-8', newline=NL).write(
        'b542 -- THE AXIOM PROBE (a scratch file; nothing else compiled)\nSIDE-explicit-formula %s ; exit %d\n%s\n%s' % (head, r.returncode, NL.join(src), txt))
    print('  probe at SIDE-explicit-formula %s exit %d : %s' % (head[:8], r.returncode, res['std3_or_fewer']))


# ------------------------------------------------------------------------------ COMPONENT 3
def pinsha(cj, r):
    p = next(p for p in cj['pins'] if p['repo'] == r['repo'])
    return (p['cited'] + ' ' if p['cited'] != 'WORKING-HEAD' else 'WORKING-HEAD ') + p['sha'][:7]


def findings():
    cj, dj, ej = jl('b542_census.json'), jl('b542_dichotomy.json'), jl('b542_engines.json')
    k = cj['kinds']
    L = ['', FTITLE, '',
         '*Filed at b542 on the author`s ruling `(R152)`(2)-(3), before the monograph read`s second act (R152)(5). Every Lean repository '
         'SPIRAL_MAP lists with a tree on D:, and the ones the ruling names, read at its cited pin through `git show`; nothing checked out, '
         'no kernel file written, nothing compiled but an axiom probe. Bank: relay `data/b542_census.json`.*', '',
         '**The census.** %d declarations read in %d repositories; %d candidates by the ruling`s needles (widened to `≠ 0`, to Zeta23`s local `ζ`, '
         'and to names defined from a zero); %d hand-read as RESIDUE (a value`s real or imaginary part equal to 0, a derivative equal to 0, a '
         'group`s `zero`); **%d rows: INHERITS %d · FORCES %d · BOTH %d · NEITHER %d.** The record`s run equals the third pre-seal probe row '
         'for row: %s.' % (cj['run4']['decls'], len(cj['pins']), cj['candidates'], len(cj['residue']), len(cj['rows']), k['INHERITS'],
                            k['FORCES'], k['BOTH'], k['NEITHER'], cj['lineage_equal']), '',
         '| repository | pin | rows | INHERITS | FORCES | BOTH | NEITHER |', '|:--|:--|--:|--:|--:|--:|--:|']
    for p in cj['pins']:
        v = cj['per_repo'].get(p['repo'])
        if v:
            L.append('| %s | %s `%s` | %d | %d | %d | %d | %d |' % (p['repo'], p['cited'], p['sha'][:7], v['rows'], v['INHERITS'], v['FORCES'], v['BOTH'], v['NEITHER']))
    L.append('| %d other repositories | at their pins | 0 | 0 | 0 | 0 | 0 |' % sum(1 for p in cj['pins'] if not cj['per_repo'].get(p['repo'])))
    L += ['', '**The INHERITS-kind and FORCES-kind rows, verbatim:**', '']
    for r in cj['rows']:
        if r['kind'] in ('INHERITS', 'FORCES', 'BOTH'):
            L.append('- **%s** `%s` %s:%d at `%s` — `%s` — %s.' % (r['kind'], r['repo'], r['file'], r['line'], pinsha(cj, r),
                                                            ' '.join(r['statement'].split()).replace('`', ''), r['note']))
    L += ['', '**The seven classes of SIDE-kernel v1.5 (TheBridgeComplete.lean), two columns each:**', '',
          '| class | inherited constraint | INHERITS cell | forcing constraint | FORCES cell | one constraint in both |', '|:--|:--|:--|:--|:--|:--|']
    for d in dj['table']:
        L.append('| %s | %s | %s | %s | %s; %s | %s |' % (d['cls'], d['inherits_constraint'], d['inherits_cell'] if d['inherits_row'] == 'ABSENT' else d['inherits_row'] + '. ' + d['inherits_cell'],
                                                          d['forces_constraint'], d['forces_cell'].replace('`', ''), d['forces_grade'],
                                                          'yes, INHERITS side not T0' if d['same_constraint'] else 'no'))
    L += ['', '**What the census earns about the catalogue.** A compiled inherited constraint stated about zeta exists for **C3 only** (1 − conj ρ '
              'is a zero, and its multiplicity twin, in the vendored Zeta23), and it holds at every zero without forcing re = 1/2; the kernel`s '
              'own inherited statements are about `completedRiemannZeta₀`, which is not ξ. A compiled forcing constraint exists for **all seven** '
              'classes as algebra about a real σ that names no zero (C7`s definition-encoded). **No class has one constraint in both columns '
              'at T0**: the one class whose forcing constraint is also stated as inherited, C2 (the Euler balance), inherits it only under '
              'ConservationHypothesis, which is RH restated (`ch_iff_rh`). The stop of `(R152)`(4) did not fire. No BOTH row exists in any '
              'repository; BOTH-shaped statements occur only as definitions (`StructuralExhaustiveness`, `RHHypothesis`, `rh_strip`, '
              '`VerifiedZerosTo`) and as premises.', '',
          '**The two engines.** %s' % ' '.join('`%s` (%s %s:%d) takes a zero of ξ: %s.' % (x['statement'].split(NL)[0].split()[1], x['repo'], x['file'], x['line'],
                                                                                          'yes' if x['takes_zero'] else 'no') for x in ej['engines']) +
          ' Both are stated over abstract types.', '',
          '**Not read.** `SIDE-interface-split` (SPIRAL_MAP.md:274: removed at b390, never built) and `SIDE-orchestrator-<a>-<b>` (a naming '
          'convention). TECHNE-Core is read in memory and enters this entry only as a count.', '']
    w = append_to(FIND, NL.join(L))
    w['heading_line'] = rd(FIND).split(NL).index(FTITLE) + 1
    put_json('b542_findings.json', w)
    print('  FINDINGS : %(added)d bytes added, prefix %(prefix)s ; entry at line %(heading_line)d' % w)


# ------------------------------------------------------------------------------ Correspondence rows
def rows():
    cj, pj = jl('b542_census.json'), jl('b542_probe.json')
    led = rd(CORR)
    nums = [int(m) for m in re.findall(r'^\| (\d+) \|', led, re.M)]
    n = max(nums) + 1
    inh = [r for r in cj['rows'] if r['kind'] in ('INHERITS', 'BOTH')]
    out = []
    for r in inh:
        full = 'Zeta23.' + r['name']
        prof = pj['profiles'].get(full)
        cells = [str(n),
                 '**AN INHERITED CONSTRAINT AT A ZERO OF ZETA** (b542, under (R152)): `%s` -- %s. Read at SIDE-explicit-formula `%s` (the '
                 'vendored Zeta23, pin v1.0).' % (' '.join(r['statement'].split()).replace('`', ''), r['note'], r['pin'] if r['pin'] != 'HEAD' else cj['pins'][[p['repo'] for p in cj['pins']].index(r['repo'])]['sha'][:7]),
                 '`SIDE-explicit-formula/%s` : `%s`' % (r['file'], full),
                 '%s (`#print axioms` probe, b542)' % ('[' + ', '.join(prof) + ']' if prof is not None else 'NOT PRINTED'),
                 'INHERITS-kind (R152)(3); DERIVES by statement-read against "a zero of zeta inherits the constraint"',
                 'No other grade moved; nothing deposits; nothing at Zenodo written; no kernel edited.']
        rr = subprocess.run([sys.executable, os.path.join(T, 'corr_row.py'), CORR] + cells, capture_output=True, text=True, encoding='utf-8')
        out.append(dict(number=n, name=full, exit=rr.returncode, stdout=rr.stdout[-300:], stderr=rr.stderr[-300:], cells=cells))
        print('  row %d %s exit %d' % (n, full, rr.returncode))
        if rr.returncode:
            break
        n += 1
    put_json('b542_rows.json', dict(rows=out))


# ------------------------------------------------------------------------------ components, desk, trail
def git(r, *a):
    return subprocess.run(['git', '-C', r] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout.strip()


def blob(repo, spec):
    return subprocess.run(['git', '-C', repo, 'show', spec], capture_output=True).stdout


PRIOR_PP, SIDE_TIP = '81d7994', '502f0a7a67462eab83a0f10eee5ea74be67957dd'
FILES = ['ERRATA.md', 'FINDINGS.md', 'OPEN_TRAILS.md']


def subseq(old, new):
    it = iter(new.split(NL))
    return all(any(l == m for m in it) for l in old.split(NL))


def w(v):
    return 'VACUOUS' if v is None else ('HELD' if v else 'REFUTED')


def scores():
    cj, ej, fj, dj = jl('b542_census.json'), jl('b542_engines.json'), jl('b542_file.json'), jl('b542_dichotomy.json')
    rows_ = cj.get('rows', [])
    inh = [r for r in rows_ if r['kind'] == 'INHERITS']
    kept = {f: subseq(blob(PP, '%s:%s' % (PRIOR_PP, f)).decode('utf-8-sig').replace(chr(13), ''), rd(os.path.join(PP, f)))
            and (f == 'ERRATA.md' or open(os.path.join(PP, f), 'rb').read().startswith(blob(PP, '%s:%s' % (PRIOR_PP, f)))) for f in FILES}
    needle = 'https://' + 'zenodo' + '.org'
    zen = [x for x in os.listdir(T) if x.startswith('b542_') and needle in rd(os.path.join(T, x))]
    t = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    tok = sum(open(os.path.join(d0, f), 'rb').read().count(t) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b542_')) if t else None
    # the ledger`s repository is written by this act (one declared file) and is judged by that file alone; every other census repository
    # must be clean and at its census HEAD (defect (e): the first scoring counted the declared ledger write as a kernel edit)
    kernels = {p['repo']: (git(rpath(p['repo']), 'status', '--porcelain', '--untracked-files=no') == '' and git(rpath(p['repo']), 'rev-parse', 'HEAD') == p['head'])
               if p['repo'] != 'SIDE-global-section' else
               (set(x for x in git(SIDE, 'diff', '--name-only', SIDE_TIP).split(NL) if x) <= {'CORRESPONDENCE.md'} and
                git(SIDE, 'status', '--porcelain', '--untracked-files=no').replace('M CORRESPONDENCE.md', '').strip() == '')
               for p in cj.get('pins', [])}
    n3_list = dict(zeta23_reflect=any(r['name'] == 'zeta_reflect_zero' for r in inh), zeta23_twin=any(r['name'] == 'zeta_mult_reflect' for r in inh),
                   lv_reflection_field=any(r['repo'] == 'SIDE-lv-conservation' for r in inh),
                   only_reflection_conjugation=all(r['name'] in ('zeta_reflect_zero', 'zeta_mult_reflect') for r in inh),
                   none_forces=all('does not force' in r['note'] for r in inh))
    return dict(
        n1=cj.get('kinds', {}).get('BOTH', 1) == 0,
        n2=not [r for r in rows_ if r['repo'] == 'SIDE-kernel' and r['kind'] == 'INHERITS'],
        n2_shape=[(r['file'], r['line'], r['name']) for r in rows_ if r['repo'] == 'SIDE-kernel' and r['reason'] == 'OBJ'],
        n3=all(n3_list.values()), n3_clauses=n3_list, inherits=[(r['repo'], r['file'], r['line'], r['name']) for r in inh],
        n4=not ej.get('any_takes_zero', True),
        n5=fj.get('backticks_outside_code') == 0 and not zen and all(kernels.values()) and tok == 0 and git(PP, 'status', '--porcelain', '--', 'outputs') == '',
        kernels_clean=all(kernels.values()), kernels_dirty=[k for k, v in kernels.items() if not v], zen=zen, token=tok, kept=kept,
        s1=bool(cj.get('lineage_equal')),
        s2=bool(inh) and all(r['repo'] == 'SIDE-explicit-formula' and r['file'].startswith('Zeta23/') for r in inh) and not n3_list['lv_reflection_field'],
        s3=dj.get('stop_fired') == [],
        readme_registry_same={f: blob(PP, '%s:%s' % (PRIOR_PP, f)) == open(os.path.join(PP, f), 'rb').read() for f in ('README.md', 'REGISTRY.md', 'SPIRAL_MAP.md')})


def components():
    cj, dj = jl('b542_census.json'), jl('b542_dichotomy.json')
    L = ['=' * 132, 'b542 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '',
         '### COMPONENT 1 -- THE FILING : ' + json.dumps(jl('b542_file.json'), ensure_ascii=False), '',
         '### COMPONENT 2 -- THE CENSUS : needles %s ; derived (public) %s ; TECHNE-only derived %d' % (cj['needles'], cj['derived_public'], cj['derived_private_count']),
         '  yields %s' % cj['yields'], '  lineage v3 %s run 4 %s EQUAL %s' % (cj['v3'], cj['run4'], cj['lineage_equal']),
         '  candidates %d ; residue %d ; rows %d ; kinds %s' % (cj['candidates'], len(cj['residue']), len(cj['rows']), cj['kinds']), '  (a) the population :']
    L += ['    %-34s %-12s %s live-eq %s map :%s rows %d' % (p['repo'], p['cited'], p['sha'][:8], p['live_eq_head'], p['map_line'], p['rows']) for p in cj['pins']]
    L += ['    NOT READ %s' % cj['not_read'], '    mktemp clone : VACUOUS -- every repository has a local clone', '  (c)-(d) the rows :']
    L += ['    %-8s %-6s %s %s:%d %s' % (r['kind'], r['reason'], r['repo'], r['file'], r['line'], '' if r['private'] else r['name']) for r in cj['rows']]
    L += ['  RESIDUE :'] + ['    %s %s:%d %s -- %s' % (r['repo'], r['file'], r['line'], r['name'], r['reason']) for r in cj['residue']]
    L += ['  (e) the dichotomy :'] + ['    %s | %s | %s | %s | same %s' % (d['cls'], d['inherits_row'], d['forces_constraint'], d['forces_cell'], d['same_constraint']) for d in dj['table']]
    L += ['    STOP : %s' % (dj['stop_fired'] or 'NOT FIRED'), '  (f) the engines : ' + json.dumps(jl('b542_engines.json'), ensure_ascii=False)[:1500],
          '  (g) TECHNE-Core : %d rows, module and shape only' % sum(1 for r in cj['rows'] if r['private']), '',
          '### THE PROBE : ' + json.dumps(jl('b542_probe.json').get('profiles'), ensure_ascii=False),
          '### COMPONENT 3 -- FINDINGS : ' + json.dumps(jl('b542_findings.json')), '### THE ROWS : ' + json.dumps([(r['number'], r['name'], r['exit']) for r in jl('b542_rows.json').get('rows', [])]),
          '### COMPONENT 4 -- THE BRANCHES : see data/b542_branches.txt', '=' * 132]
    io.open(os.path.join(D, 'b542_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[:8]))


def desk():
    sc = scores()
    N, S = ('n1', 'n2', 'n3', 'n4', 'n5'), ('s1', 's2', 's3')
    L = ['=' * 104, 'b542 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '', '### THE NAVIGATOR`S FIVE.', '-' * 104,
         '  **(N1)** ### **%s.** -- BOTH rows : %s.' % (w(sc['n1']), jl('b542_census.json').get('kinds', {}).get('BOTH')),
         '  **(N2)** ### **%s.** -- SIDE-kernel INHERITS rows stated about xi : none ; its INHERITS-SHAPE rows on completedRiemannZeta₀ : %s.' % (w(sc['n2']), sc['n2_shape']),
         '  **(N3)** ### **%s.** -- the INHERITS rows : %s ; clauses %s.' % (w(sc['n3']), sc['inherits'], sc['n3_clauses']),
         '  **(N4)** ### **%s.** -- the engines take a zero of xi : %s.' % (w(sc['n4']), not sc['n4']),
         '  **(N5)** ### **%s.** -- E-5 backticks outside code 0 ; tools naming the platform %s ; census kernels clean and at their heads %s %s ; token hits %s.'
         % (w(sc['n5']), sc['zen'] or 'NONE', sc['kernels_clean'], sc['kernels_dirty'] or '', sc['token']),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- the record`s census equals v3 row for row.' % w(sc['s1']),
         '  **(S2)** ### **%s.** -- every INHERITS row in Zeta23 ; lv-conservation holds none.' % w(sc['s2']),
         '  **(S3)** ### **%s.** -- the stop : %s.' % (w(sc['s3']), jl('b542_dichotomy.json').get('stop_fired') or 'NOT FIRED'),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in N].count(True), [sc[k] for k in N].count(False), [sc[k] for k in S].count(True), [sc[k] for k in S].count(False)),
         '  written files keep their prior lines %s ; README, REGISTRY, SPIRAL_MAP byte-identical %s' % (sc['kept'], sc['readme_registry_same']),
         '', '### THIS ACT`S OWN DEFECTS.'] + ([l for l in rd(os.path.join(D, 'b542_defects.txt')).rstrip(NL).split(NL) if l]
                                              if os.path.exists(os.path.join(D, 'b542_defects.txt')) else ['    NONE RECORDED.']) + ['=' * 104]
    io.open(os.path.join(D, 'b542_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    put_json('b542_scores.json', sc)
    print(NL.join(L))


def trail():
    sc, cj, fj = scores(), jl('b542_census.json'), jl('b542_file.json')
    rws = jl('b542_rows.json').get('rows', [])
    body = ['', HEADING, '',
            '**(R152) ratified.** (1) E-2026-09-25-5 filed. (2)-(3) The inheritance census across the federation. (4) The seven-class '
            'dichotomy. (5) The monograph read`s second act is the act after this one; BALANCE_AND_POSITIVITY follows. (6) The two push '
            'branches deleted by name.', '',
            '**Filed:** E-2026-09-25-5 at `ERRATA.md`:%s-%s, its bullet at :%s. **Entered:** the census at `FINDINGS.md`:%s; Correspondence rows %s.'
            % (fj['entry_lines'][0], fj['entry_lines'][1], fj['bullet_line'], jl('b542_findings.json').get('heading_line'), [r['number'] for r in rws]), '',
            '**The census:** %d declarations, %d candidates, %d rows -- INHERITS %d · FORCES %d · BOTH %d · NEITHER %d. The INHERITS rows are '
            'Zeta23`s `zeta_reflect_zero`, `zeta_mult_reflect` and `ZetaSeam.one_le_mult_holds`; the FORCES rows are grh-transfer`s two '
            'algebra iffs; SIDE-kernel`s own forcing terminals name no zero. No class has one constraint in both columns at T0; the stop did '
            'not fire.' % (cj['run4']['decls'], cj['candidates'], len(cj['rows']), cj['kinds']['INHERITS'], cj['kinds']['FORCES'], cj['kinds']['BOTH'],
                           cj['kinds']['NEITHER']), '',
            '**Next:** the monograph read`s second act (Chapter 26 to the end, §27.3 among it), with this census in hand; then BALANCE_AND_POSITIVITY.', '',
            '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s.** The seat`s own: (S1) %s, (S2) %s, (S3) %s.'
            % tuple(w(sc[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 's1', 's2', 's3')),
            '**No kernel lane opened at this act.** Nothing deposits; nothing at Zenodo written; no kernel edited; no monograph byte changed; '
            'the ceiling unchanged; no grade moved on an existing row; row U1 unedited; `h2` where the deposit left it; the four lists stay '
            'OPEN; nothing here is a statement about RH.', '']
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
    put_json('b542_trail_notes.json', out)


if __name__ == '__main__':
    sys.exit({'reads': reads, 'file': file, 'census': census, 'engines': engines, 'probe': probe, 'findings': findings, 'rows': rows,
              'components': components, 'desk': desk, 'trail': trail}[sys.argv[1]]())
