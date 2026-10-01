# -*- coding: utf-8 -*-
"""b569_record.py -- THE ACT'S RECORD TOOL, UNDER (R179). ### ONE SUBCOMMAND PER BANK.

### ### b569: LANE TWO, ACT NINE -- GRH-WEIL ACT FOUR. ### Subcommands, each writing only `data/b569_*` unless its
### docstring names a ledger: reads, converses, bulka, route, analogues, nodes, findings, trail, rows, scores, desk,
### components. ### Every bank is written through `put_txt` / `put_json` (encode first, then a temp file, then
### `os.replace`), so a failed encode leaves no zero-byte husk (b328's trap).
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import e0_rule as E0   # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
EF = 'D:/SIDE-explicit-formula'
PP = 'D:/MY-DOwnloads/PLACE-papers'
SIDE = 'D:/SIDE-global-section'
V010 = '6baed63ae664a22db1f325177b81253e270de6e3'
BR = 'grh-weil-b569'
STD3 = ['propext', 'Classical.choice', 'Quot.sound']

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '')


def put_txt(name, lines):
    b = (NL.join(lines) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s (%d bytes)' % (name, len(b)))


def put_json(name, obj):
    b = (json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s (%d bytes)' % (name, len(b)))


def jl(name):
    return json.load(io.open(os.path.join(D, name), encoding='utf-8'))


def rd(name):
    p = os.path.join(D, name)
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


def utc():
    import datetime
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


# ================================================================================ READING (1)
RELAY = ROOT.replace('\\', '/')
READS = [
    # (label, repo, rev, path, [lines])
    ('vendored Zeta23 WeilEF/Main (EF_lit`s proof)', EF, V010, 'Zeta23/WeilEF/Main.lean', [16, 17, 286]),
    ('vendored Zeta23 ExplicitFormula (EF_lit)', EF, V010, 'Zeta23/ExplicitFormula.lean', [97]),
    ('vendored Zeta23 RvM/ZetaGrowth (its import of ZetaBounds; its first declarations)', EF, V010,
     'Zeta23/RvM/ZetaGrowth.lean', [45, 59, 72, 94, 118]),
    ('vendored Zeta23 RvM/LocalCount (its imports)', EF, V010, 'Zeta23/RvM/LocalCount.lean', [39, 40, 41, 42, 43, 44]),
    ('vendored Zeta23 WeilEF/ZeroSummability (its imports)', EF, V010, 'Zeta23/WeilEF/ZeroSummability.lean', [22, 23, 24, 25]),
    ('kernel Chi/ZeroConfig (chiZeroConfig)', EF, V010, 'SIDEExplicitFormula/Chi/ZeroConfig.lean', [225]),
    ('kernel Chi/ZetaBoundsStrip (the representation and the four analogues)', EF, V010,
     'SIDEExplicitFormula/Chi/ZetaBoundsStrip.lean', [123, 307, 320, 328, 337]),
    ('kernel Chi/Statement (EF_lit_chi)', EF, V010, 'SIDEExplicitFormula/Chi/Statement.lean', [42]),
    ('kernel ResidueDischarge (the restated predicate; the forward implication)', EF, V010,
     'SIDEExplicitFormula/ResidueDischarge.lean', [30, 31, 41]),
    ('kernel LiCriterionBridge (the equality lemma; the composed criterion)', EF, V010,
     'SIDEExplicitFormula/LiCriterionBridge.lean', [149, 179]),
    ('kernel LiWeil (rh_imp_li_nonneg)', EF, V010, 'SIDEExplicitFormula/LiWeil.lean', [267]),
    ('vendored Bulka ReverseDirection (positivity_implies_RH)', EF, V010, 'Vendored/Bulka/Lc/LiCriterion/ReverseDirection.lean', [413, 414, 415]),
    ('vendored Bulka RHBridge (rh_equiv_mathlib)', EF, V010, 'Vendored/Bulka/Lc/LiCriterion/RHBridge.lean', [43]),
    ('relay b568 ZetaBounds classes (the rule)', RELAY, 'HEAD', 'data/b568_zetabounds_names.txt', [5, 6, 7, 8]),
    ('relay b568 node list', RELAY, 'HEAD', 'data/b568_nodes.txt', [1, 2, 3]),
    ('relay chain_page.py (the pin; record_tier; tier_of)', RELAY, 'HEAD', 'tools/chain_page.py', [48, 98, 296]),
    ('relay b564 face (the genericity rule, b562`s carried)', RELAY, 'HEAD', 'data/b564_registration_2026-09-29.txt',
     [75, 76, 110, 111, 112, 113, 114]),
    ('relay b566_checks.py (the as-of import; the PLACE-papers and clone reads)', RELAY, 'HEAD', 'tools/b566_checks.py',
     [118, 119, 212, 236, 237, 252]),
    ('relay b567_checks.py (the as-of import; the kernel and PLACE-papers reads)', RELAY, 'HEAD', 'tools/b567_checks.py',
     [122, 123, 197, 225, 230, 248]),
    ('relay the push-out bank`s form', RELAY, 'HEAD', 'data/b568_closing_push_out.txt', [1, 2, 5, 6]),
    ('relay terminal_table.py (the diff of grade cells)', RELAY, 'HEAD', 'tools/terminal_table.py', [917, 918, 919, 920, 921]),
    ('relay push_gated.sh (the push; the read-back)', RELAY, 'HEAD', 'tools/push_gated.sh', [69, 78, 80]),
    ('relay b566 closing (the heads at its close; the clones)', RELAY, 'HEAD', 'data/b566_closing.txt', [81, 82, 84, 99, 103]),
    ('relay b567 closing (the heads at its close; the clones)', RELAY, 'HEAD', 'data/b567_closing.txt', [44, 45, 47, 64, 67]),
    ('PLACE-papers the page`s head', PP, 'HEAD', 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md', [1, 3]),
]


def reads():
    """### READING (1): every cited line printed from its blob at its pin (kernel v0.10; relay and PLACE-papers HEAD at the
    ### act's start: relay 3f1d1900, PLACE-papers f2e93b0)."""
    L = ['b569 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, lines in READS:
        src = g(repo, 'show', '%s:%s' % (rev, path))
        rv = g(repo, 'rev-parse', '--short=8', rev).strip()
        L.append('### %s -- %s @ %s' % (label, path, rv))
        sl = src.split(NL)
        for n in lines:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:300]))
    L.append('')
    L.append('### the Vendored/Bulka module list at v0.10 (git ls-tree):')
    mods = [x for x in g(EF, 'ls-tree', '-r', '--name-only', V010, 'Vendored/Bulka').split(NL) if x.endswith('.lean')]
    L.append('    %d modules: %s' % (len(mods), ' '.join(m[len('Vendored/Bulka/'):-5] for m in mods)))
    put_txt('b569_reads.txt', L)


# ================================================================================ COMPONENT 1
CONV = 'SIDEExplicitFormula/PageConverses.lean'
CONV_NAMES = ['rh_imp_register4_positivity_liCoeff', 'register4_positivity_liCoeff_iff_rh',
              'rh_imp_taylorCoeff_nonneg', 'taylorCoeff_nonneg_iff_rh']
NSC = 'SIDEExplicitFormula.PageConverses.'
DECL = r'^(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+)?(?:noncomputable\s+)?(?:theorem|lemma|def|abbrev)\s+'


def header_of(src, short):
    m = re.search(DECL + re.escape(short) + r'(?![\w\'₀-₉])(.*?):=', src, re.S | re.M)
    return (' '.join(m.group(1).split()), src[:m.start()].count(NL) + 1) if m else (None, None)


def prints_axioms(text):
    """### `'Name' depends on axioms: [...]` read across Lean's wrapped lines; `does not depend` reads []."""
    flat = re.sub(r'\n(?=[ \t]*[A-Za-z_.]+[,\]])', ' ', text)
    out = {}
    for m in re.finditer(r"^'(.+?)' depends on axioms: \[([^\]]*)\]", flat, re.M):
        out[m.group(1)] = [x.strip() for x in m.group(2).split(',') if x.strip()]
    for m in re.finditer(r"^'(.+?)' does not depend on any axioms", flat, re.M):
        out[m.group(1)] = []
    return out


