# -*- coding: utf-8 -*-
"""b562_record.py -- LANE TWO, ACT FOUR: W-ORD-GRH-WEIL, ACT ONE -- THE χ-SIDE STATEMENT LAYER, THE SEAM AND THE PAIRING;
LiLimitExchange MARKED; THE DRIFT READ ON THE BENCH; (X2) FILED: THE RECORD, UNDER (R172).
### `python tools/b562_record.py reads | weight | modules | part <a|b|c> | e0 | x2 | findings | rows | rowgen_diff | workorders |
### trail | components | desk`. b560's and b561's helpers are IMPORTED, never copied. This file deletes nothing.
"""
import io, json, os, re, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
import b561_record as Z1  # noqa: E402
Q = Z1.Q
P = Q.P
PP, FIND, OT, CORR, EF, LV = Q.PP, Q.FIND, Q.OT, Q.CORR, Q.EF, Q.LV
NL = chr(10)
rd, g, append_to, guard_absent, poss, line_of = Q.rd, Q.g, Q.append_to, Q.guard_absent, Q.poss, Q.line_of
at, decl_at, statement, statement_block = Q.at, Q.decl_at, Q.statement, Q.statement_block
parse_prints, check_line, rowgen_record, STD3 = Q.parse_prints, Q.check_line, Q.rowgen_record, Q.STD3


def parse_prints(text):
    """### Lean`s `#print axioms` lines -> {name: [axioms]}, READING A LIST LEAN WRAPPED ACROSS LINES (b562: the inherited reader
    ### is line-based and missed two wrapped prints)."""
    out = {}
    for m in re.finditer(r"'([^']+)' depends on axioms: \[([^\]]*)\]", text or '', re.S):
        out[m.group(1)] = [x.strip() for x in m.group(2).replace(NL, ' ').split(',') if x.strip()]
    for m in re.finditer(r"'([^']+)' does not depend on any axioms", text or ''):
        out[m.group(1)] = []
    return out
put_txt, put_json, jl = Q.put_txt, Q.put_json, Q.jl
PRIOR_RELAY = '2f269c11'   # ### b561's table housekeeping -- relay's tip before this act
PRIOR_PP = '75bd731'
PRIOR_GS = '347fac8'
V05 = '2df46d79bd59a900dde5b8ad8240faa2a0471cdc'
BR = 'grh-weil-b562'
MAIN_MOD = 'SIDEExplicitFormula/GRHWeil.lean'
NSG = 'SIDEExplicitFormula.GRHWeil.'
MATHLIB = os.path.join(EF, '.lake', 'packages', 'mathlib')
SCR = os.environ.get('B562_SCRATCH') or os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Temp')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ML_DECLS = [
    ('Mathlib/NumberTheory/LSeries/DirichletContinuation.lean', 'LFunction'),
    ('Mathlib/NumberTheory/LSeries/DirichletContinuation.lean', 'gammaFactor'),
    ('Mathlib/NumberTheory/LSeries/DirichletContinuation.lean', 'completedLFunction'),
    ('Mathlib/NumberTheory/LSeries/DirichletContinuation.lean', 'LFunction_eq_completed_div_gammaFactor'),
    ('Mathlib/NumberTheory/LSeries/DirichletContinuation.lean', 'rootNumber'),
    ('Mathlib/NumberTheory/LSeries/DirichletContinuation.lean', 'completedLFunction_one_sub'),
    ('Mathlib/NumberTheory/LSeries/DirichletContinuation.lean', 'Even.LFunction_neg_two_mul_nat'),
    ('Mathlib/NumberTheory/LSeries/DirichletContinuation.lean', 'Odd.LFunction_neg_two_mul_nat_sub_one'),
    ('Mathlib/NumberTheory/LSeries/DirichletContinuation.lean', 'LFunction_eq_LSeries'),
    ('Mathlib/NumberTheory/LSeries/DirichletContinuation.lean', 'differentiable_LFunction'),
    ('Mathlib/NumberTheory/LSeries/Nonvanishing.lean', 'LFunction_ne_zero_of_one_le_re'),
    ('Mathlib/Analysis/SpecialFunctions/Gamma/Deligne.lean', 'Gammaℝ_ne_zero_of_re_pos'),
    ('Mathlib/Analysis/SpecialFunctions/Gamma/Beta.lean', 'Gamma_eq_zero_iff'),
    ('Mathlib/NumberTheory/DirichletCharacter/Basic.lean', 'conductor_inv'),
    ('Mathlib/NumberTheory/MulChar/Lemmas.lean', 'star_apply\''),
]


def ml_decl(rel, name):
    t = rd(os.path.join(MATHLIB, rel)).replace(chr(13), '')
    pat = re.compile(r'^\s*(?:@\[[^\]]*\]\s*)?(?:noncomputable\s+|private\s+|protected\s+)*(?:theorem|lemma|def)\s+' + re.escape(name) + r'(?=[\s:({\[]|$)')
    for i, l in enumerate(t.split(NL)):
        if pat.match(l):
            return i + 1, statement(t, i + 1, 6)
    return None, []