def converses(rev=None):
    """### Component 1's bank: each statement's source header at the branch (or `rev`), its E0 grade by the shared rule, its
    ### print from data/b569_converse_prints.txt, and the build's own lines for the module."""
    rev = rev or BR
    src = g(EF, 'show', '%s:%s' % (rev, CONV))
    pr = prints_axioms(rd('b569_converse_prints.txt'))
    bld = rd('b569_converse_build.txt')
    st = rd('b569_converse_statements.txt')
    t_st = re.search(r'written at \(UTC\) (\S+)', st)
    t_b = re.search(r'^=== START (\S+)', bld, re.M)
    rows = {}
    L = ['b569 -- COMPONENT 1: THE TWO CONVERSES, (R179)(2) -- BUILT, PRINTED, GRADED', '',
         '### the module : %s at %s (%s)' % (CONV, rev, g(EF, 'rev-parse', '--short=8', rev).strip()),
         '### the statements banked at (UTC) %s ; the build started at (UTC) %s ; statements first : %s'
         % (t_st.group(1) if t_st else '?', t_b.group(1) if t_b else '?', bool(t_st and t_b and t_st.group(1) < t_b.group(1))),
         '### the build : %s' % ' ; '.join(l for l in bld.split(NL) if 'PageConverses' in l or l.startswith('Build') or l.startswith('=== END')),
         '### the module`s own warnings in the build : %d' % sum(1 for l in bld.split(NL) if 'PageConverses.lean:' in l), '']
    L += E0.RULE_TEXT + ['']
    for n in CONV_NAMES:
        head, line = header_of(src, n)
        gr, why, _b = E0.grade(head or '', 'theorem')
        ax = pr.get(NSC + n)
        rows[NSC + n] = dict(line=line, header=head, grade=gr, why=why, axioms=ax, std3=ax == STD3)
        L.append('    :%-4s %-40s E0 %-11s axioms %s' % (line, n, gr, ax))
        L.append('          %s' % head)
    ok = all(r['grade'] == 'DERIVES' and r['std3'] for r in rows.values()) and len(rows) == 4
    L += ['', '### ### **THE FOUR AT THE STANDARD THREE, E0 DERIVES : %s** -- the converse of each compiled implication is now a'
          ' compiled implication, and each iff is a compiled equivalence; no new analysis.' % ok]
    put_txt('b569_converses.txt', L)
    put_json('b569_converses.json', dict(rev=rev, sha=g(EF, 'rev-parse', rev).strip(), rows=rows, all_ok=ok,
                                         statements_first=bool(t_st and t_b and t_st.group(1) < t_b.group(1))))


# ================================================================================ COMPONENT 3
ZRX = re.compile(r'(?<![A-Za-z0-9])(?:completedRiemannZeta|riemannZeta)[A-Za-z0-9_₀\']*')


def strip_comments(src):
    """### Lean's nested block comments and line comments replaced by spaces, newlines kept (line numbers survive)."""
    out, i, depth, n = [], 0, 0, len(src)
    while i < n:
        if src.startswith('/-', i):
            depth += 1
            i += 2
            continue
        if depth and src.startswith('-/', i):
            depth -= 1
            i += 2
            continue
        if depth:
            out.append(NL if src[i] == NL else ' ')
            i += 1
            continue
        if src.startswith('--', i):
            j = src.find(NL, i)
            j = n if j < 0 else j
            out.append(' ' * (j - i))
            i = j
            continue
        out.append(src[i])
        i += 1
    return ''.join(out)


def bulka():
    """### W-ORD-BULKA-GENERIC: the vendored modules read at v0.10 by b564's rule (reading (vi)); no build."""
    files = sorted(x for x in g(EF, 'ls-tree', '-r', '--name-only', V010, 'Vendored/Bulka').split(NL) if x.endswith('.lean'))
    mods = {}
    for f in files:
        mod = f[len('Vendored/Bulka/'):-5].replace('/', '.')
        src = g(EF, 'show', '%s:%s' % (V010, f))
        s = strip_comments(src)
        hits = [(i + 1, l.strip()) for i, l in enumerate(s.split(NL)) if ZRX.search(l)]
        raw = sum(1 for l in src.split(NL) if ZRX.search(l))
        imps = re.findall(r'^import (\S+)', s, re.M)
        mods[mod] = dict(path=f, hits=hits, raw=raw, imports=imps)
    direct = sorted(m for m in mods if mods[m]['hits'])
    spec = set(direct)
    changed = True
    while changed:
        changed = False
        for m, r in mods.items():
            if m not in spec and any(i in spec for i in r['imports']):
                spec.add(m)
                changed = True
    prop = sorted(spec)
    # ### the positive control: the rule finds a ζ object where one is known to be (RHBridge :45-:95), and the stripper
    # ### removes a commented one (the vendoring header names riemannZeta nowhere, so a synthetic line is used).
    ctl_pos = bool(ZRX.search('rw [riemannZeta_def_of_ne_zero hs_ne_zero] at hs'))
    ctl_neg = not ZRX.search(strip_comments('-- riemannZeta here is a comment\n/- completedRiemannZeta -/ x'))
    L = ['b569 -- COMPONENT 3: BULKA`S MODULES READ FOR GENERICITY (W-ORD-BULKA-GENERIC), UNDER (R179)(6) -- NO BUILD', '',
         '### the modules : Vendored/Bulka at SIDE-explicit-formula v0.10 = %s (%d .lean files)' % (V010[:7], len(files)),
         '### THE RULE (b564`s face :75-:76, :110-:114; b562`s rule carried; reading (vi) of this act`s face): a module is',
         '###   ζ-SPECIFIC if its comment-stripped code names a ζ object -- riemannZeta, completedRiemannZeta, riemannZeta_*,',
         '###   completedRiemannZeta_* (a ζ lemma of Mathlib named by its name: the pattern below, a name containing either',
         '###   stem after a non-alphanumeric) -- or imports a ζ-specific module. H21d counts the FIRST clause alone.',
         '### the pattern : %s' % ZRX.pattern,
         '### controls : a known ζ line is found %s ; a commented ζ object is not found after stripping %s' % (ctl_pos, ctl_neg), '']
    for m in sorted(mods):
        r = mods[m]
        cls = 'ζ-SPECIFIC (names)' if m in direct else ('ζ-SPECIFIC (imports)' if m in spec else 'GENERIC')
        L.append('    %-52s %-22s code lines naming a ζ object %3d (with comments %3d)' % (m, cls, len(r['hits']), r['raw']))
        for ln, t in r['hits']:
            L.append('        :%-5d %s' % (ln, t[:160]))
    L += ['',
          '### ### **NAMING A ζ OBJECT IN COMMENT-STRIPPED CODE : %d OF %d** %s' % (len(direct), len(files), direct),
          '### ### **ζ-SPECIFIC BY THE RULE (NAMING, OR IMPORTING SUCH A MODULE) : %d OF %d** ; GENERIC %d'
          % (len(prop), len(files), len(files) - len(prop)),
          '### ### **H21d (at most three of the modules name riemannZeta) : %s** -- the count is %d.'
          % ('HELD' if len(direct) <= 3 else 'REFUTED', len(direct)), '']
    L += PARAGRAPH
    put_txt('b569_bulka_generic.txt', L)
    put_json('b569_bulka_generic.json', dict(rev=V010, modules=len(files), direct=direct, propagated=prop,
                                             h21d='HELD' if len(direct) <= 3 else 'REFUTED', count=len(direct),
                                             controls=dict(pos=ctl_pos, neg=ctl_neg),
                                             per={m: dict(hits=len(r['hits']), raw=r['raw']) for m, r in mods.items()}))


# ### THE SEAT'S PARAGRAPH (the ruling asks for one), read from the modules printed above; a reading, not a print.
PARAGRAPH = [
    '### WHETHER THE CONVERSE IS AN ARGUMENT OVER A ZeroConfig -- the seat`s reading, from the lines above:',
    '### The converse (`positivity_implies_RH`, ReverseDirection :413) is not stated or proved over a zero configuration: it',
    '### is stated for Bulka`s own `riemannXi` (Lc.XiZeros, Lc.LiCriterion.Basic :1252, built from `completedRiemannZeta₀`)',
    '### and its own zero type `NontrivialZero` (Basic :116), and Zeta23`s `ZeroConfig` appears in none of the modules. Its',
    '### proof has three steps (ReverseDirection :413-:427): (1) `phi_nonzero_unit_disk_of_nonneg` (:335) -- nonnegative real',
    '### parts of the Taylor coefficients of the log-derivative of φ(z) = ξ(1/(1 − z)) force φ to have no zero in the unit',
    '### disc; the module names no ζ object outside the theorem`s conclusion (:415), and the step reads as an argument about',
    '### an entire function with φ(0) ≠ 0, specialised to `riemannXi`; (2) `re_le_half_of_phi_nonzero` (:400) -- a zero ρ',
    '### gives a zero of φ at 1 − 1/ρ, inside the disc when Re ρ > 1/2; (3) `pairedZero` (Basic :1668) -- the reflection',
    '### ρ ↦ 1 − ρ from the functional equation (`completedRiemannZeta₀_one_sub`, Fidelity :107; RHBridge :90-:91) gives the',
    '### other inequality. The ζ-specific inputs are therefore the definition of ξ, the identification of its zeros with',
    '### ζ`s nontrivial zeros (RHBridge :45-:95, XiZeros) and the reflection; the power-sum identity',
    '### (`taylorCoeff_eq_li_symmetrized`, Fidelity :140) is the forward direction`s and the bridge`s, not the converse`s, and',
    '### its module names a ζ object (Fidelity :107). For L(s, χ) at primitive χ ≠ 1 the reflection is ρ ↦ 1 − ρ̄ (the',
    '### functional equation pairs χ with χ̄), so step (3) does not carry over as written; steps (1)-(2) read as generic in',
    '### substance but are stated for `riemannXi`. A reading; nothing is built.',
]


# ================================================================================ COMPONENT 4
ZB = 'Zeta23/FromPNTPlus/ZetaBounds.lean'
ZBMOD = 'Zeta23.FromPNTPlus.ZetaBounds'
BLOCKS = [(1, 1219, 'CONTINUATION'), (1220, 1850, 'STRIP BOUNDS'), (1851, 10 ** 6, 'ZERO-FREE REGION')]
START = 'Zeta23.WeilEF.EF_lit_zetaZeroConfig'
AUX = re.compile(r'\.(?:_proof_\d+(?:_\d+)?|_simp_\d+(?:_\d+)?|match_\d+(?:_\d+)?|eq_\d+|_auxLemma\.\d+)$')


def fold(n):
    while AUX.search(n):
        n = AUX.sub('', n)
    return n


def place(lines, n):
    """### b568's matcher v2: the declaration line of `n` (its last component, a dotted capitalised prefix allowed)."""
    short = n.split('.')[-1]
    pre = '.'.join(n.split('.')[:-1])
    pat = re.compile(r'^(?:@\[[^\]]*\]\s*)?(?:private\s+)?(?:noncomputable\s+)?(?:theorem|lemma|def|abbrev|irreducible_def)\s+'
                     + (re.escape(pre) + r'\.' if pre else r'(?:[A-Z][\w]*\.)*') + re.escape(short) + r'(?![\w\'₀-₉])')
    return [i + 1 for i, l in enumerate(lines) if pat.match(l)]


def route():
    """### Component 4: the probe's output (one `lake env lean` call), folded, placed and classed; H21a scored. Written BEFORE
    ### any Component 5 build: the bank carries its own time, and Component 5's first build log carries its start."""
    out = rd('b569_route_probe_out.txt')
    reach = re.findall(r'^@@REACH (\S+) @@MOD (\S+) @@FROM (\S+)', out, re.M)
    cnt = re.search(r'^@@COUNT (\d+)', out, re.M)
    parent = {c: p for c, m, p in reach}
    zbc = [c for c, m, p in reach if m == ZBMOD]
    src = g(EF, 'show', '%s:%s' % (V010, ZB))
    lines = src.split(NL)
    folded = sorted(set(fold(c) for c in zbc))
    where = {n: place(lines, n) for n in folded}
    cls = {n: [c for lo, hi, c in BLOCKS if lo <= h[0] <= hi][0] for n, h in where.items() if len(h) == 1}
    unplaced = [n for n, h in where.items() if len(h) != 1]

    def path(c):
        p, seen = [c], {c}
        while p[-1] in parent and parent[p[-1]] not in seen:
            seen.add(parent[p[-1]])
            p.append(parent[p[-1]])
        return p
    entry = sorted(set(p for c, m, p in reach if m == ZBMOD and not p.startswith('Zeta23.FromPNTPlus.ZetaBounds')
                       and p not in set(zbc)))
    by = {c: sorted((n for n in cls if cls[n] == c), key=lambda x: where[x][0]) for _, _, c in BLOCKS}
    ctl_pos = 'Zeta23.RvM.norm_riemannZeta_le_of_re_pos' in parent
    ctl_neg = not any(fold(c) == 'ZetaZeroFree' for c in zbc)
    h21a = 'HELD' if not by['ZERO-FREE REGION'] else 'REFUTED'
    L = ['b569 -- COMPONENT 4: THE ROUTE READ, (R179)(6) -- THE ZetaBounds NAMES EF_lit`S PROOF CONSUMES TRANSITIVELY, BY CLASS',
         '### written at (UTC) %s, before any Component 5 build' % utc(), '',
         '### the probe : relay data/b569_route_probe.lean.txt, elaborated by one `lake env lean` call from the kernel checkout',
         '###   (grh-weil-b569 at 23c29cc = v0.10 + PageConverses.lean; every Zeta23 byte is v0.10`s); its output banked whole as',
         '###   relay data/b569_route_probe_out.txt',
         '### THE READ (the face`s reading (v)): from %s, every constant of its type and value, followed through every constant'
         % START,
         '###   of a Zeta23 module and stopped at Mathlib; each reached constant printed with its module and the constant it was',
         '###   reached from; auxiliaries (`_proof_`, `_simp_`, `match_`, `eq_`) folded to their parent; placed in',
         '###   %s at v0.10 by b568`s matcher v2 and classed by b568`s line rule:' % ZB,
         '###   [:1, :1219] CONTINUATION ; [:1220, :1850] STRIP BOUNDS ; [:1851, end] ZERO-FREE REGION (data/b568_zetabounds_names.txt :5-:8)',
         '### the walk : %s Zeta23 constants reached ; %d of them in %s ; folded to %d declarations ; placed %d ; unplaced %d %s'
         % (cnt.group(1) if cnt else '?', len(zbc), ZBMOD, len(folded), len(cls), len(unplaced), unplaced),
         '### controls : the walk reaches the known consumer Zeta23.RvM.norm_riemannZeta_le_of_re_pos %s ; it does not reach'
         ' ZetaZeroFree (:2485) %s' % (ctl_pos, ctl_neg),
         '### the route enters ZetaBounds from : %s' % ', '.join(entry), '']
    for c in by:
        L.append('### %s : %d' % (c, len(by[c])))
        for n in by[c]:
            L.append('    :%-5d %-34s path: %s' % (where[n][0], n, ' <- '.join(path(n)[1:6]) + (' <- ...' if len(path(n)) > 6 else '')))
        L.append('')
    L += ['### ### **BY CLASS : CONTINUATION %d ; STRIP BOUNDS %d ; ZERO-FREE REGION %d ; TOTAL %d.**'
          % (len(by['CONTINUATION']), len(by['STRIP BOUNDS']), len(by['ZERO-FREE REGION']), len(cls)),
          '### ### **H21a (the consumed subset lies in continuation and strip bounds, not in the zero-free region; refuted if the'
          ' route names a zero-free lemma) : %s.**' % h21a]
    put_txt('b569_route.txt', L)
    put_json('b569_route.json', dict(reached=int(cnt.group(1)) if cnt else None, zb_constants=len(zbc), folded=folded,
                                     where=where, cls=cls, by=by, unplaced=unplaced, entry=entry, h21a=h21a,
                                     controls=dict(pos=ctl_pos, neg=ctl_neg), written=utc()))


# ================================================================================ COMPONENT 2(a): the companion banks
REPO_DIR = {'relay': 'D:/relay', 'PLACE-papers': PP}
CLOSE_ROW = re.compile(r'^\s+(\S+)\s+main ([0-9a-f]{12}) ; remote ([0-9a-f]{12}) ; AGREE', re.M)


def companions():
    """### (R179)(3) for b566 and b567, whose committed push-out banks are not edited: one as-of line per repository their
    ### suites read, each head taken from the act's closing heads table (the line cited) and resolved to its full SHA by
    ### git in that repository (refused unless unique and equal in prefix); the relay line is the push-out bank's own tip;
    ### the clones from the closing's clone line."""
    sys.path.insert(0, os.path.join(ROOT, 'tools'))
    import asof as AF
    clones = {
        'b566': [('bulka', 'b566_closing.txt', 103, 'D:/audit-b565/bulka @35df682f KEPT',
                  '35df682f', 'the clone kept at b566`s close, deleted at b567`s by (R177); its HEAD the vendoring pin'),
                 ('arda', 'b566_closing.txt', 103, 'D:/audit-b565/arda DELETED', None, 'deleted at b566`s close by (R176)')],
        'b567': [('bulka', 'b567_closing.txt', 67, 'D:/audit-b565/bulka ABSENT', None, 'deleted at b567`s close by (R177)'),
                 ('b567-lake-51e6992e', 'b567_closing.txt', 67, 'the old build tree aside at D:/b567-lake-51e6992e PRESENT', 'PRESENT',
                  'a directory, not a repository: present at b567`s close, deleted at b568 by (R178)(2)(iv) -- defect (d)')],
    }
    for act in ('b566', 'b567'):
        clo = rd('%s_closing.txt' % act)
        cl = clo.split(NL)
        relay_sha = AF.relay_asof(ROOT, D, act)
        L = ['### b569 -- (R179)(3): THE AS-OF LINES FOR %s, A COMPANION BANK (its push-out bank is committed and not edited).' % act,
             '### written at (UTC) %s by relay tools/b569_record.py companions ; read by relay tools/asof.py repo_asof' % utc(),
             '### each head from relay data/%s_closing.txt`s heads table (the line cited), resolved to its full SHA by git in that'
             ' repository; the relay line is data/%s_closing_push_out.txt`s tip read back equal' % (act, act),
             'push_gated: as-of relay %s   ### data/%s_closing_push_out.txt' % (relay_sha, act)]
        bad = []
        for i, l in enumerate(cl):
            m = CLOSE_ROW.match(l)
            if not m or m.group(1) == 'relay':
                continue
            name, pre = m.group(1), m.group(2)
            repo = REPO_DIR.get(name, 'D:/' + name)
            full = g(repo, 'rev-parse', '--verify', '-q', pre + '^{commit}').strip()
            if len(full) != 40 or not full.startswith(pre) or m.group(2) != m.group(3):
                bad.append(name)
                continue
            L.append('push_gated: as-of %s %s   ### data/%s_closing.txt :%d' % (name, full, act, i + 1))
        for name, f, ln, needle, pre, why in clones[act]:
            ok = needle in (cl[ln - 1] if ln <= len(cl) else '')
            if not ok:
                bad.append(name)
                continue
            if pre == 'PRESENT':
                L.append('push_gated: as-of %s present at close   ### data/%s :%d ; %s' % (name, f, ln, why))
            elif pre:
                # ### the clone is gone; its full HEAD is the vendoring pin carried in every vendored header
                hdr = g(EF, 'show', '%s:Vendored/Bulka/Lc/LiCriterion/Basic.lean' % V010)
                mm = re.search(r'Pin\s+:\s+([0-9a-f]{40})', hdr)
                full = mm.group(1) if mm and mm.group(1).startswith(pre) else None
                if not full:
                    bad.append(name)
                    continue
                L.append('push_gated: as-of %s %s   ### data/%s :%d ; %s' % (name, full, f, ln, why))
            else:
                L.append('push_gated: as-of %s deleted at close   ### data/%s :%d ; %s' % (name, f, ln, why))
        parsed = AF.parse_asof_lines(NL.join(L))
        L.append('### lines : %d ; refused : %s' % (len(parsed or {}), bad or 'none'))
        if bad or not parsed:
            print('### REFUSED for %s: %s' % (act, bad))
            continue
        put_txt('b569_asof_%s.txt' % act, L)