def reads():
    L = ['b562 -- READING (1): THE READS, PRINTED BY PATH AND LINE', '### SIDE-explicit-formula v0.5 = %s ; Mathlib at %s' % (V05[:7], g(MATHLIB, 'rev-parse', '--short', 'HEAD').strip()), '']
    lw = at(V05, 'SIDEExplicitFormula/LiWeil.lean')
    for n in ('LiLimitExchange', 'li_identity_of_exchange', 'truncMember'):
        k = decl_at(lw, n)
        L.append('### LiWeil.lean:%d @2df46d7 -- %s' % (k, n))
        L += ['    %5d | %s' % (k + i, l) for i, l in enumerate(statement(lw, k, 10))]
    h2 = at(V05, 'SIDEExplicitFormula/H2Sign.lean').split(NL)
    L.append('### H2Sign.lean:24-31 @2df46d7:')
    L += ['    %5d | %s' % (i + 1, h2[i]) for i in range(23, 31)]
    sm = at(V05, 'SIDEExplicitFormula/Seam.lean')
    L.append('### Seam.lean @2df46d7 (the template): its declarations:')
    for m in re.finditer(r'^(theorem|def|lemma)\s+(\S+)', sm, re.M):
        L.append('    Seam.lean:%d %s %s' % (sm[:m.start()].count(NL) + 1, m.group(1), m.group(2)))
    dr = rd(os.path.join(D, 'b561_decay_read.txt')).split(NL)
    for i, l in enumerate(dr):
        if l.startswith('### (7)') or l.startswith('### (9)'):
            L.append('    b561_decay_read.txt:%d | %s' % (i + 1, l[:200]))
    L.append('')
    L.append('### THE MATHLIB CHECKOUT at the kernel`s rev, the Dirichlet L-function facts:')
    rows = []
    for rel, name in ML_DECLS:
        k, st = ml_decl(rel, name.split('.')[-1] if name.startswith(('Even.', 'Odd.')) and False else name)
        if k is None and '.' in name:
            k, st = ml_decl(rel, name.split('.', 1)[1])
        L.append('    %s:%s | %s' % (rel.replace('Mathlib/', ''), k, ' '.join(x.strip() for x in st)[:260] if st else '### NOT FOUND'))
        rows.append(dict(file=rel, name=name, line=k))
    for pat, what in ((r'LFunction[^\n]*conj|conj[^\n]*LFunction|starRingEnd[^\n]*LFunction', 'a conjugation lemma for LFunction'),
                      (r'rootNumber_ne_zero|norm_rootNumber|abs_rootNumber', 'a rootNumber nonvanishing or norm lemma')):
        hits = []
        for dp, dn, fn in os.walk(os.path.join(MATHLIB, 'Mathlib', 'NumberTheory')):
            for f in fn:
                if f.endswith('.lean'):
                    t = rd(os.path.join(dp, f))
                    if re.search(pat, t):
                        hits.append(os.path.relpath(os.path.join(dp, f), MATHLIB).replace(os.sep, '/'))
        L.append('    ### the search for %s under Mathlib/NumberTheory (regex %s): %d files %s' % (what, pat, len(hits), hits[:5]))
    zs = sorted(os.path.relpath(os.path.join(dp, f), EF).replace(os.sep, '/') for dp, dn, fn in os.walk(os.path.join(EF, 'Zeta23')) for f in fn if f.endswith('.lean'))
    L.append('')
    L.append('### Zeta23`s files: %d' % len(zs))
    try:
        import numpy as np
        gam = np.load(os.path.join(T, 'e16', 'zeta_ordinates.npy'))
        L.append('### the chain bank tools/e16/zeta_ordinates.npy: shape %s ; first %s ; the 10,000th %.6f' % (gam.shape, [round(float(x), 6) for x in gam[:3]], float(gam[9999])))
    except Exception as e:
        L.append('### the chain bank: ### NOT LOADED (%s)' % e)
    B = rd(Q.BALPOS).split(NL)
    L.append('### BALPOS :289-:320 (λ_n, the literature column and the margin table):')
    L += ['    BALPOS:%d | %s' % (i + 1, B[i][:160]) for i in range(288, 320) if B[i].startswith('|')]
    R125 = rd(os.path.join(D, 'b516_ferry.txt')).split(NL)
    L.append('### relay data/b516_ferry.txt:18-21 ((R125)(2)) | ' + ' '.join(R125[17:21]))
    L.append('### the remote`s refs of SIDE-explicit-formula (ls-remote origin):')
    L += ['    ' + x for x in g(EF, 'ls-remote', 'origin').split(NL) if x.strip()]
    put_txt('b562_reads.txt', L)
    put_json('b562_reads.json', dict(mathlib=rows, zeta23=zs, remote=[x for x in g(EF, 'ls-remote', 'origin').split(NL) if x.strip()]))
    print('  written: b562_reads.txt (%d lines) ; Zeta23 files %d' % (len(L), len(zs)))



# ------------------------------------------------------------------------------ READING (5)(d): the Zeta23 module table
ZMARKERS = ('riemannZeta', 'completedRiemannZeta', 'zetaZeroConfig', 'zetaSeam', 'ZetaSeam', 'IsNontrivialZero', 'zeroMult',
            'zerosIn', 'Ncount')


def strip_lean_comments(t):
    t = re.sub(r'/-.*?-/', ' ', t, flags=re.S)
    return re.sub(r'--[^\n]*', ' ', t)


def modules():
    root = os.path.join(EF, 'Zeta23')
    files = sorted(os.path.relpath(os.path.join(dp, f), EF).replace(os.sep, '/') for dp, dn, fn in os.walk(root) for f in fn if f.endswith('.lean'))
    mod_of = {f: f[:-5].replace('/', '.') for f in files}
    info = {}
    for f in files:
        src = rd(os.path.join(EF, f)).replace(chr(13), '')
        code = strip_lean_comments(src)
        imps = re.findall(r'^import\s+(\S+)', src, re.M)
        z_imps = [m for m in imps if m.startswith('Zeta23.')]
        found = [m for m in ZMARKERS if re.search(r'(?<![A-Za-z0-9_])' + m + r'(?![A-Za-z0-9_])', code)]
        info[mod_of[f]] = dict(file=f, imports=imps, zimports=z_imps, direct=found)
    trans = {}

    def spec(m, seen=()):
        if m in trans:
            return trans[m]
        if m not in info or m in seen:
            return None
        if info[m]['direct']:
            trans[m] = ('direct', info[m]['direct'])
            return trans[m]
        for i in info[m]['zimports']:
            r = spec(i, seen + (m,))
            if r:
                trans[m] = ('via', i)
                return trans[m]
        trans[m] = None
        return None
    for m in info:
        spec(m)
    L = ['b562 -- READING (5)(d): ZETA23`S FILES CLASSIFIED -- THE PRICE OF THE χ-EXPLICIT FORMULA, MODULE BY MODULE', '',
         '### THE RULE (the face`s READING (5)(d)): a module is ζ-SPECIFIC if its code (comments stripped) names a ζ object -- %s --'
         % ', '.join(ZMARKERS),
         '### or it imports, within Zeta23, a module that is; GENERIC otherwise (re-instantiable for L(s, χ) without ζ-specific input).',
         '### A mechanical scan; the one-clause reason is the scan`s own finding.', '',
         '    %-52s %-11s %s' % ('module', 'class', 'reason (one clause) | its Zeta23 imports')]
    rows = []
    for m in sorted(info):
        t = trans.get(m)
        if t is None:
            cls, why = 'GENERIC', 'names no ζ object and imports no ζ-specific module'
        elif t[0] == 'direct':
            cls, why = 'ζ-SPECIFIC', 'names %s' % ', '.join(t[1])
        else:
            cls, why = 'ζ-SPECIFIC', 'imports the ζ-specific %s' % t[1]
        rows.append(dict(module=m, file=info[m]['file'], cls=cls, why=why, direct=info[m]['direct'], zimports=info[m]['zimports']))
        L.append('    %-52s %-11s %s | %s' % (m, cls, why, ', '.join(info[m]['zimports']) or '(none)'))
    n_gen = sum(1 for r in rows if r['cls'] == 'GENERIC')
    n_dir = sum(1 for r in rows if r['direct'])
    L.append('')
    L.append('### ### **FILES %d ; ζ-SPECIFIC %d (naming a ζ object directly %d, by import only %d) ; GENERIC %d**'
             % (len(rows), len(rows) - n_gen, n_dir, len(rows) - n_gen - n_dir, n_gen))
    L.append('### the direct-mention count alone would call %d GENERIC; H14d is scored on the transitive rule (fewer than 29 generic).'
             % (len(rows) - n_dir))
    L.append('### ### **H14d (fewer than 29 of the 57 generic): %s**' % ('HOLDS' if n_gen < 29 else 'REFUTED'))
    L.append('### THE RULE`S LIMIT, READ BESIDE ITS COUNT: it is lexical. A GENERIC module can still carry ζ`s shape under a neutral')
    L.append('### name -- Zeta23.ExplicitFormula`s `literatureRHS` and `gammaBracket` are ζ`s explicit-formula right-hand side (the pole')
    L.append('### terms h(±i/2), the Γ bracket Re ψ(1/4 + ir/2) - log π) and name no ζ object; for L(s, χ) they are re-stated, not')
    L.append('### re-instantiated (the χ-side`s primeSum_chi, gammaBracket_chi, archTerm_chi in GRHWeil.lean are that re-statement).')
    L.append('### The count prices the files that must be rebuilt for χ by the rule`s words; it does not certify the rest reusable.')
    put_txt('b562_zeta23_modules.txt', L)
    put_json('b562_zeta23_modules.json', dict(rows=rows, files=len(rows), generic=n_gen, direct=n_dir, h14d=n_gen < 29))
    print(NL.join(L[-4:]))