# ================================================================================ COMPONENT 5: E0, the salt-check, rowgen
E0SETS = {
    'converses': dict(prints='b569_converse_axiomcheck.txt', decls='b569_decls_converses.json',
                      record=[('SIDEExplicitFormula/PageConverses.lean',
                               ['SIDEExplicitFormula.PageConverses.register4_positivity_liCoeff_iff_rh',
                                'SIDEExplicitFormula.PageConverses.taylorCoeff_nonneg_iff_rh'])]),
    'chi': dict(prints='b569_chi_prints.txt', decls='b569_decls_chi.json',
                record=[('SIDEExplicitFormula/Chi/ZeroSummability.lean', ['SIDEExplicitFormula.GRHWeil.EF_zero_sum_summable_chi']),
                        ('SIDEExplicitFormula/Chi/LocalCount.lean', ['SIDEExplicitFormula.GRHWeil.chiZeroConfig_local_count']),
                        ('SIDEExplicitFormula/Chi/GoodHeights.lean', ['SIDEExplicitFormula.GRHWeil.good_heights_chi']),
                        ('SIDEExplicitFormula/Chi/XiLogDeriv.lean', ['SIDEExplicitFormula.GRHWeil.logDeriv_completedLFunction_one_sub'])]),
}


def e0(which, rev='main'):
    """### Every declaration of the set graded by the shared E0 rule (relay tools/e0_rule.py) on its source header at `rev`
    ### (main after the fast-forward, so the rows cite main), its print from the AxiomCheck output, the salt-check of each
    ### definition, and rowgen's record of the terminals of record (b566_record.Q.rowgen_record, IMPORTED)."""
    import b566_record as R6
    Q = R6.Q
    c = E0SETS[which]
    pr = rd(c['prints'])
    P0 = prints_axioms(pr)
    dj = jl(c['decls'])
    decls, consumed = dj['decls'], dj['consumed']
    tip = g(EF, 'rev-parse', rev).strip()
    L = ['b569 -- COMPONENT 5: THE E0 READ (%s) -- EVERY DECLARATION GRADED, THE SALT-CHECK, THE ROWGEN RECORD' % which, '',
         '### the prints of record: relay data/%s ; the statements at %s (%s).' % (c['prints'], tip[:7], rev)] + E0.RULE_TEXT + ['']
    rows, srcs = {}, {}
    for d in decls:
        n = d['name']
        if d['file'] not in srcs:
            srcs[d['file']] = g(EF, 'show', '%s:%s' % (tip, d['file']))
        head, _ln = header_of(srcs[d['file']], n.split('.')[-1])
        gr, why, _b = E0.grade(head or '', d['kind'])
        ax = P0.get(n)
        rows[n] = dict(grade=gr, why=why, axioms=ax, std3=ax is not None and set(ax) <= set(STD3), head=head, file=d['file'],
                       header_read=head is not None)
        L.append('    %-44s %-10s %s  -- %s' % (n.split('.')[-1], 'DEFINITION' if gr == 'DEF' else gr,
                                                 'std3' if rows[n]['std3'] else ax, (why or '')[:140]))
    L += ['', '### THE CONSUMED TERMINALS, their prints:']
    cons = {n: P0.get(n) for n in consumed}
    for n, ax in cons.items():
        L.append('    %-60s %s' % (n, 'std3' if ax is not None and set(ax) <= set(STD3) else ax))
    L += ['', '### THE SALT-CHECK -- Lean`s #print of each definition (no sorry):']
    salt = {}
    for d in decls:
        if d['kind'] != 'def':
            continue
        j = pr.find('def %s' % d['name'])
        blk = pr[j:j + 900].split(NL + 'def ')[0] if j >= 0 else ''
        salt[d['name']] = bool(blk) and 'sorry' not in blk
        L += ['    ' + x for x in blk.strip().split(NL)[:2]] if blk else ['    ### %s NOT PRINTED' % d['name']]
    salt_ok = all(salt.values()) if salt else True
    L.append('### ### **THE SALT-CHECK: %s** (%d definitions)' % (salt_ok, len(salt)))
    recs_all, ctl = [], (True,)
    for rel, names in c['record']:
        recs, ctl = Q.rowgen_record(names, rel, tip, pr)
        recs_all += recs
    L += ['', '### THE ROWGEN RECORD (rowgen.py`s extract_doc_body and definition_encoded IMPORTED, at %s):' % tip[:7]]
    for r in recs_all:
        L.append('    %-40s defenc %-5s %s | check %s' % (r['name'].split('.')[-1], r['defenc'], r['defenc_why'], bool(r['check'])))
    L.append('    control: definition_encoded on `def b560_ctl_stub : Prop := True` -> %s (must be True)' % (ctl,))
    thms = [n for n, r in rows.items() if r['grade'] != 'DEF']
    cnt = {k: sum(1 for n in thms if rows[n]['grade'] == k) for k in ('DERIVES', 'INTERFACES')}
    allstd = all(r['std3'] for r in rows.values())
    consstd = all(a is not None and set(a) <= set(STD3) for a in cons.values())
    heads = all(r['header_read'] for r in rows.values())
    gate = (allstd and consstd and salt_ok and heads and ctl[0] and not any(r['defenc'] for r in recs_all)
            and all(r['check'] for r in recs_all))
    L.append('### ### **THE GATE: EVERY PRINT THE STANDARD THREE %s ; EVERY HEADER READ %s ; THEOREMS %d (DERIVES %d, INTERFACES %d) ; '
             'DEFINITIONS %d ; CONSUMED %d AT THE STANDARD THREE %s ; THE SALT-CHECK %s => %s**'
             % (allstd, heads, len(thms), cnt['DERIVES'], cnt['INTERFACES'], len(rows) - len(thms), len(cons), consstd, salt_ok,
                'PASS' if gate else 'FAIL'))
    put_txt('b569_e0_%s.txt' % which, L)
    put_json('b569_e0_%s.json' % which, dict(rows=rows, consumed=cons, gate=gate, salt=salt_ok, rowgen=recs_all,
                                             rowgen_control=ctl[0], tip=tip, counts=cnt))
    return 0 if gate else 1


# ================================================================================ COMPONENT 6: THE RECORD
def _Q():
    import b566_record as R6
    return R6.Q


V011 = '19b7d1e48a40ca22618722306194404423dca224'
C_ASOF, C_TIER, C_TABLE, C_A6 = '54cc6f9c', 'afe32bba', '93cc2f4f', '386a2572'
CHI_MODS = ['ZetaGrowth', 'LocalCount', 'ZeroSummability', 'XiLogDeriv', 'CountByIntegral', 'Landau', 'GoodHeights']
HOLD_FACT = ('the odd Γ factor’s log-derivative bound on 1/2 ≤ σ ≤ 3/2 (Γℝ(s + 1): Zeta23’s norm_logDeriv_Gammaℝ_le, from '
             'digamma_growth_strip on 1/4 ≤ Re w ≤ 1, does not reach σ + 1 ∈ [3/2, 5/2])')