# ------------------------------------------------------------------------------ READING (5)(a)-(c): the part banks
PARTS = {
    'a': ('THE STATEMENT LAYER -- GRH_chi, GRH_chi_trivial, h2_sign_chi and the χ-explicit formula`s terms',
          ['parity', 'IsTrivialPoint', 'GRH_chi', 'GRH_chi_trivial', 'primeSum_chi', 'gammaBracket_chi', 'archTerm_chi', 'h2_sign_chi'], 'grhA'),
    'b': ('THE SEAM -- a zero of LFunction χ with re <= 0 is a trivial point; the two forms of GRH_chi coincide',
          ['ne_one_of_ne_one', 'isPrimitive_inv', 'gammaFactor_ne_zero_of_re_pos', 'trivialPoint_of_gammaFactor_eq_zero',
           'LFunction_zero_re_nonpos', 're_nonpos_of_trivialPoint', 'GRH_chi_iff_trivial'], 'grhB'),
    'c': ('THE PAIRING ACROSS (χ, χ⁻¹) -- the zeros and their orders carried by conjugation',
          ['LFunction_conj_of_one_lt_re', 'LFunction_inv_conj', 'LFunction_zero_iff_conj', 'analyticOrderAt_LFunction_inv_conj'], 'grhC'),
}
SEAM_FACTS = ['LFunction_eq_completed_div_gammaFactor', 'completedLFunction_one_sub', 'LFunction_ne_zero_of_one_le_re',
              'Gammaℝ_ne_zero_of_re_pos', 'Gamma_eq_zero_iff', 'conductor_inv', 'level_one\'', 'isPrimitive_def']
PAIR_FACTS = ['LFunction_eq_LSeries', 'differentiable_LFunction', 'MulChar.star_apply\'', 'cpow_conj', 'tsum_star',
              'eqOn_of_preconnected_of_eventuallyEq', 'analyticOrderAt_conj_conj']


def part():
    X = sys.argv[2]
    title, names, tag = PARTS[X]
    src = rd(os.path.join(EF, MAIN_MOD)).replace(chr(13), '')
    att = sorted(f for f in os.listdir(SCR) if re.match(r'%s_\d+\.txt$' % tag, f))
    pr = rd(os.path.join(SCR, 'grh_prints.txt'))
    P0 = parse_prints(pr)
    L = ['b562 -- READING (5): PART (%s) -- %s' % (X, title), '',
         '### the branch %s from main %s ; the module %s (fed on stdin after LiWeil.lean)' % (BR, g(EF, 'rev-parse', '--short', BR + '~0').strip(), MAIN_MOD), '',
         '### THE ELABORATION ATTEMPTS OF THIS PART (the whole module as it then stood), each with its exit and error count:']
    for f in att:
        t = rd(os.path.join(SCR, f)).split(NL)
        L.append('    ' + t[0])
        for x in t[1:]:
            if 'error' in x or x.startswith('<stdin>') and 'warning' not in x:
                L.append('        | ' + x[:230])
    L.append('')
    L.append('### THE DECLARATIONS, AS THE SOURCE STATES THEM:')
    code_src = src
    for n in names:
        k = decl_at(code_src, n)
        if k is None:
            L.append('    ### %s NOT FOUND' % n)
            continue
        for i, l in enumerate(statement(code_src, k, 8)):
            L.append('    %5d | %s' % (k + i, l))
    L.append('')
    L.append('### LEAN`S PRINTS:')
    rows = {}
    for n in names:
        ax = P0.get(NSG + n)
        rows[n] = dict(axioms=ax, std3_or_fewer=ax is not None and set(ax) <= set(STD3))
        L.append('    %-40s %s' % (n, ax))
    if X == 'a':
        L.append('')
        L.append('### THE SALT-CHECK -- Lean`s #print of each statement-layer definition (every constant a Mathlib object or this module`s):')
        blk = pr[pr.index('def SIDEExplicitFormula.GRHWeil.GRH_chi :'):] if 'def SIDEExplicitFormula.GRHWeil.GRH_chi :' in pr else ''
        stop = blk.find('@SIDEExplicitFormula')
        L += ['    ' + x for x in blk[:stop].split(NL) if x.strip()]
        for d in ('def DirichletCharacter.LFunction', 'def DirichletCharacter.gammaFactor'):
            j = pr.find(d)
            if j >= 0:
                L += ['    ' + x for x in pr[j:].split(NL)[:2]]
        salt = ('DirichletCharacter.LFunction χ s = 0 → 0 < s.re → s.re < 1 → s.re = 1 / 2' in blk)
        L.append('### ### **GRH_chi UNFOLDS TO MATHLIB`S DirichletCharacter.LFunction, Complex.re AND EQUALITY ON ℝ: %s** (H14b)' % salt)
        rows['_salt'] = salt
    if X in ('b', 'c'):
        facts = SEAM_FACTS if X == 'b' else PAIR_FACTS
        body = NL.join(statement_block(src, decl_at(src, n)) for n in names if decl_at(src, n))
        L.append('')
        L.append('### THE FACTS THIS PART CONSUMES, BY NAME, FOUND IN ITS PROOFS: ' + ' ; '.join(
            '%s %s' % (f, 'yes' if f.split('.')[-1] in body else 'no') for f in facts))
        L.append('### rootNumber named in a proof of this part: %s' % ('rootNumber' in body))
        rows['_facts'] = {f: f.split('.')[-1] in body for f in facts}
        rows['_rootNumber'] = 'rootNumber' in body
    ok = all(v['std3_or_fewer'] for k, v in rows.items() if not k.startswith('_'))
    L.append('### ### **PRINTED %d OF %d ; THE STANDARD THREE OR FEWER, NO sorryAx : %s**' % (
        sum(1 for k, v in rows.items() if not k.startswith('_') and v['axioms'] is not None), len(names), ok))
    put_txt('b562_GRH_%s.txt' % X, L)
    put_json('b562_GRH_%s.json' % X, dict(part=X, names=names, rows=rows, all_std3=ok, attempts=len(att)))
    print('  written: b562_GRH_%s.txt ; %s' % (X, L[-1]))


G_GRADES = {
    'parity': 'DEF', 'IsTrivialPoint': 'DEF', 'GRH_chi': 'DEF', 'GRH_chi_trivial': 'DEF', 'primeSum_chi': 'DEF',
    'gammaBracket_chi': 'DEF', 'archTerm_chi': 'DEF', 'h2_sign_chi': 'DEF',
    'ne_one_of_ne_one': 'DERIVES', 'isPrimitive_inv': 'DERIVES', 'gammaFactor_ne_zero_of_re_pos': 'DERIVES',
    'trivialPoint_of_gammaFactor_eq_zero': 'DERIVES', 'LFunction_zero_re_nonpos': 'DERIVES', 're_nonpos_of_trivialPoint': 'DERIVES',
    'GRH_chi_iff_trivial': 'DERIVES', 'LFunction_conj_of_one_lt_re': 'DERIVES', 'LFunction_inv_conj': 'DERIVES',
    'LFunction_zero_iff_conj': 'DERIVES', 'analyticOrderAt_LFunction_inv_conj': 'DERIVES',
}


def e0():
    src = rd(os.path.join(EF, MAIN_MOD)).replace(chr(13), '')
    code = re.sub(r'/-.*?-/', '', src, flags=re.S)
    names = re.findall(r"^(?:theorem|def)\s+([A-Za-z_'0-9]+)", code, re.M)
    pr = rd(os.path.join(SCR, 'grh_prints.txt'))
    P0 = parse_prints(pr)
    L = ['b562 -- READING (6): THE E0 READ -- EVERY DECLARATION OF GRHWeil.lean GRADED, THE SALT-CHECK, THE ROWGEN RECORD', '']
    rows = {}
    for n in names:
        gr = G_GRADES.get(n, '### UNGRADED')
        ax = P0.get(NSG + n)
        rows[n] = dict(grade=gr, axioms=ax, std3_or_fewer=ax is not None and set(ax) <= set(STD3))
        L.append('    %-40s %-10s %s' % (n, 'DEFINITION' if gr == 'DEF' else gr, ax))
    ga = jl('b562_GRH_a.json')
    salt = bool(ga.get('rows', {}).get('_salt'))
    L.append('### the salt-check (part (a)): GRH_chi unfolds to Mathlib`s objects: %s ; no definition encodes a conclusion it is cited for;'
             ' h2_sign_chi is STATED and cited for nothing proved' % salt)
    tip = g(EF, 'rev-parse', 'HEAD').strip()
    recs, ctl = rowgen_record([NSG + n for n in ('LFunction_zero_re_nonpos', 'GRH_chi_iff_trivial', 'LFunction_inv_conj',
                                                  'analyticOrderAt_LFunction_inv_conj')], MAIN_MOD, tip, pr)
    L.append('')
    L.append('### THE ROWGEN RECORD (rowgen.py`s extract_doc_body and definition_encoded IMPORTED, at %s):' % tip[:7])
    for r in recs:
        L.append('    %-40s defenc %-5s %s | check %s' % (r['name'].split('.')[-1], r['defenc'], r['defenc_why'], bool(r['check'])))
    L.append('    control: definition_encoded on `def b560_ctl_stub : Prop := True` -> %s (must be True)' % (ctl,))
    thms = [r for r in rows.values() if r['grade'] != 'DEF']
    gate = (all(r['std3_or_fewer'] for r in rows.values()) and all(r['grade'] in ('DERIVES', 'DEF') for r in rows.values())
            and salt and ctl[0] and not any(r['defenc'] for r in recs))
    L.append('### ### **THE GATE: EVERY PRINT THE STANDARD THREE %s ; THE THEOREMS DERIVES (%d) ; THE SALT-CHECK %s => MERGE %s**'
             % (all(r['std3_or_fewer'] for r in rows.values()), len(thms), salt, gate))
    put_txt('b562_e0.txt', L)
    put_json('b562_e0.json', dict(rows=rows, gate=gate, salt=salt, rowgen=recs, rowgen_control=ctl[0], names=names, tip=tip))
    print(NL.join(L[-2:]))



# ------------------------------------------------------------------------------ the kernel state, the scores, the desk
PRE_HEADS = dict(Q.PRE_HEADS, **{'SIDE-explicit-formula': '2df46d7', 'SIDE-global-section': '347fac8'})
NEW_FILES = ['AxiomCheckGRHWeil.lean', 'SIDEExplicitFormula/GRHWeil.lean', 'SIDEExplicitFormula/LiWeil.lean']
DOC_COMMITS = ('3968ae7', '61e3551')
w_ = Q.w_


def mains():
    return {k: sorted(x for x in g(os.path.join(Q.DD, k), 'diff', '--name-only', h, 'main').split(NL) if x.strip()) for k, h in PRE_HEADS.items()}


def kstate():
    ls = {}
    for l in g(EF, 'ls-remote', 'origin').split(NL):
        if '\t' in l:
            h, r = l.split('\t')
            ls[r.strip()] = h.strip()
    ns = [x for x in g(EF, 'diff', '--name-status', V05, 'main').split(NL) if x.strip()]
    return dict(main=g(EF, 'rev-parse', 'main').strip(), remote=ls,
                v06=g(EF, 'rev-parse', 'v0.6^{}').strip(), v06obj=g(EF, 'rev-parse', 'v0.6').strip(),
                v06type=g(EF, 'cat-file', '-t', 'v0.6').strip(),
                br=g(EF, 'rev-parse', BR).strip(), held=g(EF, 'rev-parse', Q.HELD).strip(),
                liw561=g(EF, 'rev-parse', 'li-weil-b561').strip(),
                ns=sorted(x.replace('\t', ' ') for x in ns),
                ff=subprocess.run(['git', '-C', EF, 'merge-base', '--is-ancestor', V05, 'main']).returncode == 0,
                doc_diff=g(EF, 'diff', V05, DOC_COMMITS[1], '--', 'SIDEExplicitFormula/LiWeil.lean'),
                doc_files=[g(EF, 'show', '--name-only', '--pretty=format:', c).strip() for c in DOC_COMMITS])


def doc_only(diff):
    """### every changed line of the docstring commits lies inside a docstring: no line of code is added or removed."""
    ch = [l for l in diff.split(NL) if l[:1] in '+-' and not l.startswith(('+++', '---'))]
    code_like = [l for l in ch if re.match(r'^[+-]\s*(def|theorem|lemma|:=|by\b|exact|rw|fun|∀)', l)]
    return bool(ch) and not code_like, len(ch)