def _count(name):
    m = re.search(r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\. ### LIVE FAILING : (\d+) (\[[^\]]*\])?', rd(name))
    return (int(m.group(1)), int(m.group(2)), int(m.group(3)), m.group(4) or '[]') if m else None


def h20b():
    """### (R179)(2): H20b re-scored on the regenerated page's cells -- every open-looking Prop of b568's list joined to
    ### RiemannHypothesis by a node whose printed statement's top connective is ↔."""
    cells = jl('b569_node_cells.json')['cells']
    joins = [('Register4_positivity LiCoeff', 'SIDEExplicitFormula.PageConverses.register4_positivity_liCoeff_iff_rh'),
             ('∀ n, 0 ≤ (taylorCoeff riemannXi n).re', 'SIDEExplicitFormula.PageConverses.taylorCoeff_nonneg_iff_rh'),
             ('RiemannHypothesis ~ h2_sign', 'SIDEExplicitFormula.B321.h2_sign_iff_rh'),
             ('∀ L₀, h2_sign_upto L₀', 'SIDEExplicitFormula.B321.forall_upto_iff_rh'),
             ('conservationHypothesis', 'SIDEExplicitFormula.B321.ch_iff_rh'),
             ('∀ n, 0 ≤ LiCoeff n', 'SIDEExplicitFormula.LiCriterionBridge.li_nonneg_iff_rh'),
             ('arithmetic-limit positivity', 'SIDEExplicitFormula.LiCriterionBridge.arith_limit_nonneg_iff_rh')]
    rows = []
    for prop, node in joins:
        st = (cells.get(node) or {}).get('statement') or ''
        body = st.split(' : ', 1)[1] if ' : ' in st else ''
        iff = body.rstrip().endswith('↔ RiemannHypothesis')
        rows.append(dict(prop=prop, node=node, iff=iff, statement=st))
    ok = all(r['iff'] for r in rows)
    put_json('b569_h20b.json', dict(rows=rows, h20b='HELD' if ok else 'REFUTED', n=len(jl('b569_node_cells.json')['order'])))
    return ok


def scores():
    h20b()
    hb = jl('b569_h20b.json')
    rt, bk, cv = jl('b569_route.json'), jl('b569_bulka_generic.json'), jl('b569_converses.json')
    e0c, e0x = jl('b569_e0_converses.json'), jl('b569_e0_chi.json')
    r6, r7 = _count('b569_b566_rerun.txt'), _count('b569_b567_rerun.txt')
    asof = rd('b569_test_asof.txt')
    runs = rd('b569_page_runs.txt')
    kp = rd('b569_kernel_push_out.txt')
    hold = rd('b569_hold_verticalline.txt')
    # ### the `sorry` read: COMMENT-STRIPPED code of every .lean file on main (defect (h): a raw grep met a docstring's word)
    sorry_hits = []
    for f in [x for x in g(EF, 'ls-tree', '-r', '--name-only', 'main').split(NL) if x.endswith('.lean')]:
        code = strip_comments(g(EF, 'show', 'main:' + f))
        sorry_hits += ['%s:%d' % (f, i + 1) for i, l in enumerate(code.split(NL)) if re.search(r'(?<![\w.])sorry(?![\w])', l)]
    raw_hits = len([x for x in g(EF, 'grep', '-n', '-w', 'sorry', 'main', '--', '*.lean').split(NL) if x.strip()])
    ctl = bool(re.search(r'(?<![\w.])sorry(?![\w])', strip_comments('theorem x : True := by\n  sorry\n-- sorry in a comment')))
    sorry_main = ', '.join(sorry_hits)
    put_json('b569_sorry_read.json', dict(code_hits=sorry_hits, raw_word_hits=raw_hits, control_code_sorry_found=ctl))
    ns = [x for x in g(EF, 'diff', '--name-status', V010, 'main').split(NL) if x.strip()]
    kept = {b: g(EF, 'rev-parse', b).strip()[:12] for b in ('detection-region-b559', 'li-weil-b561', 'grh-weil-b562', 'li-weil-b563',
                                                             'grh-weil-b564', 'vendor-bulka-backport-b566', 'vendor-bulka-forward-b566',
                                                             'residue-discharge-b567', 'grh-weil-b567')}
    kept0 = dict(re.findall(r'^    (\S+) ([0-9a-f]{40})$', rd('b569_branches.txt'), re.M))
    kept_ok = all(kept0.get(b, '').startswith(v) for b, v in kept.items())
    v011 = ('tag v0.11 peeled local %s remote %s' % (V011, V011)) in kp
    one_err = len(re.findall(r'error:', hold)) == 1 and 'linarith failed' in hold and 'rc=1' in hold
    h21c = one_err and not sorry_main and ctl
    landed = cv['all_ok'] and e0c['gate'] and e0x['gate']
    no_mod = all(x.startswith('A') or x == 'M\tREADME.md' for x in ns)
    S = dict(
        H20b=(hb['h20b'], 'every open-looking Prop of b568`s list is joined to RiemannHypothesis by a node whose printed statement is '
              'a ↔: %s (data/b569_h20b.json, from the regenerated page`s cells)' % ', '.join(r['node'].split('.')[-1] for r in hb['rows'])),
        H21a=(rt['h21a'], 'the route consumes %d ZetaBounds declarations, all CONTINUATION (strip bounds %d, zero-free region %d); '
              'controls %s (data/b569_route.txt, written before any Component 5 build)' % (len(rt['cls']), len(rt['by']['STRIP BOUNDS']),
                                                                                       len(rt['by']['ZERO-FREE REGION']), rt['controls'])),
        H21b=('NOT SCORABLE', 'VACUOUS in its letter: the consumed subset carries no strip-bound name (H21a`s bank), so no strip bound`s '
              'χ-analogue is owed; read on the route`s own bounds, the χ-analogues of ZetaGrowth`s growth compiled from '
              'LFunction_eq_mul_integral, norm_integral_tail_le and Mathlib`s LFunction facts with no new analytic input '
              '(Chi/ZetaGrowth.lean); the Γ-factor fact named at the HOLD is VerticalLine`s, not a strip bound`s'),
        H21c=('HELD' if h21c else 'REFUTED', 'EF_lit_chi HELD at a named fact: %s -- one error in the attempt (data/b569_hold_verticalline.txt); '
              'no `sorry` on main (git grep: %s)' % (HOLD_FACT, 'none' if not sorry_main else sorry_main[:80])),
        H21d=(bk['h21d'], 'comment-stripped ζ-object naming in %d of 33 modules: %s (data/b569_bulka_generic.txt)' % (bk['count'], bk['direct'])),
        N1=('HELD' if (cv['all_ok'] and hb['h20b'] == 'HELD' and 'byte-identical: True' in runs) else 'REFUTED',
            'the four converse declarations print the standard three and read E0 as compositions; the page regenerated twice '
            'byte-identical at v0.11 with %d nodes; H20b %s' % (hb['n'], hb['h20b'])),
        N2=('HELD' if (r6 and r6[1] == 74 and r6[0] == 74 and r7 and r7[1] == 69 and r7[0] == 69 and '24 of 24 cases as wanted -- PASS' in asof)
            else 'REFUTED', 'b566 re-run %s of %s, b567 re-run %s of %s under the extended lines (data/b569_b566_rerun.txt, '
            'data/b569_b567_rerun.txt); the two-repository test 24 of 24' % (r6[1], r6[0], r7[1], r7[0])),
        N3=('HELD' if bk['h21d'] == 'HELD' else 'REFUTED', 'H21d %s: %d modules name a ζ object; the power-sum identity '
            '(taylorCoeff_eq_li_symmetrized) sits in Lc.LiCriterion.Fidelity, which names one (Fidelity :107)' % (bk['h21d'], bk['count'])),
        N4=('HELD' if rt['h21a'] == 'HELD' else 'REFUTED', 'H21a %s: the consumed subset lies in the continuation class alone' % rt['h21a']),
        N5=('HELD' if h21c else 'REFUTED', 'EF_lit_chi HELD at an archimedean fact (the odd Γ factor), not landing; its first clause '
            'VACUOUS (H21b NOT SCORABLE: no strip-bound name is consumed)'),
        N6=('HELD' if (v011 and landed and no_mod and kept_ok) else 'REFUTED',
            'v0.11 = %s made by push_gated.sh and read back, with the converses and the seven χ modules; v0.10..main: additions only '
            'and README appended (%d paths); the kept branches at their heads; nothing at Zenodo; nothing deposits' % (V011[:7], len(ns))),
        S1=('HELD' if bk['h21d'] == 'REFUTED' else 'REFUTED', 'H21d REFUTED at %d modules' % bk['count']),
        S2=('HELD' if not rt['by']['STRIP BOUNDS'] and not rt['by']['ZERO-FREE REGION'] else 'REFUTED',
            'continuation %d, strip bounds %d, zero-free region %d' % (len(rt['by']['CONTINUATION']), len(rt['by']['STRIP BOUNDS']),
                                                                      len(rt['by']['ZERO-FREE REGION']))),
        S3=('HELD' if h21c else 'REFUTED', 'the χ-analogue of RvM/ZetaGrowth compiled (Chi/ZetaGrowth.lean) and the route ran on through '
            'LocalCount, ZeroSummability, XiLogDeriv, CountByIntegral, Landau and GoodHeights; the HOLD is at VerticalLine'),
        counts=dict(b566=r6, b567=r7, nodes=hb['n'], chi_decls=len(e0x['rows']), conv_decls=len(e0c['rows'])),
    )
    put_json('b569_scores.json', S)
    for k in ('H20b', 'H21a', 'H21b', 'H21c', 'H21d', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'S1', 'S2', 'S3'):
        print('  %-5s %-13s %s' % (k, S[k][0], S[k][1][:140]))


DEFECTS = [
    '(a) THE LOCK GATE, RUN ONE, REFUSED: the satisfiability audit (data/audit_b569_reg_satisfiable.txt) carried no subject digest -- it '
    'was not stamped with the other face-subject records. Stamped; run two permitted (data/b569_lockgate_notes2.txt; run one kept as '
    'data/b569_lockgate_notes.txt). The face was not edited between the runs.',
    '(b) COMPONENTS OUT OF ORDER: Components 3 (Bulka, 05:47Z) and 4 (the route, 05:50Z) were banked before Component 2`s instruments, '
    'while Component 1`s build ran. No instrument read them; H21a was still scored before any Component 5 build.',
    '(c) THE HEREDOC BACKSLASH TRAP, THREE TIMES: patch566.py/patch567.py wrote b`\\r\\n` as real line breaks into b566_checks.py and '
    'b567_checks.py (a SyntaxError on the first run); the asof.py self-test line broke at a `\\n`; the hχ1 renaming regex of '
    'gen_goodheights.py lost its word boundaries (GoodHeights attempt 2 failed the same way as attempt 1). Each caught by its first run '
    'and rewritten without heredoc backslashes before any bank was read from it.',
    '(d) THE AS-OF LINE GAINED A THIRD FORM: b567`s suite reads b567`s old build tree D:/b567-lake-51e6992e, PRESENT at b567`s close and '
    'deleted at b568 by (R178)(2)(iv). It is a directory, not a repository, with no head; the ruling`s two forms did not fit, and the '
    'face`s reading (ii) named only them. The reader takes `present at close` as a third form (tools/asof.py, PRESENT); its one line is '
    'in data/b569_asof_b567.txt. Routed to the author.',
    '(e) THE HOLD`S PLACE: VerticalLine`s χ-analogue was attempted at its archimedean step only; its prime side (VerticalLine :100-:259; '
    'Mathlib`s LSeries_twist_vonMangoldt_eq is its χ-input) was not attempted, so "the earliest obstacle" is the first statement '
    'attempted that does not compile, not a proof that no earlier statement of the module fails. The fact named is derivable by '
    'Zeta23`s own compactness-and-Stirling argument on a wider strip; it was not attempted in this act.',
    '(f) THE E0 RULE`S LETTER ON TWO χ DECLARATIONS: LFunction_zeros_finite_of_isCompact (hK : IsCompact K) and EF_zero_sum_summable_chi '
    '(hk : ContDiff ℝ 2 k, hkc : HasCompactSupport k) read as carrying a premise, the domain pattern not covering those binder types. '
    'The rule is not edited; the reading is the rule`s; routed to the author.',
    '(g) THE TIER KEY MOVES ONE PAGE CELL: under (R179)(4) ch_iff_rh`s tier is computed from its printed facts (T0), where b568`s page '
    'printed T2 from its record grade ENCODES-CONCLUSION; the table carries no tier cell for it, so no CONFLICT. As the ruling defines; '
    'for the author.',
    '(h) THE FIRST SCORES RUN READ A DOCSTRING AS A `sorry`: the H21c predicate grepped the word on main and met DetectionRegion.lean '
    ':7-:8, prose saying the HELD branch`s bodies are `sorry` and kept off main; H21c printed REFUTED. The read now strips comments '
    'from every .lean file on main before looking (b569_sorry_read.json: code hits, the raw word count, the control), and the scores '
    'were re-run; no bank was read from the first run.',
    '(i) A CORRESPONDENCE ROW REFUSED, THEN WRITTEN OUT OF ORDER: row 417 (chiZeroConfig_local_count) carried the statement`s '
    'absolute-value bars, which corr_row.py refuses as cell boundaries (exit 2, nothing written); rows 418 and 419 were written '
    'after it in the same run, and 417 was written alone on retry with the bars as ‖ (rows_retry), so the ledger reads 414, 415, '
    '416, 418, 419, 417. No line is removed; the rows are each once.',
    '(j) THE SUITE`S FIRST PRE-PUSH RUN DID NOT START: a surplus parenthesis in one positive control (G-CONVERSE-PRINTS) was a '
    'SyntaxError at import; nothing was written by that run. Fixed and re-run; the banked pre-push reading is the second.',
]


def defects():
    put_txt('b569_defects.txt', ['### b569 -- THIS ACT`S OWN DEFECTS (the seat`s), as they occur.'] + ['    ' + d for d in DEFECTS])


def findings():
    """### FINDINGS: the act's entry (no grade word on a line with a backticked name -- A6). Appends only."""
    Q = _Q()
    S = jl('b569_scores.json')
    rt, bk = jl('b569_route.json'), jl('b569_bulka_generic.json')
    title = ('## GRH-Weil, act four: the explicit formula for χ by the ζ route, the ZetaBounds subset by class, held at the odd Γ '
             'factor’s log-derivative bound; the page’s two converses; Bulka’s modules read')
    Q.guard_absent(Q.FIND, title)
    c = S['counts']
    e = ['', title, '',
         '*Filed at b569 on the author’s ruling `(R179)`. Banks: relay `data/b569_converses.txt`, `data/b569_route.txt`, '
         '`data/b569_bulka_generic.txt`, `data/b569_chi_prints.txt`, `data/b569_e0_chi.txt`, `data/b569_e0_converses.txt`, '
         '`data/b569_hold_verticalline.txt`, `data/b569_page_runs.txt`, `data/b569_page_diff.txt`, `data/b569_h20b.json`, '
         '`data/b569_test_asof.txt`, `data/b569_test_chain_page.txt`, `data/b569_test_push_gated.txt`, `data/b569_b566_rerun.txt`, '
         '`data/b569_b567_rerun.txt`. Nothing about the zeros of ζ or of any L(s, χ) is claimed beyond the compiled statements’ own '
         'words.*', '',
         '**b568 at its weight** (`(R179)`(1)): the page stands under its name; H20a, H20c, H20d held and H20b was refuted in letter at '
         'two places; the 146 ZetaBounds names fall as continuation 68, strip bounds 39, zero-free region 39.', '',
         '**The two converses** (`(R179)`(2)). SIDE-explicit-formula `PageConverses.lean` at v0.11 = `%s`: the converse of each '
         'compiled implication the page carried, and each joined into an iff -- `register4_positivity_liCoeff_iff_rh` and '
         '`taylorCoeff_nonneg_iff_rh` -- compositions of `rh_imp_li_nonneg`, `li_coeff_eq_taylorCoeff` and Bulka’s '
         '`positivity_implies_RH`; all four print [propext, Classical.choice, Quot.sound]. The page '
         '`THE_CLAUSE_AND_ITS_COMPILED_FACES.md` is regenerated at v0.11 from relay `data/b569_nodes.txt` (%d nodes), twice '
         'byte-identical; every open-looking statement on it is now joined to RiemannHypothesis by a compiled ↔. H20b %s.'
         % (V011[:7], c['nodes'], S['H20b'][0]), '',
         '**The instruments** (`(R179)`(3)-(5)), each committed alone with its test. The as-of lines (relay `%s`): one line per '
         'repository the suite reads, from the act’s push-out bank or a companion bank; b566 re-runs %d of %d and b567 %d of %d; '
         'the two-repository test 24 of 24. The tier key (relay `%s`): the page’s head carries the key sentence, a node’s tier is '
         'computed from its printed facts and the table’s tier is printed beside it; a disagreement refuses the page (18 of 18). '
         'The table check (relay `%s`, FERRY_STANDING A6 `%s`): a PLACE-papers push regenerates the terminal table in memory and '
         'refuses a moved grade cell the face does not name (29 of 29).'
         % (C_ASOF, c['b566'][1], c['b566'][0], c['b567'][1], c['b567'][0], C_TIER, C_TABLE, C_A6), '',
         '**Bulka’s modules read** (W-ORD-BULKA-GENERIC). By b564’s rule, %d of the 33 vendored modules name a ζ object in their '
         'comment-stripped code and %d are ζ-specific with their importers; the Hadamard and complex-variable modules are generic. '
         'The converse is not an argument over a zero configuration: it is stated for Bulka’s own `riemannXi` and its zero type; its '
         'ζ-specific inputs are ξ, the identification of ξ’s zeros with ζ’s nontrivial zeros, and the reflection ρ ↦ 1 − ρ. H21d %s.'
         % (bk['count'], len(bk['propagated']), S['H21d'][0]), '',
         '**The route** (`(R179)`(6)). From `EF_lit_zetaZeroConfig` the constant walk reaches %d Zeta23 constants; the ZetaBounds '
         'ones fold to %d declarations, all in the continuation class, entering through RvM’s half-plane bound. H21a %s.'
         % (rt['reached'], len(rt['cls']), S['H21a'][0]), '',
         '**The build.** On grh-weil-b569, in the route’s import order, seven χ-modules: ZetaGrowth (the half-plane bound '
         '‖L(s, χ)‖ ≤ (N + 1)‖s‖/Re s and its growth forms), LocalCount (N_χ(t, t+1] ≤ A₀ log(|t| + 3)), ZeroSummability (the '
         'Summable conjunct of `EF_lit_chi`), XiLogDeriv (the completed function’s log-derivative and its functional equation across '
         'χ and χ⁻¹, carrying log N; the root number shown nonzero), CountByIntegral (the completed function’s zeros), Landau (the '
         'partial fraction for L′/L) and GoodHeights -- %d declarations, every print within the standard three, merged by '
         'fast-forward and tagged v0.11 by the push script. **HELD** at the χ-analogue of VerticalLine: %s; the attempt is on '
         '`grh-weil-b569-held` and is not on main. H21b %s; H21c %s.'
         % (c['chi_decls'], HOLD_FACT, S['H21b'][0], S['H21c'][0]), '',
         '**The scores.** H20b %s; H21a %s; H21b %s; H21c %s; H21d %s. (N1) %s, (N2) %s, (N3) %s, (N4) %s, (N5) %s, (N6) %s; the '
         'seat’s (S1) %s, (S2) %s, (S3) %s.' % tuple(S[k][0] for k in ('H20b', 'H21a', 'H21b', 'H21c', 'H21d', 'N1', 'N2', 'N3', 'N4',
                                                                     'N5', 'N6', 'S1', 'S2', 'S3')), '',
         '**Next.** `EF_lit_chi` is HELD, so per `(R179)`(7): GRH-Weil act five at the frontier -- VerticalLine’s χ-analogue, '
         'beginning at the odd Γ factor’s bound. The author rules on the closing.', '',
         '*Nothing deposits; nothing at Zenodo written; no existing statement of any kernel changed; no sentence here claims priority; '
         'nothing here is a statement about RH, GRH or any zero beyond the compiled statements’ own words.*', '']
    r = Q.append_to(Q.FIND, NL.join(e))
    put_json('b569_findings.json', dict(entry_line=Q.line_of(Q.FIND, title), append=r, title=title))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, title))


def trail():
    """### OPEN_TRAILS: the W-ORD-GRH-WEIL line, the W-ORD-BULKA-GENERIC line, the act's record. Appends."""
    Q = _Q()
    S = jl('b569_scores.json')
    fj, rt, bk = jl('b569_findings.json'), jl('b569_route.json'), jl('b569_bulka_generic.json')
    wg = Q.line_of(Q.OT, '### `W-ORD-GRH-WEIL` -- THE χ-SIDE OF THE WEIL ARC')
    head = ('### b569 — lane two, act nine under (R179): GRH-Weil act four -- the explicit formula for χ by the ζ route to its good '
            'heights, held at VerticalLine’s odd Γ factor; the page’s two converses; the as-of lines, the tier key, the table check')
    Q.guard_absent(Q.OT, head)
    a1 = ('\n*Appended 2026-10-01 by b569, under the author’s ruling `(R179)`(6), to the W-ORD-GRH-WEIL entry (:%s) -- THE ROUTE AND '
          'ITS FRONTIER:* EF_lit’s proof consumes %d ZetaBounds declarations, all continuation (relay `data/b569_route.txt`); their '
          'roles are carried by the χ-analogues compiled at b567. The route’s χ-analogues through GoodHeights are compiled at v0.11 '
          '= `%s` (seven Chi modules); the Summable conjunct of `EF_lit_chi` is `EF_zero_sum_summable_chi`. The frontier is '
          'VerticalLine: %s.\n' % (wg, len(rt['cls']), V011[:7], HOLD_FACT))
    wb = Q.line_of(Q.OT, '| **3** | `W-ORD-BULKA-GENERIC`')
    a2 = ('\n*Appended 2026-10-01 by b569 to W-ORD-BULKA-GENERIC (:%s) -- DONE as a read:* %d of 33 modules name a ζ object, %d are '
          'ζ-specific with their importers; the converse is stated over Bulka’s own ξ and zero type, not a zero configuration (relay '
          '`data/b569_bulka_generic.txt`).\n' % (wb, bk['count'], len(bk['propagated'])))
    rows = ['', head, '',
            '**(R179) ratified.** (1) b568 entered at its weight. (2) The two converses compiled. (3) The as-of commit extended to every '
            'repository the suite reads. (4) The tier cell defined on the page’s head. (5) Defect (k) made a pre-push check, a standing '
            'line. (6) GRH-Weil act four. (7) The gates; v0.11 by the push script; the next act named at the closing.', '',
            '**Entered:** FINDINGS.md:%s (the entry); OPEN_TRAILS.md (the W-ORD-GRH-WEIL line, the W-ORD-BULKA-GENERIC line, this record); '
            'PLACE-papers `THE_CLAUSE_AND_ITS_COMPILED_FACES.md` (regenerated at v0.11); relay `tools/FERRY_STANDING.md` A6; '
            'SIDE-global-section CORRESPONDENCE.md rows 414-419; SIDE-explicit-formula main = **v0.11** = `%s`, grh-weil-b569 and '
            'grh-weil-b569-held pushed by name. Relay instrument commits: the as-of lines `%s`, the tier key `%s`, the table check '
            '`%s`, A6 `%s`.' % (fj['entry_line'], V011[:7], C_ASOF, C_TIER, C_TABLE, C_A6), '',
            '**H20b %s · H21a %s · H21b %s · H21c %s · H21d %s. (N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s · (N6) %s.** The seat’s '
            'own: (S1) %s, (S2) %s, (S3) %s.' % tuple(S[k][0] for k in ('H20b', 'H21a', 'H21b', 'H21c', 'H21d', 'N1', 'N2', 'N3', 'N4',
                                                                        'N5', 'N6', 'S1', 'S2', 'S3')), '',
            '**Next:** per `(R179)`(7), with `EF_lit_chi` HELD: GRH-Weil act five at the frontier -- the χ-analogue of VerticalLine, '
            'beginning at the odd Γ factor’s log-derivative bound. The author rules on the closing.', '',
            '**No `sorry` on any `main`.** Nothing deposits; nothing at Zenodo written; no existing statement changed; no Zeta23 or '
            'vendored file edited or added; no monograph byte changed; ERRATA untouched; the ceiling unchanged; row U1 unedited; `h2` '
            'where the deposit left it; the four lists stay OPEN; nothing here is a statement about RH, GRH or any zero beyond the '
            'compiled statements’ own words.', '']
    r = [Q.append_to(Q.OT, a1), Q.append_to(Q.OT, a2), Q.append_to(Q.OT, NL.join(rows))]
    put_json('b569_trail.json', dict(grh_line=Q.line_of(Q.OT, '*Appended 2026-10-01 by b569, under the author’s ruling `(R179)`(6)'),
                                     bulka_line=Q.line_of(Q.OT, '*Appended 2026-10-01 by b569 to W-ORD-BULKA-GENERIC'),
                                     line=Q.line_of(Q.OT, head), head=head, appends=r))
    print(json.dumps(jl('b569_trail.json'), ensure_ascii=False)[:300])