def scores():
    dj = jl('b562_drift.json')
    ga, gb, gc = (jl('b562_GRH_%s.json' % x) for x in 'abc')
    mj = jl('b562_zeta23_modules.json')
    k = kstate()
    needle = 'https://' + 'zenodo' + '.org'
    zen = [x for x in os.listdir(T) if x.startswith('b562_') and needle in rd(os.path.join(T, x))]
    dep = g(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2').strip() == ''
    trial = dict(head=g(Q.P.TRIAL, 'rev-parse', 'HEAD').strip(), status=g(Q.P.TRIAL, 'status', '--porcelain', '--untracked-files=no').strip())
    mm = {k2: [f for f in v if f.endswith('.lean')] for k2, v in mains().items()}
    other = {k2: v for k2, v in mm.items() if k2 != 'SIDE-explicit-formula'}
    held_ok = k['held'] == Q.HELD_TIP == k['remote'].get('refs/heads/' + Q.HELD) and k['liw561'] == k['remote'].get('refs/heads/li-weil-b561')
    donly, nch = doc_only(k['doc_diff'])
    sym = dj.get('within', {})
    b1 = bool(dj.get('shrink'))
    b2 = False   # ### D_sym scales as n² at every δ: a drift in n (the bench`s (iv)(b2) and the table (ii))
    b3 = all(dj.get('b3', {}).get(str(d)) for d in (0.1, 0.03, 0.01))
    s = dict(
        h13a=bool(dj.get('h13a_holds')),
        h13b=(b1 and b2 and b3),
        h14a=bool(gb.get('all_std3')) and gb.get('rows', {}).get('_rootNumber') is False,
        h14b=bool(ga.get('rows', {}).get('_salt')),
        h14c=bool(gc.get('all_std3')),
        h14d=bool(mj.get('h14d')),
        n1=bool(dj.get('h13a_holds')),
        n2=(b1 and b2 and b3),
        n3=(bool(gb.get('all_std3')) and bool(ga.get('rows', {}).get('_salt'))),
        n4=bool(gc.get('all_std3')),
        n5=bool(mj.get('h14d')),
        n6=(k['v06'] == k['main'] == k['remote'].get('refs/tags/v0.6^{}') and bool(ga.get('all_std3')) and bool(gb.get('all_std3'))),
        n7=(donly and k['ff'] and all(v == [] for v in other.values()) and zen == [] and dep and trial['head'].startswith('f22ff35')
            and trial['status'] == '' and held_ok),
        s1=gb.get('rows', {}).get('_rootNumber') is False and bool(gb.get('all_std3')),
        s2=bool(gc.get('all_std3')) and 'the search for a conjugation lemma for LFunction under Mathlib/NumberTheory' in rd(os.path.join(D, 'b562_reads.txt'))
            and ': 0 files []' in [l for l in rd(os.path.join(D, 'b562_reads.txt')).split(NL) if 'conjugation lemma for LFunction' in l][0],
        s3=all(abs(dj['D']['symmetric|%g' % d]['D'][n]) < abs(dj['D']['one-sided|%g' % d]['D'][n]) for d in (0.1, 0.03, 0.01) for n in range(1, 13)),
        _detail=dict(kernel=k, mains=mm, zen=zen, dep=dep, trial=trial, held_ok=held_ok, doc_only=donly, doc_changed=nch, b=(b1, b2, b3)))
    return s


def desk():
    s = scores()
    d0 = s['_detail']
    k = d0['kernel']
    dj = jl('b562_drift.json')
    mj = jl('b562_zeta23_modules.json')
    h = dj.get('h13a', {})
    lines = ['=' * 104, 'b562 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
             '### (R172)`S SIX, CLAUSE BY CLAUSE.', '-' * 104,
             '  **(H13a)** ### **%s.** -- the one-sided slopes %s against -(1/2) log(1/δ) %s: off by %s; the sign agrees at every δ; the'
             ' 10%% clause fails at all three (data/b562_drift.txt (iii)).' % (w_(s['h13a']), [round(h[x]['slope'], 3) for x in ('0.1', '0.03', '0.01')],
                                                                             [round(h[x]['pred'], 3) for x in ('0.1', '0.03', '0.01')],
                                                                             ['%.1f%%' % (100 * h[x]['rel']) for x in ('0.1', '0.03', '0.01')]),
             '  **(H13b)** ### **%s.** -- (b1) bounded, the bound shrinking: %s (max |D| %s); (b2) no drift in n: FALSE -- D scales as n² at every'
             ' δ (the bench`s table (ii)); (b3) within floor at every n: %s (|Z - λ_n| / floor 23.7, 6.59, 1.55 at δ = 0.1, 0.03, 0.01).'
             % (w_(s['h13b']), d0['b'][0], [round(dj['sym_max'][x], 4) for x in ('0.1', '0.03', '0.01')], d0['b'][2]),
             '  **(H14a)** ### **%s.** -- the seam compiled at attempt 3 from LFunction_eq_completed_div_gammaFactor, completedLFunction_one_sub'
             ' (at χ⁻¹), LFunction_ne_zero_of_one_le_re, Gammaℝ_ne_zero_of_re_pos; no root-number fact consumed (data/b562_GRH_b.txt).' % w_(s['h14a']),
             '  **(H14b)** ### **%s.** -- GRH_chi unfolds to DirichletCharacter.LFunction, Complex.re and equality on ℝ (data/b562_GRH_a.txt).' % w_(s['h14b']),
             '  **(H14c)** ### **%s.** -- via the Dirichlet series and the identity theorem: the rev holds no conjugation lemma for LFunction'
             ' (data/b562_reads.txt, the search: 0 files).' % w_(s['h14c']),
             '  **(H14d)** ### **%s.** -- %d of %d files GENERIC by the face`s rule (ζ-specific %d); the threshold was fewer than 29; the'
             ' rule`s lexical limit is printed beside the count (data/b562_zeta23_modules.txt).' % (w_(s['h14d']), mj['generic'], mj['files'], mj['files'] - mj['generic']), '',
             '### THE NAVIGATOR`S SEVEN.', '-' * 104,
             '  **(N1)** ### **%s.** -- H13a %s.' % (w_(s['n1']), w_(s['h13a'])),
             '  **(N2)** ### **%s.** -- H13b %s.' % (w_(s['n2']), w_(s['h13b'])),
             '  **(N3)** ### **%s.** -- H14a %s, H14b %s.' % (w_(s['n3']), w_(s['h14a']), w_(s['h14b'])),
             '  **(N4)** ### **%s.** -- H14c via THE SERIES (no Mathlib conjugation lemma at the rev).' % w_(s['n4']),
             '  **(N5)** ### **%s.** -- %d generic, not fewer than 29.' % (w_(s['n5']), mj['generic']),
             '  **(N6)** ### **%s.** -- v0.6 %s object %s peeled %s = main %s (remote %s), carrying the statement layer, the seam and the pairing;'
             ' the χ-explicit formula the HELD point.' % (w_(s['n6']), k['v06type'], k['v06obj'][:7], k['v06'][:7], k['main'][:7], k['remote'].get('refs/tags/v0.6^{}', '')[:7]),
             '  **(N7)** ### **%s.** -- the docstring commits change %d lines, all inside docstrings: %s ; main against v0.5 %s, a fast-forward %s ;'
             ' .lean files changed on the other mains %s ; HELD branches local = remote %s ; tools naming the platform %s ; deposit clean %s ; trial %s.'
             % (w_(s['n7']), d0['doc_changed'], d0['doc_only'], k['ns'], k['ff'], [x for x, v in d0['mains'].items() if v and x != 'SIDE-explicit-formula'] or 'NONE',
                d0['held_ok'], d0['zen'] or 'NONE', d0['dep'], d0['trial']), '',
             '### THE SEAT`S THREE.', '-' * 104,
             '  **(S1)** ### **%s.** -- no rootNumber in the seam`s proofs; the seam at the standard three.' % w_(s['s1']),
             '  **(S2)** ### **%s.** -- the pairing via the series; the search for a Mathlib conjugation lemma for LFunction: 0 files.' % w_(s['s2']),
             '  **(S3)** ### **%s.** -- |D_symmetric| < |D_one-sided| at every n and δ (the bench`s (v)).' % w_(s['s3']), '']
    nav = [s[x] for x in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7')]
    seat = [s[x] for x in ('s1', 's2', 's3')]
    lines.append('### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
                 % (nav.count(True), nav.count(False), nav.count(None), seat.count(True), seat.count(False)))
    lines.append('### ### **(R172) : H13a %s ; H13b %s ; H14a %s ; H14b %s ; H14c %s ; H14d %s.**'
                 % tuple(w_(s[x]) for x in ('h13a', 'h13b', 'h14a', 'h14b', 'h14c', 'h14d')))
    lines += ['', '### THIS ACT`S OWN DEFECTS.'] + rd(os.path.join(D, 'b562_defects.txt')).rstrip().split(NL)
    put_txt('b562_desk_notes.txt', lines)
    put_json('b562_scores.json', {k2: v for k2, v in s.items() if not k2.startswith('_')})
    print(NL.join(lines[:36]))


# ------------------------------------------------------------------------------ the ledger lines
SPECIES_H = ('## A species named for CP-7: three stated Props of the programme found false on reading, each at a convention on a '
             'boundary and each invisible to the print and the compile')
X2_H = ('*Appended 2026-09-29 by b562, under the author’s ruling `(R172)`(3), to the LI-WEIL-BRIDGE work-order (:3548; b561’s lines '
        'at :11542, :11544) -- (X2) FILED WITH ITS HYPOTHESES FIXED:*')
FH = ('## GRH-Weil, act one: the χ-side statement layer, the seam and the pairing across (χ, χ⁻¹); the drift read on the bench; '
      'LiLimitExchange marked -- held at the χ-explicit formula')
GRH_WO = ('*Appended 2026-09-29 by b562, under the author’s ruling `(R172)`(4), to the W-ORD-GRH-WEIL entry (:11373; the critical '
          'path’s row :11425) -- ACT ONE’S LINE AND THE LEADING ITEM:*')
HEADING = ('### b562 — lane two, act four under (R172): W-ORD-GRH-WEIL act one -- the χ-side statement layer, the seam and the pairing '
           'compiled (v0.6), held at the χ-explicit formula; LiLimitExchange marked; the drift read on the bench; (X2) filed')
ROW_SUP, ROW_ACT = '397', '398'


def species():
    guard_absent(FIND, SPECIES_H)
    t = ['', SPECIES_H, '',
         '*Filed at b562 on the author’s ruling `(R172)`(1)(b). A reading, descriptive voice; nothing is proved here.*', '',
         '**The three.** (i) lv’s h2, `mellin Phi (s/2) ≠ 0` at every s of the critical strip: false as stated, since the Mellin '
         'integral’s value there is the junk value of a divergent integral (`lv_h2_false_on_strip`, SIDE-explicit-formula '
         '`RegisterDepth.lean`:143; FINDINGS :4799, :5336) -- the convention is integrability at a half-plane’s edge. (ii) Register 1, '
         '`Register1_universalityHypothesis`: false as stated (`not_register1`, `RegisterDepth.lean`:60; FINDINGS :4794, :5571) -- the '
         'convention is totality at a register’s edge. (iii) `LiLimitExchange n` for n ≥ 1: false as stated on b561’s derivation (relay '
         '`data/b561_decay_read.txt` (7); FINDINGS :6072), the one-sided smoothing moving the jump’s midpoint into u < 0 -- the '
         'convention is the value at a jump. Its docstring and `li_identity_of_exchange`’s now say so on `main` (SIDE-explicit-formula '
         '`3968ae7`, `61e3551`, docstrings alone).', '',
         '**What they share.** Each is a Prop the programme wrote down, each elaborated, each printed the standard three or nothing, '
         'and each is false for a reason located at a boundary the statement’s words do not mention: where an integral stops '
         'converging, where a register’s quantifier runs out, where a function jumps. The print certifies the axioms a proof uses, '
         'and the compile certifies that a statement is well-typed; neither reads whether a stated hypothesis can hold. The three '
         'were found by reading -- two by proving their negations, one by a derivation on the page and a bench beside it (relay '
         '`data/b562_drift.txt`, where the one-sided drift is negative and grows in log(1/δ)).', '',
         '*Nothing deposits; nothing here is a statement about RH or any zero.*', '']
    o = append_to(FIND, NL.join(t))
    o['line'] = line_of(FIND, SPECIES_H)
    put_json('b562_species.json', o)
    print('  FINDINGS.md:%(line)d (%(added)d bytes, prefix %(prefix)s)' % o)


def x2():
    guard_absent(OT, X2_H)
    dj = jl('b562_drift.json')
    t = (NL + X2_H + ' the bridge’s next item as ruled is the SYMMETRIC family -- `LiLimitExchange` restated over truncations mollified '
         'evenly about the jump (f(u) + f(−u) = 1, f(0) = 1/2), the limit taken from both sides. **H12a’**: the paired truncated '
         'transform’s excess over the jump’s is odd about the jump at leading order, so the uniform bound returns to order n/‖ρ‖² '
         'and (D3) is a pairing estimate on existing lemmas. **H12b** and **H12c** as `(R171)` wrote them, transferred. **The (X1) '
         'fallback** (the midpoint-normalised jump) replaces (X2) as the next item if H13b is refuted. **H13b at b562’s bench: '
         'REFUTED** (relay `data/b562_drift.txt` (iv)): the symmetric drift shrinks with δ (max |D| %.4f, %.4f, %.4f at δ = 0.1, 0.03, '
         '0.01) but scales as n² at each δ and stands beyond the tail floor at every n. By `(R172)`(3) and (7) the next item is '
         '(X1).' % (dj['sym_max']['0.1'], dj['sym_max']['0.03'], dj['sym_max']['0.01']) + NL)
    o = append_to(OT, t)
    o['line'] = line_of(OT, X2_H)
    put_json('b562_x2.json', o)
    print('  OPEN_TRAILS.md:%(line)d (%(added)d bytes, prefix %(prefix)s)' % o)


def rows():
    k = kstate()
    ej = jl('b562_e0.json')
    sup = [ROW_SUP,
           '**li_identity_of_exchange’S GRADE UNDER THE SUPERSESSION RULE** (b562, under (R172)(1)(a)): its premise `LiLimitExchange n` '
           'is false as stated for n ≥ 1 on b561’s reading (relay data/b561_decay_read.txt (7)), so the conditional certifies '
           'nothing; this row’s grade cell replaces row 395’s for this terminal alone; row 395 stands unedited above.',
           '`SIDE-explicit-formula/SIDEExplicitFormula/LiWeil.lean` -- `SIDEExplicitFormula.LiWeil.li_identity_of_exchange` (its '
           'docstring marked at `61e3551`)',
           '[propext, Classical.choice, Quot.sound] (relay data/b560_e0.txt; unchanged at v0.6, data/b562_doc_push.txt)',
           'SUPERSEDES row 395: T2 -- `li_identity_of_exchange` (in the table`s grade vocabulary SHELL: a conditional on a premise '
           'false as stated certifies nothing)',
           'Written 2026-09-29 (b562) through `relay/tools/corr_row.py`; the rule is `supersede` in `relay/tools/terminal_table.py`.']
    r = subprocess.run([sys.executable, os.path.join(T, 'corr_row.py'), CORR] + sup, capture_output=True, text=True, encoding='utf-8')
    print(r.stdout[-300:], r.stderr[-300:])
    names = ['LFunction_zero_re_nonpos', 'GRH_chi_iff_trivial', 'LFunction_inv_conj', 'analyticOrderAt_LFunction_inv_conj']
    act = [ROW_ACT,
           '**GRH-WEIL, ACT ONE: THE χ-SIDE STATEMENT LAYER, THE SEAM AND THE PAIRING** (b562, under (R172)(4)). SIDE-explicit-formula '
           'v0.6 = %s (GRHWeil.lean), for χ a primitive Dirichlet character mod N, χ ≠ 1, over Mathlib’s DirichletCharacter.LFunction: '
           'GRH_chi and its form off the trivial points coincide (a zero with re ≤ 0 is a trivial point, from the functional '
           'equation at χ⁻¹ and the Γ factor, no root-number fact); the zeros and their orders are carried to χ⁻¹ by conjugation. '
           'h2_sign_chi is stated and its equivalence to GRH_chi not proved: the χ-explicit formula is the held point. Nothing here '
           'proves GRH.' % k['v06'][:7],
           '`SIDE-explicit-formula/SIDEExplicitFormula/GRHWeil.lean` (v0.6) : ' + ', '.join('`%s%s`' % (NSG, n) for n in names),
           '%d of %d declarations: [propext, Classical.choice, Quot.sound], no sorryAx (relay data/b562_e0.txt)'
           % (sum(1 for r2 in ej['rows'].values() if r2['std3_or_fewer']), len(ej['rows'])),
           ' ; '.join('`%s` %s' % (n, ej['rows'][n]['grade']) for n in names),
           'LANDED on main by fast-forward, v0.6 pushed after main read back (tools/push_gated.sh); held at the χ-explicit formula; '
           'h2 where the deposit left it; nothing deposits; nothing at Zenodo written.']
    r2 = subprocess.run([sys.executable, os.path.join(T, 'corr_row.py'), CORR] + act, capture_output=True, text=True, encoding='utf-8')
    print(r2.stdout[-300:], r2.stderr[-300:])
    put_json('b562_rows.json', dict(sup=sup, act=act, exit_sup=r.returncode, exit_act=r2.returncode))


def rowgen_diff():
    sys.path.insert(0, os.path.join(T, 'rowgen'))
    import rowgen as RG
    recs = jl('b562_e0.json').get('rowgen', [])
    for r in recs:
        r['exists'] = bool(r.get('check'))
        r['axioms'] = "'%s' depends on axioms: [%s]" % (r['name'], ', '.join(r['axioms'] or [])) if isinstance(r.get('axioms'), list) else (r.get('axioms') or '')
    rowtxt = [l for l in rd(CORR).split(NL) if l.startswith('| %s |' % ROW_ACT)]
    out = RG.diff(recs, NL.join(rowtxt))
    L = ['b562 -- READING (6): THE ROWGEN DIFF (rowgen.diff IMPORTED) OF THE MERGED RECORDS AGAINST CORRESPONDENCE ROW %s' % ROW_ACT, '',
         '### records: %d ; row found: %s' % (len(recs), bool(rowtxt))] + ['    ' + str(x) for x in out]
    put_txt('b562_rowgen.txt', L)
    print(NL.join(L))


def findings():
    guard_absent(FIND, FH)
    s = jl('b562_scores.json')
    k = kstate()
    dj, mj = jl('b562_drift.json'), jl('b562_zeta23_modules.json')
    h = dj['h13a']
    t = ['', FH, '',
         '*Filed at b562 on the author’s ruling `(R172)`. Lane two, act four. Banks: relay `data/b562_GRH_a.txt` … `_c.txt`, '
         '`data/b562_zeta23_modules.txt`, `data/b562_drift.txt`, `data/b562_e0.txt`, `data/b562_doc_push.txt`, `data/b562_v06_push.txt`; '
         'SIDE-explicit-formula v0.6 = `%s`. Nothing about the zeros of ζ or of any L-function is claimed beyond the compiled '
         'statements’ own words; a measurement is labelled as one.*' % k['v06'][:7], '',
         '**What is compiled, 19 of 19 at the standard three.** For χ a primitive Dirichlet character mod N, χ ≠ 1, over Mathlib’s '
         '`DirichletCharacter.LFunction`: the statement layer -- `GRH_chi` (every zero in the open strip has re = 1/2, unfolding to '
         'Mathlib’s objects), `GRH_chi_trivial`, and `h2_sign_chi` stated in H2Sign’s form with the χ-explicit formula’s prime and Γ '
         'terms; the seam -- `LFunction_zero_re_nonpos` (a zero with re ≤ 0 is a trivial point −(2m + a)) and `GRH_chi_iff_trivial`, '
         'from the relation between L and its completion, the functional equation applied to χ⁻¹ (primitive by `conductor_inv`), '
         'the nonvanishing on re ≥ 1 and Gammaℝ’s nonvanishing on re > 0, with no root-number fact (the rev carries none for a '
         'composite modulus); the pairing -- `LFunction_inv_conj` (L(χ⁻¹, s̄) = conj L(χ, s)) by the Dirichlet series and the '
         'identity theorem, the rev holding no conjugation lemma for L, and the orders carried by Zeta23’s `analyticOrderAt_conj_conj`.', '',
         '**Where it stops.** The χ-explicit formula: `h2_sign_chi χ ↔ GRH_chi χ` is stated as the target and not proved. Its price, '
         'by the face’s rule over Zeta23’s 57 files: %d ζ-specific (naming ζ’s objects), %d generic; H14d (fewer than 29 generic) is '
         'REFUTED, and the rule is lexical -- `literatureRHS` and `gammaBracket` carry ζ’s shape under neutral names and are '
         're-stated for χ, not re-instantiated.' % (mj['files'] - mj['generic'], mj['generic']), '',
         '**The drift on the bench, a measurement.** Over the chain bank’s 10,000 ordinates, the one-sided family’s drift is linear in '
         'n with slopes %.3f, %.3f, %.3f at δ = 0.1, 0.03, 0.01 against −(1/2) log(1/δ) = %.3f, %.3f, %.3f: the sign agrees, the difference '
         'narrows as δ falls, and the 10%% clause fails at all three -- H13a REFUTED. The symmetric family’s drift shrinks with δ '
         '(max %.4f, %.4f, %.4f) and is smaller than the one-sided at every n and δ, but scales as n² at each δ and stands beyond '
         'the tail floor at every n -- H13b REFUTED. The paired Li sum over the bank plus the n²-tail reproduces BALPOS’s λ_n to '
         '3·10⁻⁹ … 3·10⁻⁷.' % (h['0.1']['slope'], h['0.03']['slope'], h['0.01']['slope'], h['0.1']['pred'], h['0.03']['pred'],
                                h['0.01']['pred'], dj['sym_max']['0.1'], dj['sym_max']['0.03'], dj['sym_max']['0.01']), '',
         '**LiLimitExchange marked.** Its docstring and `li_identity_of_exchange`’s now carry the false-as-stated line (two commits, '
         'docstrings alone, every print unchanged); row 397 supersedes row 395’s grade for `li_identity_of_exchange` (T2); the '
         'species entry names the three such Props.', '',
         '**The scores.** H13a %s; H13b %s; H14a %s; H14b %s; H14c %s; H14d %s. (N1) %s, (N2) %s, (N3) %s, (N4) %s, (N5) %s, (N6) %s, '
         '(N7) %s.' % tuple(w_(s.get(x)) for x in ('h13a', 'h13b', 'h14a', 'h14b', 'h14c', 'h14d', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7')), '',
         '**Next** (`(R172)`(7)): H13b is refuted, so the bridge’s (X1) act -- the explicit formula at the midpoint-normalised jump -- '
         'and then GRH-WEIL’s second act.', '',
         '*Nothing deposits; nothing at Zenodo written; no `sorry` on any `main`; nothing here is a statement about RH, GRH or any zero '
         'beyond the compiled statements’ own words.*', '']
    o = append_to(FIND, NL.join(t))
    o['heading_line'] = line_of(FIND, FH)
    put_json('b562_findings.json', o)
    print('  FINDINGS.md:%(heading_line)d (%(added)d bytes appended, prefix kept %(prefix)s)' % o)


def workorders():
    guard_absent(OT, GRH_WO)
    k = kstate()
    mj = jl('b562_zeta23_modules.json')
    t = (NL + GRH_WO + ' at SIDE-explicit-formula v0.6 = `%s` (`GRHWeil.lean`): **the statement layer, the seam and the pairing '
         'COMPILED** (19 declarations, the standard three); **the χ-explicit formula NOT BUILT -- the held point**. **THE LEADING '
         'ITEM, the module count** (relay `data/b562_zeta23_modules.txt`): of Zeta23’s %d files, %d are ζ-specific by the face’s rule '
         '(they name ζ’s objects: the seam, the local count, the contour, the full-line assembly, the zero-sum limit and summability, '
         'the log-derivative, the growth and Landau bounds) and must be rebuilt for L(s, χ); %d are generic (the abstract zero '
         'configuration, the Poisson transform, the Gamma facts, the linear algebra, the tail, the PNT+ import) -- with the rule’s '
         'lexical limit that `literatureRHS` carries ζ’s shape and is re-stated for χ. H14d REFUTED (%d ≥ 29). The critical path’s '
         'price at :11425 (31 items, 6 new and 25 re-instantiated) stands beside this count.' % (k['v06'][:7], mj['files'],
                                                                                               mj['files'] - mj['generic'], mj['generic'], mj['generic']) + NL)
    o = append_to(OT, t)
    o['line'] = line_of(OT, GRH_WO)
    put_json('b562_workorders.json', o)
    print('  OPEN_TRAILS.md:%(line)d (%(added)d bytes, prefix %(prefix)s)' % o)


def components():
    L = ['=' * 132, 'b562 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '']
    for n in ('b562_reads.txt', 'b562_doc_push.txt', 'b562_drift.txt', 'b562_GRH_a.txt', 'b562_GRH_b.txt', 'b562_GRH_c.txt',
              'b562_zeta23_modules.txt', 'b562_e0.txt', 'b562_v06_push.txt', 'b562_rowgen.txt', 'b562_branches.txt'):
        L.append('### relay data/%s' % n)
        L.extend('  ' + x for x in rd(os.path.join(D, n)).rstrip().split(NL))
        L.append('')
    for n, key in (('b562_species.json', 'line'), ('b562_x2.json', 'line'), ('b562_findings.json', 'heading_line'),
                   ('b562_rows.json', 'exit_act'), ('b562_workorders.json', 'line')):
        L.append('### relay data/%s -- %s %s' % (n, key, jl(n).get(key)))
    put_txt('b562_components.txt', L)
    print('  written: b562_components.txt (%d lines)' % len(L))


def trail():
    guard_absent(OT, HEADING)
    s = jl('b562_scores.json')
    sp, x2j, f, wo = jl('b562_species.json'), jl('b562_x2.json'), jl('b562_findings.json'), jl('b562_workorders.json')
    k = kstate()
    t = ['', HEADING, '',
         '**(R172) ratified.** (1) b561 at its weight: LiLimitExchange marked false as stated on main by docstring, the grade '
         'superseded, the species named. (2) The drift put to the bench. (3) (X2) filed with its hypotheses. (4) GRH-WEIL act one. '
         '(5) The hypotheses. (6) Housekeeping. (7) The next act by H13b. The branch was cut from `main` after the docstring commits, '
         'not from v0.5, on the author’s b560 ruling of the same shape (declared on the face).', '',
         '**Entered:** FINDINGS.md:%s (the species entry), :%s (the entry); OPEN_TRAILS.md:%s ((X2) filed), :%s (GRH-WEIL act one’s '
         'line and the leading item); SIDE-global-section CORRESPONDENCE.md rows %s (the supersession) and %s; SIDE-explicit-formula '
         'docstring commits `3968ae7`, `61e3551` and v0.6 = `%s`, the branch `grh-weil-b562` pushed by name.'
         % (sp.get('line'), f.get('heading_line'), x2j.get('line'), wo.get('line'), ROW_SUP, ROW_ACT, k['v06'][:7]), '',
         '**H13a %s · H13b %s · H14a %s · H14b %s · H14c %s · H14d %s.** The stop: the χ-explicit formula (h2_sign_chi ↔ GRH_chi stated, '
         'not proved), priced by the module count.' % tuple(w_(s.get(x)) for x in ('h13a', 'h13b', 'h14a', 'h14b', 'h14c', 'h14d')), '',
         '**Housekeeping:** the remote lists no li-weil-b560 -- its deletion recorded as done at b561, by inference from the listing, '
         'not as this act’s; defect (e) of b561 stands as transient with its two records.', '',
         '**The table:** regenerated at this act, its line for `li_identity_of_exchange` reads **CONFLICT** (INTERFACES / SHELL), not SHELL: row 397 removes row 395’s cell, but b560’s entry at FINDINGS.md:6048 grades the terminal INTERFACES, and the supersession form reaches CORRESPONDENCE rows alone (`supersede`, relay `tools/terminal_table.py`:153). The tool is unedited, and the conflict is left for the author (relay `data/b562_defects.txt` (f)).', '',
         '**Next:** the bridge’s (X1) act (H13b refuted, `(R172)`(7)); then GRH-WEIL’s second act.', '',
         '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s · (N6) %s · (N7) %s.** The seat’s own: (S1) %s, (S2) %s, (S3) %s.'
         % tuple(w_(s.get(x)) for x in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 's1', 's2', 's3')),
         '**Two docstring commits and one fast-forward onto `main`, one tag pushed after main read back, no `sorry` on any `main`.** '
         'Nothing deposits; nothing at Zenodo written; no existing statement changed; no Zeta23 file edited; no monograph byte '
         'changed; no keystone body edited; ERRATA untouched; the ceiling unchanged; row U1 unedited; `h2` where the deposit left it; '
         'the four lists stay OPEN; nothing here is a statement about RH or any zero beyond the compiled statements’ own words.', '']
    o = append_to(OT, NL.join(t))
    o['line'] = line_of(OT, HEADING)
    put_json('b562_trail.json', o)
    print('  OPEN_TRAILS.md:%(line)d (%(added)d bytes appended, prefix kept %(prefix)s)' % o)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        sys.exit('usage: b562_record.py <component>')
    fn()