ROW_ACT = '414'
TERMS = [('415', 'SIDEExplicitFormula.PageConverses.', 'register4_positivity_liCoeff_iff_rh', 'SIDEExplicitFormula/PageConverses.lean',
          'converses'),
         ('416', 'SIDEExplicitFormula.PageConverses.', 'taylorCoeff_nonneg_iff_rh', 'SIDEExplicitFormula/PageConverses.lean', 'converses'),
         ('417', 'SIDEExplicitFormula.GRHWeil.', 'chiZeroConfig_local_count', 'SIDEExplicitFormula/Chi/LocalCount.lean', 'chi'),
         ('418', 'SIDEExplicitFormula.GRHWeil.', 'logDeriv_completedLFunction_one_sub', 'SIDEExplicitFormula/Chi/XiLogDeriv.lean', 'chi'),
         ('419', 'SIDEExplicitFormula.GRHWeil.', 'good_heights_chi', 'SIDEExplicitFormula/Chi/GoodHeights.lean', 'chi')]


def rows():
    """### the act's row and one row per terminal of record, through relay tools/corr_row.py; each terminal's grade is its E0
    ### reading at main (a print-backed reading), checked DERIVES before the row is written."""
    Q = _Q()
    for rn in (ROW_ACT,) + tuple(t[0] for t in TERMS):
        if [l for l in Q.rd(Q.CORR).split(NL) if l.startswith('| %s |' % rn)]:
            sys.exit('### ROW %s ALREADY PRESENT' % rn)
    e = {'converses': jl('b569_e0_converses.json'), 'chi': jl('b569_e0_chi.json')}
    for rn, ns, n, rel, which in TERMS:
        if e[which]['rows'][ns + n]['grade'] != 'DERIVES' or not e[which]['rows'][ns + n]['std3']:
            sys.exit('### %s is not graded at the standard three by E0: no row' % n)
    out = []
    act = [ROW_ACT,
           '**GRH-WEIL ACT FOUR AND THE PAGE`S CONVERSES** (b569, under (R179)(2), (6)). SIDE-explicit-formula v0.11 = %s: the '
           'converses of the two compiled implications the page carried, joined into iffs (PageConverses.lean); the χ-analogues of '
           'EF_lit`s route from RvM/ZetaGrowth through WeilEF/GoodHeights (seven Chi modules), the Summable conjunct of EF_lit_chi '
           'among them; EF_lit_chi HELD at VerticalLine`s odd Γ factor. Nothing here proves RH or GRH.' % V011[:7],
           'SIDE-explicit-formula SIDEExplicitFormula/PageConverses.lean and SIDEExplicitFormula/Chi/{%s}.lean (v0.11 = %s)'
           % (','.join(CHI_MODS), V011[:7]),
           '%d declarations print within [propext, Classical.choice, Quot.sound], no sorryAx (relay data/b569_converse_axiomcheck.txt, '
           'data/b569_chi_prints.txt)' % (len(e['converses']['rows']) + len(e['chi']['rows'])),
           ' ; '.join('`%s` DERIVES' % t[2] for t in TERMS),
           'LANDED at v0.11 = %s; EF_lit_chi HELD (branch grh-weil-b569-held); nothing deposits; nothing at Zenodo written.' % V011[:7]]
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'corr_row.py'), Q.CORR] + act, capture_output=True, text=True,
                       encoding='utf-8')
    out.append(dict(row=ROW_ACT, exit=r.returncode, tail=(r.stdout + r.stderr)[-300:]))
    pr = {**prints_axioms(rd('b569_converse_axiomcheck.txt')), **prints_axioms(rd('b569_chi_prints.txt'))}
    for rn, ns, n, rel, which in TERMS:
        head = e[which]['rows'][ns + n]['head']
        cells = [rn,
                 '**%s** (b569, under (R179)(%s)), SIDE-explicit-formula v0.11 = %s: `%s%s %s`.' % (n, '2' if which == 'converses' else '6',
                                                                                                   V011[:7], ns, n, head),
                 '`SIDE-explicit-formula/%s` (v0.11 = %s) : `%s%s`' % (rel, V011[:7], ns, n),
                 '\'%s%s\' depends on axioms: [%s] (relay data/%s)' % (ns, n, ', '.join(pr.get(ns + n) or []),
                                                                       'b569_converse_axiomcheck.txt' if which == 'converses' else 'b569_chi_prints.txt'),
                 '`%s` DERIVES' % n,
                 'LANDED at v0.11 = %s; the E0 read at main (relay data/b569_e0_%s.txt); no premise.' % (V011[:7], which)]
        r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'corr_row.py'), Q.CORR] + cells, capture_output=True, text=True,
                           encoding='utf-8')
        out.append(dict(row=rn, exit=r.returncode, tail=(r.stdout + r.stderr)[-300:]))
    put_json('b569_rows.json', dict(rows=out, act=act))
    print('  rows', [(o['row'], o['exit']) for o in out])


def rows_retry():
    """### defect (i): a terminal row refused by corr_row.py (a `|` in its statement cell) is written alone, `|` → `‖` in that cell
    ### as the tool directs; rows already present are not touched; the result is merged into b569_rows.json."""
    Q = _Q()
    rj = jl('b569_rows.json')
    e = {'converses': jl('b569_e0_converses.json'), 'chi': jl('b569_e0_chi.json')}
    pr = {**prints_axioms(rd('b569_converse_axiomcheck.txt')), **prints_axioms(rd('b569_chi_prints.txt'))}
    present = set(l.split('|')[1].strip() for l in Q.rd(Q.CORR).split(NL) if l.startswith('| 41'))
    for rn, ns, n, rel, which in TERMS:
        if rn in present:
            continue
        head = e[which]['rows'][ns + n]['head'].replace('|', '‖')
        cells = [rn,
                 '**%s** (b569, under (R179)(6)), SIDE-explicit-formula v0.11 = %s: `%s%s %s`.' % (n, V011[:7], ns, n, head),
                 '`SIDE-explicit-formula/%s` (v0.11 = %s) : `%s%s`' % (rel, V011[:7], ns, n),
                 '\'%s%s\' depends on axioms: [%s] (relay data/b569_chi_prints.txt)' % (ns, n, ', '.join(pr.get(ns + n) or [])),
                 '`%s` DERIVES' % n,
                 'LANDED at v0.11 = %s; the E0 read at main (relay data/b569_e0_%s.txt); no premise; the statement`s absolute-value '
                 'bars written ‖ for the ledger`s cell boundary.' % (V011[:7], which)]
        r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'corr_row.py'), Q.CORR] + cells, capture_output=True, text=True,
                           encoding='utf-8')
        rj['rows'].append(dict(row=rn, exit=r.returncode, tail=(r.stdout + r.stderr)[-300:], retry=True))
    put_json('b569_rows.json', rj)
    print('  rows', [(o['row'], o['exit']) for o in rj['rows']])


def rowgen_diff():
    """### rowgen.diff (IMPORTED) of the E0 read's rowgen records against the terminal rows 415-419."""
    Q = _Q()
    sys.path.insert(0, os.path.join(ROOT, 'tools', 'rowgen'))
    import rowgen as RG
    recs = jl('b569_e0_converses.json').get('rowgen', []) + jl('b569_e0_chi.json').get('rowgen', [])
    for r in recs:
        r['exists'] = bool(r.get('check'))
        r['axioms'] = ("'%s' depends on axioms: [%s]" % (r['name'], ', '.join(r['axioms'] or []))
                       if isinstance(r.get('axioms'), list) else (r.get('axioms') or ''))
    L = ['b569 -- COMPONENT 5: THE ROWGEN DIFF (rowgen.diff IMPORTED) OF THE RECORDS AGAINST CORRESPONDENCE ROWS 415-419', '']
    res = {}
    for rn, ns, n, rel, which in TERMS:
        rowtxt = [l for l in Q.rd(Q.CORR).split(NL) if l.startswith('| %s |' % rn)]
        out = RG.diff(recs, NL.join(rowtxt))
        mine = [x for x in out if isinstance(x, tuple) and x[0] == ns + n]
        res[rn] = dict(found=len(rowtxt) == 1, out=[list(x) if isinstance(x, tuple) else x for x in out], mine=[list(x) for x in mine])
        L.append('### row %s found: %s ; records %d' % (rn, len(rowtxt) == 1, len(recs)))
        L += ['    ' + str(x) for x in out]
    ok = all(v['found'] and v['mine'] and all(m[1] == ['ok'] for m in v['mine']) for v in res.values())
    L += ['', '### ### **THE ROWGEN DIFF : %s** -- every terminal row`s own record reads [`ok`]' % ('CLEAN' if ok else 'NOT CLEAN')]
    put_txt('b569_rowgen.txt', L)
    put_json('b569_rowgen.json', dict(rows=res, clean=ok))


def desk():
    S = jl('b569_scores.json')
    L = ['=' * 104, 'b569 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H20b RE-SCORED ((R179)(2)) AND H21a-H21d ((R179)(6)).', '-' * 104]
    for k in ('H20b', 'H21a', 'H21b', 'H21c', 'H21d'):
        L.append('  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]))
    L += ['', '### THE NAVIGATOR`S SIX.', '-' * 104]
    for k in ('N1', 'N2', 'N3', 'N4', 'N5', 'N6'):
        L.append('  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]))
    L += ['', '### THE SEAT`S THREE.', '-' * 104]
    for k in ('S1', 'S2', 'S3'):
        L.append('  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]))
    nh = sum(1 for k in ('N1', 'N2', 'N3', 'N4', 'N5', 'N6') if S[k][0] == 'HELD')
    sh = sum(1 for k in ('S1', 'S2', 'S3') if S[k][0] == 'HELD')
    L += ['', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE 0.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; '
          'REFUTED %d.**' % (nh, 6 - nh, sh, 3 - sh),
          '### ### **H20b %s ; H21 : %s.**' % (S['H20b'][0], ' ; '.join('%s %s' % (k, S[k][0]) for k in ('H21a', 'H21b', 'H21c', 'H21d'))), '']
    L += rd('b569_defects.txt').rstrip(NL).split(NL)
    put_txt('b569_desk_notes.txt', L)


def components():
    S = jl('b569_scores.json')
    fj, tj, rj, rt, bk = jl('b569_findings.json'), jl('b569_trail.json'), jl('b569_rows.json'), jl('b569_route.json'), jl('b569_bulka_generic.json')
    c = S['counts']
    L = ['b569 -- THE COMPONENTS, BANKED UNDER (R179).', '',
         '### COMPONENT 0 : the process listing (no orphan, data/b569_procs_stepzero.txt) ; push-b568, push-b568-closing and '
         'push-b568-housekeeping deleted by name after --merged listed them (data/b569_branches.txt) ; the kept branches at their heads',
         '### COMPONENT 1 : PageConverses.lean (kernel 23c29cc), statements first (data/b569_converse_statements.txt), built, 4 of 4 at the '
         'standard three (data/b569_converses.txt) ; data/b569_nodes.txt %d nodes ; the page regenerated at v0.11 twice byte-identical '
         '(data/b569_page_runs.txt, data/b569_page_diff.txt) ; H20b %s' % (c['nodes'], S['H20b'][0]),
         '### COMPONENT 2 : the as-of lines relay %s (24 of 24), companions data/b569_asof_b566.txt, data/b569_asof_b567.txt ; b566 re-run %s '
         'of %s, b567 re-run %s of %s ; the tier key relay %s (18 of 18) ; the table check relay %s (29 of 29) ; A6 relay %s'
         % (C_ASOF, c['b566'][1], c['b566'][0], c['b567'][1], c['b567'][0], C_TIER, C_TABLE, C_A6),
         '### COMPONENT 3 : data/b569_bulka_generic.txt ; %d of 33 name a ζ object ; H21d %s' % (bk['count'], S['H21d'][0]),
         '### COMPONENT 4 : data/b569_route.txt ; %d consumed, continuation %d ; H21a %s' % (len(rt['cls']), len(rt['by']['CONTINUATION']), S['H21a'][0]),
         '### COMPONENT 5 : seven Chi modules on grh-weil-b569 (%s) ; %d declarations within the standard three ; v0.11 = %s by push_gated.sh '
         '(data/b569_kernel_push_out.txt) ; HELD at VerticalLine (data/b569_hold_verticalline.txt, grh-weil-b569-held) ; H21b %s, H21c %s'
         % (', '.join(CHI_MODS), c['chi_decls'], V011[:7], S['H21b'][0], S['H21c'][0]),
         '### COMPONENT 6 : the entry FINDINGS :%s ; OPEN_TRAILS :%s (W-ORD-GRH-WEIL), :%s (W-ORD-BULKA-GENERIC), :%s (the record) ; '
         'CORRESPONDENCE rows %s ; next: GRH-Weil act five at the frontier'
         % (fj['entry_line'], tj['grh_line'], tj['bulka_line'], tj['line'], ', '.join('%s (exit %d)' % (o['row'], o['exit']) for o in rj['rows']))]
    put_txt('b569_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd in ('scores', 'defects', 'findings', 'trail', 'rows', 'rows_retry', 'rowgen_diff', 'desk', 'components'):
        globals()[cmd]()
        sys.exit(0)
    if cmd == 'e0':
        sys.exit(e0(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else 'main'))
    fn = dict(reads=reads, converses=converses, bulka=bulka, route=route, companions=companions).get(cmd)
    if fn is None:
        print('usage: b569_record.py <reads|converses|bulka|...>')
        sys.exit(2)
    fn()
