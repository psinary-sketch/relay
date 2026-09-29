# -*- coding: utf-8 -*-
"""b564_record.py -- LANE TWO, ACT SIX: GRH-WEIL ACT TWO -- THE χ-INSTANCE OF THE CONFIGURATION, THE GENERIC MODULES
CONSUMED, THE FRONTIER ATTEMPTED; THE CEILING SENTENCE; THE CONFLICT CLEARED; PRIOR ART; THE CONVERSE RE-PRICED, UNDER (R174).
### `python tools/b564_record.py reads | trailsup <before|after> | ceiling | priorart | converse | dag | part <name> |
### e0 | findings | rows | workorder | trail | components | desk`. b563's helpers are IMPORTED, never copied. This file
### deletes nothing.
"""
import io, json, os, re, subprocess, sys, hashlib
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
import b563_record as Z3  # noqa: E402
Q = Z3.Q
P = Q.P
PP, FIND, OT, CORR, EF = Q.PP, Q.FIND, Q.OT, Q.CORR, Q.EF
NL = chr(10)
rd, g, append_to, guard_absent, poss, line_of = Q.rd, Q.g, Q.append_to, Q.guard_absent, Q.poss, Q.line_of
at, decl_at, statement, statement_block = Q.at, Q.decl_at, Q.statement, Q.statement_block
parse_prints, rowgen_record, STD3 = Z3.parse_prints, Q.rowgen_record, Q.STD3
put_txt, put_json, jl, w_ = Q.put_txt, Q.put_json, Q.jl, Q.w_
PRIOR_RELAY = 'f0e92155'   # ### b563's table housekeeping -- relay's tip before this act
PRIOR_PP = '0a0f958'
PRIOR_GS = '6fbd70e'
V07 = '1e4a00792008'
BR = 'grh-weil-b564'
README, REGISTRY = os.path.join(PP, 'README.md'), os.path.join(PP, 'REGISTRY.md')
ML = os.path.join(EF, '.lake', 'packages', 'mathlib')
MLREV = '51e6992efd06126df61a496bebf8f49482a4e129'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def _decl_lines(L, text, fname, names, rev, cap=10):
    for n in names:
        k = decl_at(text, n)
        if k is None:
            L.append('### %s: %s NOT FOUND' % (fname, n))
            continue
        L.append('### %s:%d @%s -- %s' % (fname, k, rev, n))
        L += ['    %5d | %s' % (k + i, l) for i, l in enumerate(statement(text, k, cap))]


def _lines(L, path, a, b, label):
    ls = rd(path).split(NL)
    L.append('### %s :%d-:%d' % (label, a, b))
    L += ['    %5d | %s' % (i, ls[i - 1][:400]) for i in range(a, b + 1) if ls[i - 1].strip()]


def reads():
    L = ['b564 -- READING (1): THE READS, PRINTED BY PATH AND LINE',
         '### SIDE-explicit-formula v0.7 = %s ; main at step zero %s ; Mathlib rev %s' % (
             g(EF, 'rev-parse', 'v0.7^{}').strip()[:7], g(EF, 'rev-parse', 'main').strip()[:7],
             g(ML, 'rev-parse', 'HEAD').strip()[:8]), '']
    v = V07[:7]
    for f in ['LiWeil', 'LiWeilSym', 'GRHWeil']:
        t = at(V07, 'SIDEExplicitFormula/%s.lean' % f).split(NL)
        L.append('### %s.lean @%s -- the header`s first line and the imports' % (f, v))
        L += ['    %5d | %s' % (i + 1, t[i]) for i in range(len(t)) if t[i].startswith('import') or (i < 4 and t[i].startswith('SIDE-'))]
    gw = at(V07, 'SIDEExplicitFormula/GRHWeil.lean')
    _decl_lines(L, gw, 'GRHWeil.lean', ['isPrimitive_inv', 'gammaFactor_ne_zero_of_re_pos', 'LFunction_zero_re_nonpos',
                                        'LFunction_inv_conj', 'LFunction_zero_iff_conj', 'analyticOrderAt_LFunction_inv_conj'], v, 6)
    df = at(V07, 'Zeta23/Defs.lean')
    _decl_lines(L, df, 'Zeta23/Defs.lean', ['ZeroConfig', 'reflect', 'gammaOf'], v, 16)
    st = at(V07, 'Zeta23/Statement.lean')
    _decl_lines(L, st, 'Zeta23/Statement.lean', ['IsNontrivialZero', 'zeroMult', 'ZetaSeam', 'zetaZeros'], v, 12)
    sc = at(V07, 'Zeta23/Statement/SeamClosed.lean')
    _decl_lines(L, sc, 'Zeta23/Statement/SeamClosed.lean', ['zetaSeam', 'zetaZeroConfig'], v, 3)
    zr = at(V07, 'Zeta23/ZetaReflect.lean')
    _decl_lines(L, zr, 'Zeta23/ZetaReflect.lean', ['analyticOrderAt_conj_conj', 'analyticOrderAt_zeta_one_sub',
                                                   'zeta_reflect_zero', 'zeta_mult_reflect'], v, 3)
    mn = at(V07, 'Zeta23/WeilEF/Main.lean')
    _decl_lines(L, mn, 'Zeta23/WeilEF/Main.lean', ['EF_lit_zetaZeroConfig'], v, 6)
    mb = os.path.join(D, 'b562_zeta23_modules.txt')
    L.append('### relay data/b562_zeta23_modules.txt sha256 %s (%d lines)' % (sha(mb), len(rd(mb).split(NL))))
    dc = rd(os.path.join(ML, 'Mathlib', 'NumberTheory', 'LSeries', 'DirichletContinuation.lean'))
    _decl_lines(L, dc, 'Mathlib/NumberTheory/LSeries/DirichletContinuation.lean @%s' % MLREV[:8],
                ['LFunction', 'differentiable_LFunction', 'gammaFactor', 'differentiable_completedLFunction',
                 'LFunction_eq_completed_div_gammaFactor', 'rootNumber'], 'ml', 4)
    k = [i + 1 for i, l in enumerate(dc.split(NL)) if l.startswith('theorem completedLFunction_one_sub')]
    for n in k:
        L.append('### DirichletContinuation.lean:%d -- IsPrimitive.completedLFunction_one_sub' % n)
        L += ['    %5d | %s' % (n + i, l) for i, l in enumerate(dc.split(NL)[n - 1:n + 1])]
    nv = rd(os.path.join(ML, 'Mathlib', 'NumberTheory', 'LSeries', 'Nonvanishing.lean'))
    _decl_lines(L, nv, 'Mathlib/NumberTheory/LSeries/Nonvanishing.lean @%s' % MLREV[:8], ['LFunction_ne_zero_of_one_le_re'], 'ml', 3)
    L.append('')
    _lines(L, FIND, 4729, 4750, 'FINDINGS.md (b536`s prior-art entry, its form and its search list)')
    for n in (5575, 5601, 6064):
        _lines(L, FIND, n, n, 'FINDINGS.md (the field entry`s lineage)')
    _lines(L, OT, 11577, 11577, 'OPEN_TRAILS.md (b562`s trail line)')
    for n in (11523, 11542, 11544, 11565, 11590):
        _lines(L, OT, n, n, 'OPEN_TRAILS.md')
    cr = [l for l in rd(CORR).split(NL) if l.startswith('| 397 ')]
    L.append('### CORRESPONDENCE row 397 : ' + (cr[0][:600] if cr else 'NOT FOUND'))
    _lines(L, README, 115, 115, 'README.md (the ceiling of (R146)(2))')
    _lines(L, REGISTRY, 950, 950, 'REGISTRY.md (the ceiling of (R146)(2))')
    put_txt('b564_reads.txt', L)
    print(NL.join(L[:6]))
    print('  lines %d ; written: b564_reads.txt' % len(L))


TERM = 'li_identity_of_exchange'


def author_sentence():
    """### (R174)(1)`s sentence, READ from the banked ferry between its quotation marks and whitespace-joined -- not retyped."""
    f = ' '.join(rd(os.path.join(D, 'b564_ferry.txt')).split())
    m = re.search(r'the sentence, the author.s: "([^"]+)"', f)
    return m.group(1) if m else None


def ceiling_para():
    s = author_sentence()
    if not s:
        sys.exit('### THE AUTHOR`S SENTENCE WAS NOT FOUND IN THE BANKED FERRY')
    return ("*(Appended under the author's ruling `(R174)`(1), 2026-09-29, b564, beside the `(R146)`(2) sentence above, "
            "which stays: b563 entered at its weight, SIDE-explicit-formula v0.7 = `1e4a007`.)* Supportable, the author's "
            "sentence: *" + s + "* Not supportable, unchanged: *RH proved*; *h2_sign proved*; *Li's criterion compiled* "
            "without the half named.")


def _insert_after(path, n, para):
    """### insert `para` as its own paragraph after line n; every byte of lines 1..n is kept and read back."""
    import banned_terms as BT
    para = poss(para)
    if [m.group(0) for m in BT.PAT.finditer(para)]:
        sys.exit('### A BANNED STEM IN THE INSERT TO %s' % path)
    if para.count('`') % 2:
        sys.exit('### UNBALANCED BACKTICKS IN THE INSERT TO %s' % path)
    raw = open(path, 'rb').read()
    if b'\r' in raw:
        sys.exit('### CR BYTES IN %s: REFUSING' % path)
    ls = raw.split(b'\n')
    head = b'\n'.join(ls[:n]) + b'\n'
    tail = b'\n'.join(ls[n:])
    new = head + b'\n' + para.encode('utf-8') + b'\n' + tail
    open(path, 'wb').write(new)
    after = open(path, 'rb').read()
    return dict(file=os.path.relpath(path, PP).replace(os.sep, '/'), after_line=n, before=len(raw), added=len(after) - len(raw),
                head_kept=after.startswith(head), tail_kept=after.endswith(tail), new_line=n + 2)


def ceiling():
    para = ceiling_para()
    out = {}
    for path, n in ((README, 115), (REGISTRY, 950)):
        l0 = rd(path).split(NL)[n - 1]
        if '(R146)' not in l0:
            sys.exit('### %s :%d IS NOT THE (R146)(2) LINE' % (os.path.basename(path), n))
        guard_absent(path, para[:90])
        out[os.path.basename(path)] = _insert_after(path, n, para) if n < len(rd(path).rstrip(NL).split(NL)) else \
            dict(append_to(path, NL + para + NL), after_line=n, new_line=n + 2)
    L = ['b564 -- COMPONENT 1 (i): THE CEILING SENTENCE, APPENDED BESIDE (R146)(2)`S LINE, IN b536`S FORM', '',
         '### the author`s sentence, read from the banked ferry: ' + author_sentence(), '### the paragraph: ' + para, '']
    for k, v in out.items():
        L.append('### %s : %s' % (k, json.dumps(v)))
        L.append('    the line now at :%d : %s' % (v['new_line'], rd(os.path.join(PP, k)).split(NL)[v['new_line'] - 1][:200]))
    put_txt('b564_ceiling.txt', L)
    put_json('b564_ceiling.json', dict(sentence=author_sentence(), para=para, files=out))
    print(NL.join(L))


def _table_rows(j):
    rows = j['rows'] if isinstance(j, dict) else j
    return {(r['repo'], r['name']): r for r in rows}


def trailsup(stage):
    """### the table regenerated by `tools/terminal_table.py`, unedited; compared with the committed table (relay HEAD)."""
    before = _table_rows(json.loads(subprocess.run(['git', '-C', ROOT, 'show', 'HEAD:data/terminal_table.json'],
                                                   capture_output=True).stdout.decode('utf-8')))
    r = subprocess.run([sys.executable, os.path.join(T, 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8', errors='replace')
    after = _table_rows(json.loads(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8').read()))
    run = io.open(os.path.join(D, 'terminal_table_run.txt'), encoding='utf-8').read()
    cb = sorted('%s|%s' % k for k, v in before.items() if v['grade'] == 'CONFLICT')
    ca = sorted('%s|%s' % k for k, v in after.items() if v['grade'] == 'CONFLICT')
    changed = sorted('%s|%s %s -> %s' % (k[0], k[1], before[k]['grade'], after[k]['grade']) for k in before
                     if k in after and before[k]['grade'] != after[k]['grade'])
    L = ['b564 -- COMPONENT 1 (%s): THE TABLE REGENERATED %s THE TRAIL-LINE SUPERSESSION' % (stage, stage.upper()), '',
         '### regenerated: exit %d ; rows %d (committed %d) ; rows gone %s ; rows added %s' % (
             r.returncode, len(after), len(before), sorted('%s|%s' % k for k in before if k not in after) or 'NONE',
             sorted('%s|%s' % k for k in after if k not in before) or 'NONE'),
         '### the run`s header: ' + (' | '.join(l.strip() for l in run.split(NL) if 'SUPERSESSIONS READ' in l) or '### ABSENT'),
         '### ### **CONFLICT committed %d -> regenerated %d**' % (len(cb), len(ca)),
         '### CONFLICT committed (%d):' % len(cb)] + ['    ' + x for x in cb] + \
        ['### CONFLICT regenerated (%d):' % len(ca)] + ['    ' + x for x in ca] + \
        ['### ### **TERMINALS WHOSE GRADE CHANGED : %s**' % (changed or 'NONE')]
    term = {}
    for lab, tab in (('committed', before), ('regenerated', after)):
        term[lab] = []
        for k, v in tab.items():
            if k[1].endswith(TERM):
                L.append('### %s -- %s|%s grade %s' % (lab, k[0], k[1], v['grade']))
                L += ['    cell %-22s %s:%s' % (c['grade'], c['ledger'], c['line']) for c in v['grade_cells']]
                term[lab] += [dict(grade=c['grade'], ledger=c['ledger'], line=c['line']) for c in v['grade_cells']]
                term[lab + '_grade'] = v['grade']
    put_txt('b564_trailsup_%s.txt' % stage, L)
    put_json('b564_trailsup_%s.json' % stage, dict(rc=r.returncode, rows=len(after), conflict_committed=cb, conflict_regenerated=ca,
                                                  changed=changed, term=term))
    print(NL.join(L))


SUPLINE = ('SUPERSEDES OPEN_TRAILS :11577 for li_identity_of_exchange: T2-INTERFACES-on-false-premise -- appended 2026-09-29 '
           'by b564 under the author’s ruling (R174)(2), the trail-line form of b554 as relay tools/terminal_table.py reads it; '
           'the source: CORRESPONDENCE row 397 of SIDE-global-section (b562) and relay data/b561_decay_read.txt (7), the premise '
           'false as stated for n ≥ 1; OPEN_TRAILS :11577 stands unedited above; no identifier on this line is in backticks.')


def supline():
    import terminal_table as TT
    m = TT.TRAIL_SUP_RE.search(SUPLINE)
    print('### TRAIL_SUP_RE (tools/terminal_table.py :166): %s' % TT.TRAIL_SUP_RE.pattern)
    print('### the line`s match: %s' % (str(m.groups()) if m else '### NO MATCH -- REFUSING'))
    if not m or m.groups() != ('11577', TERM):
        sys.exit(2)
    if TT.NAME_RE.search(SUPLINE):
        sys.exit('### A BACKTICKED NAME ON THE LINE -- REFUSING')
    guard_absent(OT, SUPLINE[:60])
    res = append_to(OT, NL + SUPLINE + NL)
    n = line_of(OT, SUPLINE[:60])
    print('### appended at OPEN_TRAILS :%s ; %s' % (n, json.dumps(res)))
    put_json('b564_supline.json', dict(line=n, text=SUPLINE, res=res, regex=TT.TRAIL_SUP_RE.pattern, match=list(m.groups())))


BULKA = 'https://github.com/nicholasbulka/li-criterion-rh-equivalence-lean'
BULKA_SHA = '35df682f3b709ffe5fbcfdd452dfa964bd622b87'
ARDA = 'https://github.com/DrMurphyIsIn/Arda'
ARDA_SHA = 'acfb0ee57108a185c484409cd91ac5621ce2d13e'

COMPARE = (
    'THE COMPARISON, ONE PARAGRAPH. Two public Lean 4 / Mathlib developments formalize the objects. (a) Bulka`s '
    'li-criterion-rh-equivalence-lean (created 2026-09-05, main ' + BULKA_SHA[:8] + '; imported into Vilin97/lean-pool by PR #495, '
    'merged 2026-09-28) states li_criterion : RiemannHypothesis <-> (forall n, 0 <= (taylorCoeff riemannXi n).re), the '
    'coefficient being the n-th Taylor coefficient at 0 of the log-derivative of xi(1/(1-z)) (Li`s lambda_{n+1}), BOTH '
    'DIRECTIONS, and li_coefficients_eq_zero_sum : that coefficient equals (1/2) times the sum over the strip zeros, with '
    'multiplicity analyticOrderNatAt riemannXi, of the symmetric pair (1 - (1 - 1/rho)^{-(n+1)}) + (1 - (1 - 1/rho)^{n+1}), '
    'with summability; its README and formalization.yaml report the standard three and no sorry (read, not built here). '
    'The kernel`s LiCoeff n is defined directly as (1/2) the tsum over Mathlib`s strip zeros of mult * Re(pairTerm n rho), '
    'the pairing with conj rho, multiplicity analyticOrderAt riemannZeta: the same zero-side object up to the index shift '
    'and the choice of partner (1 - rho against conj rho), with no Taylor coefficient; the kernel holds the forward half '
    '(rh_imp_li_nonneg) and not the converse, which Bulka`s ReverseDirection proves by a Pringsheim-type argument, not a '
    'Turan-type power-sum lemma. (b) Arda`s telperion node RH_bl_explicit_formula (PR #562, merged 2026-09-19; the node '
    'marked proved 2026-09-21 by E6Bridge27.bl_explicit_formula at main ' + ARDA_SHA[:8] + ', by its own record, read, not '
    'built here) states Tendsto (liZeroSum n) atTop (nhds (archSide n + finiteSide n)) for n >= 1: the zero side as the '
    'limit of symmetric HEIGHT windows, the arithmetic side as the Bombieri-Lagarias residue closed forms (S_inf(n) with '
    'gamma, log pi, zeta(j); S_f(n) with the eta_j of -zeta`/zeta at 1). li_identity_sym states LiCoeff n as the '
    'delta -> 0+ limit of EF_lit`s literature right-hand side (the prime sum and the Gamma term of Zeta23`s explicit '
    'formula) at the symmetric smoothed members of the Bombieri-Lagarias test function: the same identity`s two sides, '
    'reached by a different limit (a family of test functions in EF_lit`s class, the zero side absolutely summed, rather '
    'than height windows of the unsmoothed kernel) and with the arithmetic side left as EF_lit`s integral and prime '
    'series rather than evaluated in closed form. No sentence here claims priority for either side.')


def priorart():
    gr = jl('b564_priorart_grep.json')
    gh = jl('b564_web_gh.json')
    ws = jl('b564_web_search.json')
    ctl = rd(os.path.join(D, 'b564_priorart_control.txt'))
    L = ['b564 -- COMPONENT 2: PRIOR ART FOR LI`S CRITERION AND THE BOMBIERI-LAGARIAS FORMULA, UNDER (R174)(3), b536`S FORM', '',
         '### (i)-(ii) THE CHECKOUTS (relay data/b564_priorart_grep.txt, the hit lines there):']
    for side in ('mathlib', 'zeta23'):
        for q, v in gr[side].items():
            L.append('    %-8s %-52s files %4d lines %5d' % (side, q[:52], v['files'], v['lines']))
    L.append('    the Mathlib bare-`Li` hits read by hand: every one an author name or a copyright line (relay data/b564_priorart_grep.txt)')
    L.append('    ### THE POSITIVE CONTROL (relay data/b564_priorart_control.txt), the same regexes over SIDEExplicitFormula/:')
    L += ['      ' + l.strip() for l in ctl.split(NL) if l.startswith('  query')]
    L.append('    ### Keiper, `Li criterion` and the (rho - 1)/rho spelling carry NO positive control in the kernel: their zeros')
    L.append('    ### are a search that could not have been shown to fire, not an absence.')
    L += ['', '### (iii) GITHUB BY NAME, through `gh` (authenticated as the corpus`s account): code search and repository search']
    for s in gh:
        rf = ' (refused first at %s: rate limit; retried)' % s['refused_first']['date'] if s.get('refused_first') else ''
        L.append('    %-5s %-42s lang %-4s %s rc %d hits %3d%s' % (s['kind'], s['query'][:42], s.get('language', '-'), s['date'], s['rc'], s['count'], rf))
    lean_paths = sorted(set((h['repo'], h['path']) for s in gh if s['kind'] == 'code' for h in s['hits'] if h['path'].endswith('.lean')))
    L.append('    ### .lean paths among ALL code hits: %d. ### THE CODE-SEARCH ROUTE MISSES A KNOWN POSITIVE: Bulka`s' % len(lean_paths))
    L.append('    ### comparator/Challenge.lean carries "Li`s criterion" and "Bombieri-Lagarias" in its text, and neither query')
    L.append('    ### returned it; its zeros for Lean files are not evidence of absence. The repository search found it.')
    L.append('    the repository hits naming a formalization, by description:')
    for s in gh:
        if s['kind'] == 'repos':
            for h in s['hits']:
                L.append('      [%s] %s (%s, updated %s) -- %s' % (s['query'], h['url'], h['language'], h['updated'], h['description'][:120]))
    L += ['', '### (iv) THE WEB SEARCHES (arXiv, the Lean Zulip archive, the open web), each with its query, date and URLs:']
    for s in ws:
        L.append('    [%s] %s ; domains %s ; %d URLs' % (s['date'], s['query'], s['domains'], len(s['urls'])))
        L += ['        ' + u for u in s['urls']]
        L += ['        READ: ' + r for r in s['read']]
        if s.get('note'):
            L.append('        NOTE: ' + s['note'])
    L += ['', '### THE HITS THAT ARE FORMALIZATIONS, READ FOR THEIR STATEMENTS (the fetched files banked as relay data/b564_fetched_*):',
          '  (a) %s @%s -- comparator/Challenge.lean (b564_fetched_bulka_Challenge.lean.txt):' % (BULKA, BULKA_SHA)]
    ch = rd(os.path.join(D, 'b564_fetched_bulka_Challenge.lean.txt')).split(NL)
    for i, l in enumerate(ch):
        if l.startswith(('theorem', 'def ', '    RiemannHypothesis', '    Summable', '    taylorCoeff', '      = ', '        (', '          ((', '            ((', '              +', '  (deriv', '  f (1', '  deriv', '  (1 / 2')):
            L.append('      %4d | %s' % (i + 1, l))
    yml = rd(os.path.join(D, 'b564_fetched_bulka_formalization.yaml.txt')).split(NL)
    L += ['      formalization.yaml %d | %s' % (i + 1, l.strip()) for i, l in enumerate(yml) if re.search(r'sorry_count|axioms:|reviewers|No external', l)]
    L.append('  (b) %s @%s -- the node statement (b564_fetched_arda_RH_bl_explicit_formula.lean.txt) and its proof module' % (ARDA, ARDA_SHA))
    L.append('      telperion/examples/rvm_bridge/lean/E6Bridge27.lean (b564_fetched_arda_E6Bridge27.lean.txt):')
    for f in ('b564_fetched_arda_RH_bl_explicit_formula.lean.txt', 'b564_fetched_arda_E6Bridge27.lean.txt'):
        t = rd(os.path.join(D, f)).split(NL)
        k = [i for i, l in enumerate(t) if l.startswith('theorem bl_explicit_formula')]
        for i in k:
            L += ['      %s %4d | %s' % (f[13:24], i + 1 + j, t[i + j]) for j in range(4) if i + j < len(t)]
    L += ['', '### ' + COMPARE, '',
          '### (N2) -- ### **REFUTED**: two formalizations found in public Lean repositories (a) and (b); none in Mathlib at 51e6992e',
          '### or in Zeta23 at v0.7. Neither was built or audited by this act; their claims are their own records`.']
    put_txt('b564_prior_art.txt', L)
    put_json('b564_prior_art.json', dict(n2='REFUTED', bulka=dict(url=BULKA, sha=BULKA_SHA, created='2026-09-05', lean_pool_pr495_merged='2026-09-28'),
                                         arda=dict(url=ARDA, sha=ARDA_SHA, pr562_merged='2026-09-19', node_proved='2026-09-21'),
                                         lean_paths_in_code_hits=len(lean_paths), compare=COMPARE))
    print(NL.join(L[:3]))
    print('  lines %d ; written: b564_prior_art.txt' % len(L))


FIELD = ('*Appended 2026-09-29 by b564 to the field entry (:5575), its sources block (:5601) and b561’s line (:6064), under '
         '`(R174)`(3) -- PRIOR ART FOR THE LI FORM, SEARCHED IN b536’S FORM (relay `data/b564_prior_art.txt`):* Mathlib at '
         '`51e6992e` and Zeta23 at v0.7 carry no Li coefficient, no Keiper or Bombieri–Lagarias name and no (1 − 1/ρ)^n in any '
         'searched spelling (a positive control over the kernel’s own tree fires). Two public Lean 4 / Mathlib developments '
         'formalize the objects, read for their statements and not built here: (a) ' + BULKA + ' (created 2026-09-05, read at '
         '`' + BULKA_SHA[:8] + '` on 2026-09-29; imported into https://github.com/Vilin97/lean-pool by pull request 495, merged '
         '2026-09-28) states Li’s criterion in both directions over Mathlib’s RiemannHypothesis, the coefficient as a Taylor '
         'coefficient of the log-derivative of ξ(1/(1 − z)), and its identity with the symmetric zero sum of 1 − (1 − 1/ρ)^(n+1); '
         '(b) ' + ARDA + ' (its node RH_bl_explicit_formula, pull request 562 merged 2026-09-19, recorded proved 2026-09-21 at '
         '`' + ARDA_SHA[:8] + '` by its own record, read 2026-09-29) states the Bombieri–Lagarias explicit formula on Li’s test '
         'class, the symmetric height-window zero sums tending to the archimedean and finite closed forms for n ≥ 1. Beside '
         'them the programme holds the Li form’s forward half (`rh_imp_li_nonneg`, v0.4) and the identity in limit form over '
         'the symmetric smoothed family (`li_identity_sym`, v0.7); the converse, compiled in (a) by a Pringsheim-type argument, '
         'is not compiled here. GitHub’s code search returned no Lean file for any query, (a)’s included, so its zeros are not '
         'evidence of absence; the Lean Zulip archive was reached only through a web search that returned none of its pages. '
         'No sentence here claims priority.')


def fieldappend():
    guard_absent(FIND, FIELD[:70])
    res = append_to(FIND, NL + FIELD + NL)
    n = line_of(FIND, FIELD[:70])
    print('### the field-entry append at FINDINGS :%s ; %s' % (n, json.dumps(res)))
    put_json('b564_fieldappend.json', dict(line=n, text=poss(FIELD), res=res))


def _find_decl(rel, name, rev=None):
    t = at(rev or V07, rel)
    k = decl_at(t, name)
    if k is None:
        k = next((i + 1 for i, l in enumerate(t.split(NL)) if re.match(r'\s*' + re.escape(name) + r'\s*:', l)), None)
    return k, (t.split(NL)[k - 1].strip() if k else None)


CONV_WO = ('*Appended 2026-09-29 by b564, under the author’s ruling `(R174)`(4), to the LI-WEIL-BRIDGE work-order (:3548; b563’s '
           'line at :11590) -- THE CONVERSE RE-PRICED ON THE REFLECTION MAP (relay `data/b564_converse_price.txt`):* the converse '
           '(∀ n, 0 ≤ LiCoeff n → RiemannHypothesis) in four items. (V1) reflection stability with multiplicity -- COMPILED: '
           'the fields reflect_mem and mult_reflect of Zeta23’s ZeroConfig (Zeta23/Defs.lean :143-:144), discharged for ζ by '
           'zeta_reflect_zero and zeta_mult_reflect (Zeta23/ZetaReflect.lean :294, :330). (V2) an off-line zero has an orbit '
           'member with |1 − 1/ρ′| exceeding 1 -- DERIVED ON THE PAGE, NOT COMPILED: |1 − 1/ρ|² − 1 = (1 − 2β)/(β² + γ²), so '
           'the modulus exceeds 1 exactly when β lies left of 1/2, and reflection sends β to 1 − β; the kernel holds only the '
           'on-line equality (norm_one_sub_inv_of_re_half, LiWeil.lean :91), the strict form is absent from the kernel and from '
           'Mathlib by name; its price is one elementary lemma. (V3) the dominant set is finite -- DERIVED ON THE PAGE, NOT '
           'COMPILED: |1 − 1/ρ|² ≥ 1 + η forces β² + γ² ≤ 1/η, a bounded region, and finite_window (Zeta23/Defs.lean :146) '
           'makes the zeros there finitely many, so the maximum r_max is attained at finitely many zeros; the kernel’s nearest '
           'fact is tieSet_finite for the power-window score (PowerWindow.lean :403); its price is one lemma. (V4) the power-sum '
           'lemma -- ABSENT: for finitely many z_k of modulus r_max with multiplicities, Re Σ m_k z_k^n ≤ −c r_max^n for '
           'infinitely many n; Mathlib at 51e6992e holds no Turán-type power-sum inequality by name (H16d HELD); this is the '
           'lemma of substance. The kernel’s power-window route (PowerLimit.lean) meets the same finite dominant set and '
           'escapes the lemma by choosing a polynomial that sets the phases; Li’s fixed test functions leave no such freedom. '
           'A public formalization proves the converse by a different route, a Pringsheim-type argument on the Taylor '
           'coefficients of the log-derivative of ξ(1/(1 − z)) (FINDINGS :6136); consuming it here would first identify LiCoeff '
           'with that coefficient. Nothing is attempted.')

CONV_PTR = ('*Appended 2026-09-29 by b564, under the author’s ruling `(R174)`(4), to the consumer read (:11542) -- THE RESIDUE '
            'CHAIN’S LAST STEP POINTED AT THE PRICE:* the chain’s last step, liCriterion : Register4_positivity lam → '
            'RiemannHypothesis (SIDE-kernel, R4_positivity_to_RH), restated with λ := LiCoeff is the converse priced at the '
            'line above, (V1) compiled, (V2) and (V3) one lemma each, (V4) the power-sum lemma absent at the rev.')


def converse():
    L = ['b564 -- COMPONENT 3: THE CONVERSE RE-PRICED ON THE REFLECTION MAP, UNDER (R174)(4). NOTHING IS ATTEMPTED.', '',
         '### THE CONVERSE: forall n, 0 <= LiCoeff n -> RiemannHypothesis (LiCoeff at LiWeil.lean :243). Each item with what it',
         '### rests on, printed from the kernel at v0.7 = 1e4a007 or from Mathlib at 51e6992e, or marked ABSENT.', '']
    facts = [('(V1)', 'Zeta23/Defs.lean', 'reflect_mem'), ('(V1)', 'Zeta23/Defs.lean', 'mult_reflect'),
             ('(V1)', 'Zeta23/ZetaReflect.lean', 'zeta_reflect_zero'), ('(V1)', 'Zeta23/ZetaReflect.lean', 'zeta_mult_reflect'),
             ('(V1)', 'SIDEExplicitFormula/PowerLimit.lean', 'reflect_re'),
             ('(V2)', 'SIDEExplicitFormula/LiWeil.lean', 'norm_one_sub_inv_of_re_half'),
             ('(V3)', 'Zeta23/Defs.lean', 'finite_window'), ('(V3)', 'SIDEExplicitFormula/PowerWindow.lean', 'tieSet_finite'),
             ('(V3)', 'SIDEExplicitFormula/PowerWindow.lean', 'killSet_finite')]
    for tag, rel, name in facts:
        k, l = _find_decl(rel, name)
        if k is None:
            kk = next((i + 1 for i, x in enumerate(at(V07, rel).split(NL)) if re.search(r'\b' + name + r'\b', x) and 'theorem' in x), None)
            k, l = kk, (at(V07, rel).split(NL)[kk - 1].strip() if kk else None)
        L.append('  %s %s:%s -- %s' % (tag, rel, k, (l or 'NOT FOUND')[:170]))
    gr = jl('b564_powersum_grep.json')
    kern = subprocess.run(['git', '-C', EF, 'grep', '-n', '-E', 'norm_one_sub_inv|one_sub_inv', V07, '--', 'SIDEExplicitFormula', 'Zeta23'],
                          capture_output=True).stdout.decode('utf-8', 'replace').strip().split(NL)
    ml = subprocess.run(['git', '-C', ML, 'grep', '-c', '-E', 'norm_one_sub_inv|abs_one_sub_inv', 'HEAD', '--', 'Mathlib'],
                        capture_output=True).stdout.decode('utf-8', 'replace').strip()
    L += ['', '### (V2) THE ALGEBRA, DERIVED ON THE PAGE (a derivation, not compiled). For rho = beta + i gamma, rho != 0:',
          '###   |1 - 1/rho|^2 = |rho - 1|^2 / |rho|^2 = ((beta - 1)^2 + gamma^2) / (beta^2 + gamma^2),',
          '###   |1 - 1/rho|^2 - 1 = (1 - 2 beta) / (beta^2 + gamma^2), positive exactly when beta < 1/2;',
          '###   reflect rho = 1 - conj rho has real part 1 - beta (reflect_re), so an off-line zero with beta > 1/2 has its',
          '###   reflection with 1 - beta < 1/2, and the orbit carries a member of modulus exceeding 1.',
          '### the kernel`s own |1 - 1/rho| lemmas (git grep at v0.7, "norm_one_sub_inv|one_sub_inv", declarations and uses): %d lines' % len([x for x in kern if x]),
          ] + ['      ' + x[:170] for x in kern if x] + \
         ['### Mathlib by name ("norm_one_sub_inv|abs_one_sub_inv", git grep -c at HEAD = 51e6992e): %s' % (ml or '0 files'),
          '### ### (V2) STATUS: the on-line equality COMPILED (LiWeil.lean :91); the strict inequality off the line ABSENT; price one lemma.',
          '', '### (V3) THE DOMINANT SET, DERIVED ON THE PAGE (a derivation, not compiled). |1 - 1/rho|^2 >= 1 + eta (eta > 0) forces',
          '###   (1 - 2 beta) >= eta (beta^2 + gamma^2), and 1 - 2 beta <= 1 on the strip, so beta^2 + gamma^2 <= 1/eta: a bounded',
          '###   region; finite_window gives finitely many zeros with |gamma| <= eta^(-1/2); so above any level exceeding 1 there are',
          '###   finitely many zeros, the supremum r_max over off-line zeros is attained, and the set where it is attained is finite.',
          '###   No count bound (N(T+1) - N(T)) is consumed. ### (V3) STATUS: ABSENT as a lemma; its parts compiled (finite_window;',
          '###   the analogue tieSet_finite for the power-window score); price one lemma.', '',
          '### (V4) THE POWER-SUM LEMMA. For finitely many complex z_1..z_K of modulus r > 1 with multiplicities m_k >= 1,',
          '###   Re sum_k m_k z_k^n <= -c r^n for infinitely many n (some c > 0) -- the Bombieri-Lagarias / Turan-type step.',
          '### THE SEARCH (relay data/b564_powersum_grep.txt, the Mathlib checkout at 51e6992e, case-insensitive):']
    for q, v in gr.items():
        fs = sorted(set(h[0] for h in v['hits']))
        L.append('    %-24s files %3d lines %4d : %s' % (q, v['files'], v['lines'], ', '.join(f.replace('Mathlib/', '') for f in fs)))
    L += ['### THE HITS READ BY FILE: Turan -- Turan`s theorem of extremal graph theory and its density (SimpleGraph/Extremal);',
          '###   powerSum / power sum -- the power-sum symmetric polynomials psum and Newton`s identities, Faulhaber`s power-sum',
          '###   congruence over ZMod p, and a cardinal-arithmetic identity; sum of powers -- Jensen`s inequality for sums of real',
          '###   powers (Algebra/Order/Chebyshev), factorization multiplicities, a power-series exp identity, cyclotomic units;',
          '###   Dirichlet approximation -- Dirichlet`s approximation theorem (Real.exists_int_int_abs_mul_sub_le) and its',
          '###   normed-group form; Kronecker -- Kronecker products of matrices, the Kronecker delta, and Kronecker`s theorem on',
          '###   algebraic integers whose conjugates all have modulus 1 (NumberField/InfinitePlace/Embeddings). NONE bounds the real',
          '###   part of a sum of n-th powers of complex numbers from above or below: none is a Turan-type power-sum inequality.',
          '### THE MATCHER FIRES: "Turan" found Turan`s graph theorem, so the regex reads the name; the search is BY NAME, as the',
          '### ruling words H16d, and a power-sum inequality under another name is outside it.',
          '### ### **H16d : HELD** -- no Turan-type power-sum inequality by name at the rev. ### (N3) : HELD.',
          '### ### (V4) STATUS: ABSENT; the lemma of substance.', '',
          '### THE ALTERNATIVE ROUTE, BESIDE THE PRICE (not a fifth item): the public formalization of FINDINGS :6136 (a) proves',
          '### positivity -> RH by a Pringsheim-type argument on the Taylor coefficients of the log-derivative of xi(1/(1 - z)),',
          '### with no power-sum lemma; for the kernel it would first need LiCoeff identified with that coefficient (the index',
          '### shift n -> n + 1 and the partner conj rho against 1 - rho). Not attempted; not imported.', '',
          '### THE APPENDS: the work-order line and the pointer from the residue chain`s last step (OPEN_TRAILS, below).']
    out = {}
    for key, txt in (('workorder', CONV_WO), ('pointer', CONV_PTR)):
        # ### b564 defect (c): the two texts share their first 70 characters, so a 70-character guard refused the second
        # ### after the first landed. The key is now 200 characters, and a line already present is recorded, not re-appended.
        if poss(txt[:200]).encode('utf-8') in open(OT, 'rb').read():
            out[key] = dict(line=line_of(OT, txt[:200]), res='ALREADY PRESENT (appended by the first run)')
        else:
            res = append_to(OT, NL + txt + NL)
            out[key] = dict(line=line_of(OT, txt[:200]), res=res)
        L.append('    %s at OPEN_TRAILS :%s' % (key, out[key]['line']))
    put_txt('b564_converse_price.txt', L)
    put_json('b564_converse_price.json', dict(h16d='HELD', n3='HELD', appends=out, v=dict(V1='COMPILED', V2='ABSENT (one lemma)',
                                                                                          V3='ABSENT (one lemma)', V4='ABSENT (the lemma of substance)')))
    print(NL.join(L))


ZETA_ID = re.compile(r'\b(?:riemannZeta\w*|completedRiemannZeta\w*|\w*riemannZeta\w*|zeta_\w+|\w+_riemannZeta\w*)\b')

# ### THE SEAT`S READING OF EACH FRONTIER MODULE`S KIND (READING (5)), one clause each; filled for the modules the tool
# ### finds at the frontier, a module not listed here printing UNREAD so no kind is assigned silently.
KIND = {
    'Zeta23.Statement': ('THE CONFIGURATION INSTANCE', 'it defines IsNontrivialZero and zeroMult from riemannZeta, the seam '
                         'structure ZetaSeam and zetaZeros, which builds ZeroConfig from zeta`s zeros'),
    'Zeta23.FromPNTPlus.ZetaBounds': ('THE GROWTH SIDE', 'bounds on zeta and zeta` in vertical strips through the Euler-Maclaurin '
                                      'form riemannZeta0, the lower bounds near re s = 1 and the zero-free region, the '
                                      'log-derivative bounds'),
}


def dag():
    rows = {}
    for l in rd(os.path.join(D, 'b562_zeta23_modules.txt')).split(NL):
        m = re.match(r'\s{4}(Zeta23\.\S+)\s+(GENERIC|ζ-SPECIFIC)\s+(.*?)\s\|\s(.*)$', l)
        if m:
            imps = [] if m.group(4).strip() == '(none)' else [x.strip() for x in m.group(4).split(',')]
            rows[m.group(1)] = dict(cls=m.group(2), reason=m.group(3), bank_imports=imps)
    files = [f for f in g(EF, 'ls-tree', '-r', '--name-only', V07, 'Zeta23').split(NL) if f.endswith('.lean')]
    mods = {f[:-5].replace('/', '.'): f for f in files}
    for mname, f in mods.items():
        t = at(V07, f)
        rows.setdefault(mname, dict(cls='NOT IN THE BANK', reason='', bank_imports=[]))
        rows[mname]['file_imports'] = [l.split()[1] for l in t.split(NL) if l.startswith('import Zeta23')]
        code = re.sub(r'/-.*?-/', '', t, flags=re.S)
        code = NL.join(l.split('--')[0] for l in code.split(NL))
        rows[mname]['code'] = code
    diffs = [(m, sorted(set(r['bank_imports']) ^ set(r.get('file_imports', [])))) for m, r in rows.items()
             if set(r['bank_imports']) != set(r.get('file_imports', []))]
    spec = {m for m, r in rows.items() if r['cls'] == 'ζ-SPECIFIC'}
    frontier = sorted(m for m in spec if not any(i in spec for i in rows[m]['file_imports']))
    depth = {}

    def dep(m):
        if m not in depth:
            depth[m] = 0
            depth[m] = 1 + max([dep(i) for i in rows[m]['file_imports']] or [-1])
        return depth[m]
    for m in rows:
        dep(m)

    def reach(a, b):
        seen, st = set(), [a]
        while st:
            x = st.pop()
            for i in rows[x]['file_imports']:
                if i == b:
                    return True
                if i not in seen:
                    seen.add(i)
                    st.append(i)
        return False
    pairs = [(a, b) for a in frontier for b in frontier if a < b]
    unordered = [(a, b) for a, b in pairs if not reach(a, b) and not reach(b, a)]
    order = sorted(frontier, key=lambda m: (depth[m], 0 if KIND.get(m, ('',))[0] == 'THE CONFIGURATION INSTANCE' else 1, m))
    ties = [(a, b) for a, b in unordered if depth[a] == depth[b]]
    ml_idx = {}
    for fdir in ('Mathlib/NumberTheory/LSeries', 'Mathlib/NumberTheory/Harmonic', 'Mathlib/Analysis/SpecialFunctions'):
        out = subprocess.run(['git', '-C', ML, 'grep', '-n', '-E', r'^(theorem|lemma|def|noncomputable def|irreducible_def)\s+\S*[Zz]eta',
                              'HEAD', '--', fdir], capture_output=True).stdout.decode('utf-8', 'replace')
        for l in out.split(NL):
            m = re.match(r'HEAD:([^:]+):(\d+):\S+(?:\s+def)?\s+(\S+)', l)
            if m:
                ml_idx.setdefault(m.group(3).split('.')[-1], '%s:%s' % (m.group(1), m.group(2)))
    L = ['b564 -- COMPONENT 4: THE IMPORT DAG OF ZETA23 AND THE ζ-SPECIFIC FRONTIER, UNDER (R174)(5)', '',
         '### READ TWICE: the b562 bank`s import column (relay data/b562_zeta23_modules.txt) and the `import Zeta23.*` lines of the',
         '### files at v0.7 = %s. Modules: bank %d, files %d. ### EDGES DISAGREEING: %s' % (
             V07[:7], len([r for r in rows.values() if r['cls'] != 'NOT IN THE BANK']), len(mods), diffs or 'NONE'), '',
         '    %-62s %-11s %-5s %s' % ('module', 'class', 'depth', 'its Zeta23 imports (from the file)')]
    for m in sorted(rows, key=lambda x: (depth[x], x)):
        r = rows[m]
        L.append('    %-62s %-11s %-5d %s' % (m, r['cls'], depth[m], ', '.join(r['file_imports']) or '(none)'))
    nspec, ngen = len(spec), len([m for m in rows if rows[m]['cls'] == 'GENERIC'])
    L += ['', '### ### **ζ-SPECIFIC %d ; GENERIC %d ; FILES %d**' % (nspec, ngen, len(mods)), '',
          '### THE FRONTIER: the ζ-specific modules none of whose Zeta23 imports is ζ-specific.']
    front = []
    for m in order:
        ids = sorted(set(ZETA_ID.findall(rows[m]['code'])))
        kind = KIND.get(m, ('UNREAD', 'no kind assigned'))
        L.append('  %-40s depth %d ; KIND %s -- %s' % (m, depth[m], kind[0], kind[1]))
        L.append('      imports (Zeta23): %s' % (', '.join(rows[m]['file_imports']) or '(none)'))
        L.append('      what it consumes from Mathlib about ζ (identifiers of its comment-stripped code; the Mathlib line where the name is declared):')
        for i in ids:
            L.append('        %-44s %s' % (i, ml_idx.get(i, 'declared in this module or not a Mathlib name' if re.search(r'^(?:theorem|lemma|def|noncomputable def)\s+' + re.escape(i) + r'\b', rows[m]['code'], re.M) else 'NOT LOCATED by the declaration scan')))
        front.append(dict(module=m, depth=depth[m], kind=kind[0], ids=ids, imports=rows[m]['file_imports']))
    L += ['', '### IMPORT ORDER (READING (5)): by depth, then the configuration instance first, then by name.',
          '### pairs of frontier modules with no import path between them: %s' % (unordered or 'NONE'),
          '### of these, at equal depth (a TIE the DAG does not break; broken by the face`s rule): %s' % (ties or 'NONE'),
          '### the order: %s' % ' -> '.join(order), '']
    n = len(frontier)
    first = KIND.get(order[0], ('UNREAD',))[0] if order else None
    arch = [f['module'] for f in front if f['kind'] == 'THE ARCHIMEDEAN SIDE']
    h16c = (n <= 4) and first in ('THE CONFIGURATION INSTANCE', 'THE EULER SIDE') and not arch
    L += ['### H16c: the frontier`s count %d (the ruling`s cap four) ; its earliest member %s (%s) ; archimedean modules at the frontier: %s' % (
              n, order[0] if order else None, first, arch or 'NONE'),
          '### ### **H16c : %s**%s' % ('HELD' if h16c else 'REFUTED', ' -- the earliest member is set by the face`s tie rule, printed above' if ties else ''),
          '### (N4) : %s' % ('HELD' if h16c else 'REFUTED')]
    put_txt('b564_dag.txt', L)
    put_json('b564_dag.json', dict(frontier=front, order=order, unordered=unordered, ties=ties, h16c='HELD' if h16c else 'REFUTED',
                                   generic=sorted(m for m in rows if rows[m]['cls'] == 'GENERIC'), specific=sorted(spec),
                                   edge_diffs=diffs, depth=depth))
    print(NL.join(L[-30:]))


PARTS = {
    'a': ('THE χ-INSTANCE OF THE ZERO CONFIGURATION', 'SIDEExplicitFormula/Chi/ZeroConfig.lean', 'a_'),
    'b': ('THE GENERIC MODULES CONSUMED BY THE χ-INSTANCE', 'SIDEExplicitFormula/Chi/Generic.lean', 'b_'),
    'c1': ('THE FRONTIER`S SECOND MODULE: ZetaBounds`s χ-ANALOGUES, IN ITS ORDER', 'SIDEExplicitFormula/Chi/ZetaBounds.lean', 'c_'),
}
# ### every fact part (a) consumes, by name, with the file the tool reads its line from (Mathlib at the rev, or the kernel at v0.7)
FACTS_A = [
    ('Mathlib', 'Mathlib/NumberTheory/LSeries/DirichletContinuation.lean', 'differentiable_LFunction'),
    ('Mathlib', 'Mathlib/NumberTheory/LSeries/DirichletContinuation.lean', 'differentiable_completedLFunction'),
    ('Mathlib', 'Mathlib/NumberTheory/LSeries/DirichletContinuation.lean', 'LFunction_eq_completed_div_gammaFactor'),
    ('Mathlib', 'Mathlib/NumberTheory/LSeries/DirichletContinuation.lean', 'completedLFunction_one_sub'),
    ('Mathlib', 'Mathlib/NumberTheory/LSeries/DirichletContinuation.lean', 'Even.gammaFactor_def'),
    ('Mathlib', 'Mathlib/NumberTheory/LSeries/DirichletContinuation.lean', 'Odd.gammaFactor_def'),
    ('Mathlib', 'Mathlib/NumberTheory/LSeries/Nonvanishing.lean', 'LFunction_ne_zero_of_one_le_re'),
    ('Mathlib', 'Mathlib/Analysis/SpecialFunctions/Gamma/Deligne.lean', 'differentiable_Gammaℝ_inv'),
    ('Mathlib', 'Mathlib/Analysis/Analytic/Order.lean', 'analyticOrderAt_ne_top_of_isPreconnected'),
    ('Mathlib', 'Mathlib/Analysis/Analytic/Order.lean', 'analyticOrderAt_mul'),
    ('Mathlib', 'Mathlib/Analysis/Analytic/Order.lean', 'analyticOrderAt_comp_of_deriv_ne_zero'),
    ('Mathlib', 'Mathlib/Analysis/Analytic/IsolatedZeros.lean', 'eqOn_zero_or_eventually_ne_zero_of_preconnected'),
    ('Mathlib', 'Mathlib/Analysis/Complex/CauchyIntegral.lean', '_root_.Differentiable.analyticAt'),
    ('Mathlib', 'Mathlib/Analysis/SpecialFunctions/Pow/Deriv.lean', 'DifferentiableAt.const_cpow'),
    ('kernel', 'SIDEExplicitFormula/GRHWeil.lean', 'ne_one_of_ne_one'),
    ('kernel', 'SIDEExplicitFormula/GRHWeil.lean', 'isPrimitive_inv'),
    ('kernel', 'SIDEExplicitFormula/GRHWeil.lean', 'gammaFactor_ne_zero_of_re_pos'),
    ('kernel', 'SIDEExplicitFormula/GRHWeil.lean', 'LFunction_inv_conj'),
    ('kernel', 'SIDEExplicitFormula/GRHWeil.lean', 'LFunction_zero_iff_conj'),
    ('kernel', 'SIDEExplicitFormula/GRHWeil.lean', 'analyticOrderAt_LFunction_inv_conj'),
]


def _fact_line(where, rel, name):
    if where == 'Mathlib':
        t = rd(os.path.join(ML, *rel.split('/')))
    else:
        t = at(V07, rel)
    short = name.split('.')[-1]
    for i, l in enumerate(t.split(NL)):
        if re.match(r'\s*(?:protected\s+)?(?:theorem|lemma|def|noncomputable def)\s+' + re.escape(name) + r'(?=[\s:({\[]|$)', l) or \
                re.match(r'\s*(?:protected\s+)?(?:theorem|lemma)\s+' + re.escape(short) + r'(?=[\s:({\[]|$)', l):
            return i + 1
    return None


def _attempts(tag):
    idx = [l for l in rd(os.path.join(D, 'b564_att_index.txt')).split(NL) if l.startswith(tag)]
    out = []
    for l in idx:
        lab = l.split()[0]
        errs = [x for x in rd(os.path.join(D, 'b564_att_%s.txt' % lab)).split(NL) if ': error' in x]
        out.append((lab, l, errs))
    return out


def part(X):
    title, rel, tag = PARTS[X]
    tip = g(EF, 'rev-parse', BR).strip()
    src = at(tip, rel)
    prints = parse_prints(rd(os.path.join(D, 'b564_prints.txt')))
    decls = [d for d in jl('b564_decls.json') if d['file'] == rel]
    L = ['b564 -- READING (6): PART (%s) -- %s' % (X, title), '',
         '### the branch %s at %s, cut from v0.7 = %s ; the file %s (sha256 at the tip %s)' % (
             BR, tip[:7], V07[:7], rel, hashlib.sha256(src.encode('utf-8')).hexdigest()[:16]), '',
         '### THE ELABORATION ATTEMPTS (`lake env lean --stdin` against the scratchpad oleans; the index line, then the errors):']
    att = _attempts(tag)
    for lab, head, errs in att:
        L.append('    ' + head)
        L += ['        | ' + e[:220] for e in errs]
    closed = att[-1][1] if att else None
    L += ['### the part closed at attempt %d of four' % len(att) if att and ' exit 0 ' in att[-1][1] else '### ### the part DID NOT CLOSE', '']
    L.append('### THE DECLARATIONS (%d), AS THE TIP STATES THEM (first lines), AND LEAN`S PRINT OF EACH:' % len(decls))
    rows = {}
    for d in decls:
        ax = prints.get(d['name'])
        rows[d['name']] = dict(kind=d['kind'], axioms=ax, std3=ax is not None and set(ax) <= set(STD3))
        first = src.split(NL)[d['line'] - 1].strip()
        L.append('    %4d | %-110s %s' % (d['line'], first[:110], ax))
    ok = all(r['std3'] for r in rows.values())
    L.append('### ### **PRINTED %d OF %d ; THE STANDARD THREE OR FEWER, NO sorryAx : %s**' % (
        sum(1 for r in rows.values() if r['axioms'] is not None), len(rows), ok))
    extra = {}
    if X == 'a':
        L += ['', '### EVERY FACT THE INSTANCE CONSUMES, BY NAME (Mathlib at 51e6992e; the kernel at v0.7):']
        for where, frel, name in FACTS_A:
            k = _fact_line(where, frel, name)
            L.append('    %-8s %-58s %s:%s' % (where, name, frel, k if k else 'NOT LOCATED'))
        used_root = 'rootNumber' in re.sub(r'/-.*?-/', '', src, flags=re.S).replace('rootNumber χ⁻¹', '')
        L += ['### NO ROOT-NUMBER FACT CONSUMED: the one mention of rootNumber is inside the constant c(s) of the functional',
              '### equation (the order inequality needs c analytic, not nonzero); a second mention: %s' % used_root,
              '### ### **H16b : %s** -- the χ-instance compiles from the rev`s LFunction facts at the standard three.' % ('HELD' if ok else 'REFUTED'),
              '### (S2) : %s' % ('HELD' if ok and not used_root else 'REFUTED')]
        extra = dict(h16b='HELD' if ok else 'REFUTED', s2='HELD' if ok and not used_root else 'REFUTED')
    if X == 'b':
        gs = jl('b564_generic_scan.json')
        dag = jl('b564_dag.json')
        recl = sorted(m for m, v in gs.items() if v)
        n_gen, n_spec = len(dag['generic']), len(dag['specific'])
        ls = jl('b564_generic_leanscan.json')
        L += ['', '### THE CONSUMPTION BUILD: every one of the %d generic modules imported by name, unedited (the Zeta23 blobs at the' % n_gen,
              '### tip against v0.7: %s); the Lean scan`s %d consumer declarations instantiated at chiZeroConfig (relay' % (
                  'UNCHANGED' if not g(EF, 'diff', '--name-only', V07, tip, '--', 'Zeta23').strip() else 'CHANGED', len(ls['consumers'])),
              '### data/b564_generic_leanscan.txt); the modules with no ZeroConfig-taking declaration are consumed by import alone.',
              '', '### THE SCAN FOR riemannZeta AND THE ζ-SPECIFIC CONSTANTS (relay data/b564_generic_scan.txt, hit lines there),',
              '### read by hand -- each module carrying a marker, the lines that make it ζ-specific by the face`s definition:']
        why = {
            'Zeta23.Defs': ':55-:69 mu (ζ`s Γ bracket, digamma at 1/4 + iτ/2, log π), PiX (the pole of ζ), PX and nuX (the Λ(n) sum, no χ)',
            'Zeta23.ExplicitFormula': ':37 gammaBracket, :40-:44 literatureRHS (the pole terms paperFT k (±I/2), the Λ(n) sum, ζ`s Γ term)',
            'Zeta23.ExplicitFormula.Bridge': ':80-:165 bounds on mu, ζ`s Γ bracket',
            'Zeta23.GammaFacts': ':31-:87 mu`s evenness and smoothness (digamma at 1/4 + iτ/2)',
            'Zeta23.GammaFacts.Mu': ':120-:383 mu`s monotonicity and derivative bound; log π',
            'Zeta23.GammaFacts.StirlingVert': ':601-:615 mu`s Stirling expansion',
            'Zeta23.Hypotheses': ':62-:73 the fields on mu, :22-:46 the Λ(n) sums and nuX',
            'Zeta23.WeilEF.GammaRBracket': ':86 mu`s bracket (digamma(1/4 + it/2) - log π); its :42 is the generic logDeriv of Gammaℝ',
        }
        for m in recl:
            L.append('    %-34s RE-CLASSIFIED ζ-SPECIFIC -- %s' % (m, why.get(m, 'UNREAD')))
        L += ['### riemannZeta itself named in a generic module: %s' % (
                  [m for m, v in gs.items() if any(k.startswith('riemannZeta') for k in v)] or 'NONE'),
              '### ### **THE COUNT CORRECTED: GENERIC %d -> %d ; ζ-SPECIFIC %d -> %d** (the constants clause; the lexical rule of b562'
              % (n_gen, n_gen - len(recl), n_spec, n_spec + len(recl)),
              '### names none of them ζ-specific, since they carry ζ`s shape under neutral names -- b562`s own bank said so of two).',
              '### H16a`s first clause (consumed without edit): %s ; its second (no generic module names riemannZeta or a' % ('HELD' if ok else 'REFUTED'),
              '### ζ-specific constant): REFUTED by the %d modules above.' % len(recl),
              '### ### **H16a : REFUTED** ### (S3) : %s' % ('HELD' if ok and recl else 'REFUTED')]
        extra = dict(h16a='REFUTED', h16a_clause1='HELD' if ok else 'REFUTED', reclassified=recl, s3='HELD' if ok and recl else 'REFUTED',
                     generic_corrected=n_gen - len(recl), specific_corrected=n_spec + len(recl))
    if X == 'c1':
        hs = jl('b564_held_search.json')
        L += ['', '### THE ζ-ORIGINAL`S ζ-NAMING DECLARATIONS IN ORDER AND THEIR χ-ANALOGUES HERE:',
              '    analyticAt_riemannZeta (:184)             -> analyticAt_LFunction',
              '    differentiableAt_deriv_riemannZeta (:189) -> differentiableAt_deriv_LFunction',
              '    riemannZetaResidue (:193)                 -> LFunction_bddAbove_near_one (no pole for χ ≠ 1)',
              '    riemannZetaLogDerivResidue (:504)         -> LFunction_logDeriv_bddAbove_near_one (with continuousAt_neg_logDeriv_LFunction_one)',
              '    riemannZetaLogDerivResidueBigO (:542)     -> LFunction_logDeriv_isBigO_one',
              '    riemannZeta0 (:548)                       -> LFunction0 (with charPartialSum), the Abel-summation form',
              '    riemannZeta0_apply (:557)                 -> definitional (LFunction0 is written in the applied form)',
              '    HasDerivAtZeta0 (:1095)                   -> ### HELD, NOT ATTEMPTED: the four attempts were spent; its first',
              '                                                 consumed fact, the bound on the partial sums of χ, compiled here',
              '                                                 (norm_charPartialSum_le, via sum_range_block_char_eq_zero and',
              '                                                 norm_sum_range_char_le)',
              '    Zeta0EqZeta (:1178) and all after it      -> not attempted',
              '', '### THE HELD POINT AND WHAT IT NEEDS: s -> LFunction0 χ M s differentiable on 0 < re s (the derivative under the',
              '### integral over (M, oo), the analogue of ZetaBounds`s own hasDerivAt_Zeta0Integral for the kernel S_χ), then its',
              '### agreement with LFunction χ there (identity theorem from agreement on re s > 1). The rev`s search (relay',
              '### data/b564_held_search.txt):']
        for q, v in hs.items():
            L.append('    %-44s files %3d lines %4d' % (q[:44], v['files'], v['lines']))
        L += ['### read: LFunction_eq_LSeries holds for 1 < re s only (DirichletContinuation.lean :75); LSeries_eq_mul_integral',
              '### (SumCoeff.lean :137) needs LSeriesSummable, which fails for χ on re s <= 1; no bound on the partial sums of a',
              '### character by name (so it was proved here); the Dirichlet test holds in general form (SpecificLimits/Normed.lean',
              '### :722); LFunction`s big-O lemmas are horizontal at re s = 1 (Nonvanishing.lean :316, :334); the `conditionally`',
              '### hits are order theory, read by file. ### THE READING: the rev holds no representation of LFunction χ on',
              '### 0 < re s by its partial sums; the analytic tools the analogue would use it holds in general form. The module is',
              '### HELD at the analogue of HasDerivAtZeta0 by its four attempts, the fact it would establish being the one the rev',
              '### lacks. ### ITS KIND: THE GROWTH SIDE -- not archimedean and not the Euler side`s logarithmic-derivative expansion.']
        extra = dict(held_at='HasDerivAtZeta0 (ZetaBounds.lean :1095)', kind='THE GROWTH SIDE')
    put_txt('b564_%s.txt' % X, L)
    put_json('b564_%s.json' % X, dict(part=X, file=rel, tip=tip, rows=rows, all_std3=ok,
                                       attempts=[dict(label=a, head=h, errors=e) for a, h, e in att], **extra))
    print(NL.join(L[-4:]))


ROW = ['chi_reflect_zero', 'chi_mult_reflect', 'analyticOrderAt_completed_one_sub', 'finite_window_chi', 'chiZeroConfig_conj_mem',
       'norm_charPartialSum_le']
NSG = 'SIDEExplicitFormula.GRHWeil.'


def _grade_scan():
    flat = re.sub(r'\s+', ' ', rd(os.path.join(D, 'b564_grade_scan.txt')))
    out = {}
    for m in re.finditer(r'B564GRADE (\S+) nprop=(\d+) \[(.*?)\](?= B564GRADE| ?$)', flat):
        # ### the whole type of each binder (b564: reading the head token alone graded `hT : Zeta23.Tail.T₀ ≤ T` INTERFACES)
        binders = [tuple(x.split(' : ', 1)) for x in re.split(r', (?=[^\s,:]+ : )', m.group(3)) if ' : ' in x]
        out[m.group(1)] = dict(nprop=int(m.group(2)), binders=binders, raw=m.group(3)[:400])
    return out


def e0():
    decls = jl('b564_decls.json')
    pr = rd(os.path.join(D, 'b564_prints.txt'))
    P0 = parse_prints(pr)
    GS = _grade_scan()
    L = ['b564 -- READING (7): THE E0 READ -- EVERY DECLARATION OF SIDEExplicitFormula/Chi/*.lean GRADED, THE SALT-CHECK, THE ROWGEN RECORD', '',
         '### the prints of record: AxiomCheckChi.lean elaborated against scratch oleans built by `lean -o` from the branch tip`s',
         '### files (relay data/b564_olean_build.txt: each source`s sha256 equals its committed blob`s); the premises: relay',
         '### data/b564_grade_scan.txt (every explicit Prop binder of every theorem, from Lean`s elaborated statement).',
         '### THE RULE: a theorem is INTERFACES when an explicit Prop binder other than the instance`s own (hχ : χ.IsPrimitive,',
         '### h1 : χ ≠ 1) has a Zeta23 predicate at its head -- a premise the vendored module names (TailHyp, EF_lit, ...),',
         '### passed through the instantiation unchanged; DERIVES otherwise (its other binders are domain conditions: a zero,',
         '### a real part, a window). Definitions are ungraded and salt-checked.', '']
    rows = {}
    for d in decls:
        n = d['name']
        ax = P0.get(n)
        if d['kind'] == 'def':
            gr, why = 'DEF', ''
        else:
            gsn = GS.get(n)
            named = [(b, t.split(' (')[0].split(' ')[0]) for b, t in (gsn['binders'] if gsn else [])
                     if b not in ('hχ', 'h1') and t.startswith('Zeta23.') and not t.startswith('Zeta23.ZeroConfig')
                     and not re.search(r' (?:≤|<|=|≠|∈|⊆|≥|>) ', t)]
            gr = 'INTERFACES' if named else 'DERIVES'
            why = ', '.join('%s : %s' % bt for bt in named)
            if gsn is None:
                gr, why = 'UNREAD', 'not in the premise scan'
        rows[n] = dict(file=d['file'], grade=gr, why=why, axioms=ax, std3=ax is not None and set(ax) <= set(STD3))
        L.append('    %-72s %-10s %s%s' % (n.replace('SIDEExplicitFormula.GRHWeil.', ''), 'DEFINITION' if gr == 'DEF' else gr,
                                           'std3' if rows[n]['std3'] else ax, ('  -- on ' + why[:120]) if why else ''))
    L.append('')
    L.append('### THE SALT-CHECK -- Lean`s #print of each definition (no sorry; every constant a Mathlib, Zeta23 or kernel object):')
    salt = {}
    for d in decls:
        if d['kind'] != 'def':
            continue
        j = pr.find('def %s' % d['name'])
        blk = pr[j:j + 700].split(NL + NL)[0] if j >= 0 else ''
        salt[d['name']] = bool(blk) and 'sorry' not in blk
        if not d['name'].startswith(NSG + 'Generic.'):
            L += ['    ' + x for x in blk.split(NL)[:4]] if blk else ['    ### %s NOT PRINTED' % d['name']]
    ng = sum(1 for k in salt if k.startswith(NSG + 'Generic.'))
    L.append('    (the %d Generic definitions: each printed, each the vendored definition applied to chiZeroConfig)' % ng)
    salt_ok = all(salt.values())
    L.append('### ### **THE SALT-CHECK: %s** (%d definitions)' % (salt_ok, len(salt)))
    tip = g(EF, 'rev-parse', BR).strip()
    txt = pr + NL + rd(os.path.join(D, 'b564_row_checks.txt'))
    recs, ctl = rowgen_record([NSG + n for n in ROW], 'SIDEExplicitFormula/Chi/ZeroConfig.lean', tip, txt)
    for r in recs:
        if r['name'].endswith('norm_charPartialSum_le'):
            recs2, _ = rowgen_record([r['name']], 'SIDEExplicitFormula/Chi/ZetaBounds.lean', tip, txt)
            r.update(recs2[0])
    L.append('')
    L.append('### THE ROWGEN RECORD (rowgen.py`s extract_doc_body and definition_encoded IMPORTED, at %s):' % tip[:7])
    for r in recs:
        L.append('    %-38s defenc %-5s %s | check %s' % (r['name'].split('.')[-1], r['defenc'], r['defenc_why'], bool(r['check'])))
    L.append('    control: definition_encoded on `def b560_ctl_stub : Prop := True` -> %s (must be True)' % (ctl,))
    thms = [n for n, r in rows.items() if r['grade'] != 'DEF']
    cnt = {k: sum(1 for n in thms if rows[n]['grade'] == k) for k in ('DERIVES', 'INTERFACES', 'UNREAD')}
    per = {}
    for n in thms:
        per.setdefault((rows[n]['file'].split('/')[-1], rows[n]['grade']), 0)
        per[(rows[n]['file'].split('/')[-1], rows[n]['grade'])] += 1
    gate = (all(r['std3'] for r in rows.values()) and cnt['UNREAD'] == 0 and salt_ok and ctl[0]
            and not any(r['defenc'] for r in recs) and all(r['check'] for r in recs) and len(P0) == len(rows))
    L.append('### by file and grade: %s' % ', '.join('%s %s %d' % (a, b, c) for (a, b), c in sorted(per.items())))
    L.append('### ### **THE GATE: EVERY PRINT THE STANDARD THREE %s ; THEOREMS %d (DERIVES %d, INTERFACES %d, UNREAD %d) ; DEFINITIONS %d ; '
             'PRINTED %d OF %d ; THE SALT-CHECK %s => MERGE %s**' % (all(r['std3'] for r in rows.values()), len(thms), cnt['DERIVES'],
                                                                    cnt['INTERFACES'], cnt['UNREAD'], len(rows) - len(thms), len(P0),
                                                                    len(rows), salt_ok, gate))
    put_txt('b564_e0.txt', L)
    put_json('b564_e0.json', dict(rows=rows, gate=gate, salt=salt_ok, rowgen=recs, rowgen_control=ctl[0], tip=tip, counts=cnt))
    print(NL.join(L[-3:]))


PRE_HEADS = dict(Z3.PRE_HEADS, **{'SIDE-explicit-formula': '1e4a007', 'SIDE-global-section': PRIOR_GS})
NEW_FILES = ['AxiomCheckChi.lean', 'SIDEExplicitFormula/Chi/Generic.lean', 'SIDEExplicitFormula/Chi/ZeroConfig.lean',
             'SIDEExplicitFormula/Chi/ZetaBounds.lean']
KEPT_TIPS = {'detection-region-b559': '8faf7ded8754870669547c9caa54ee5f0275e7c1',
             'li-weil-b561': '2df46d79bd59a900dde5b8ad8240faa2a0471cdc',
             'grh-weil-b562': 'de1f175ec02655b7b1d95f22e73004e6052cfa2e',
             'li-weil-b563': '1e4a00792008' + ''}
ROW_ACT = '400'


def kstate():
    ls = {}
    for l in g(EF, 'ls-remote', 'origin').split(NL):
        if '\t' in l:
            h, r = l.split('\t')
            ls[r.strip()] = h.strip()
    ns = [x for x in g(EF, 'diff', '--name-status', V07, 'main').split(NL) if x.strip()]
    kept = {b: g(EF, 'rev-parse', b).strip() for b in KEPT_TIPS}
    mains = {}
    for k, h in PRE_HEADS.items():
        mains[k] = sorted(x for x in g(os.path.join(Q.DD, k), 'diff', '--name-only', h, 'main').split(NL) if x.strip())
    return dict(main=g(EF, 'rev-parse', 'main').strip(), remote=ls, v08=g(EF, 'rev-parse', 'v0.8^{}').strip(),
                v08obj=g(EF, 'rev-parse', 'v0.8').strip(), v08type=g(EF, 'cat-file', '-t', 'v0.8').strip(),
                br=g(EF, 'rev-parse', BR).strip(), kept=kept, ns=sorted(x.replace('\t', ' ') for x in ns), mains=mains,
                ff=subprocess.run(['git', '-C', EF, 'merge-base', '--is-ancestor', V07, 'main']).returncode == 0)


def scores():
    k = kstate()
    ta = jl('b564_trailsup_after.json')
    pa, pb, pc = jl('b564_a.json'), jl('b564_b.json'), jl('b564_c1.json')
    dag, conv, pr = jl('b564_dag.json'), jl('b564_converse_price.json'), jl('b564_prior_art.json')
    only_term = ta['changed'] == ['SIDE-explicit-formula|SIDEExplicitFormula.LiWeil.%s CONFLICT -> SHELL' % TERM]
    n1 = only_term and len(ta['conflict_regenerated']) == len(ta['conflict_committed']) - 1
    cells = ta['term'].get('regenerated', [])
    s1 = only_term and len(cells) == 1 and cells[0]['ledger'].endswith('CORRESPONDENCE.md') and cells[0]['line'] == 470
    others = {kk: v for kk, v in k['mains'].items() if kk not in ('SIDE-explicit-formula', 'SIDE-global-section')}
    n7 = (k['ns'] == ['A ' + f for f in NEW_FILES] and k['ff'] and all(not v for v in others.values())
          and k['mains'].get('SIDE-global-section') in ([], ['CORRESPONDENCE.md'])
          and all(k['kept'][b].startswith(t[:12]) for b, t in KEPT_TIPS.items()))
    v08 = k['v08'] == k['main'] == k['br'] and k['remote'].get('refs/tags/v0.8^{}') == k['v08'] and k['remote'].get('refs/heads/main') == k['main']
    s = dict(h16a=False, h16b=pa.get('h16b') == 'HELD', h16c=dag.get('h16c') == 'HELD', h16d=conv.get('h16d') == 'HELD',
             n1=n1, n2=pr.get('n2') == 'HELD', n3=conv.get('n3') == 'HELD', n4=dag.get('h16c') == 'HELD',
             n5=pb.get('h16a') == 'HELD' and pa.get('h16b') == 'HELD',
             n6=v08 and pc.get('kind') in ('THE ARCHIMEDEAN SIDE', 'THE EULER SIDE'), n7=n7,
             s1=s1, s2=pa.get('s2') == 'HELD', s3=pb.get('s3') == 'HELD', v08=v08, kstate=k)
    L = ['b564 -- THE SCORES, READ OFF THE BANKS', '']
    for key in ('h16a', 'h16b', 'h16c', 'h16d', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 's1', 's2', 's3', 'v08'):
        L.append('    %-5s %s' % (key.upper(), w_(s[key])))
    L += ['### (N6) read: v0.8 tagged with the χ-instance %s ; the frontier HELD at %s (%s), which is neither archimedean nor the'
          ' Euler side' % (v08, pc.get('held_at'), pc.get('kind')),
          '### (N7) read: main against v0.7 %s (a fast-forward %s) ; other kernel mains changed %s ; SIDE-global-section %s ; the kept'
          ' branches at their tips %s' % (k['ns'], k['ff'], {kk: v for kk, v in others.items() if v} or 'NONE',
                                         k['mains'].get('SIDE-global-section'),
                                         all(k['kept'][b].startswith(t[:12]) for b, t in KEPT_TIPS.items()))]
    put_txt('b564_scores.txt', L)
    put_json('b564_scores.json', s)
    print(NL.join(L))


FH_W = '## b563 at its weight: the forward half of Li’s criterion and the Bombieri–Lagarias limit formula over Mathlib’s zeros; the ceiling sentence entered'
FH = ('## GRH-Weil, act two: the χ-instance of the zero configuration, the generic modules consumed, the frontier held at '
      'ZetaBounds (the analogue of HasDerivAtZeta0)')


def findings():
    guard_absent(FIND, FH_W)
    guard_absent(FIND, FH)
    s, k = jl('b564_scores.json'), kstate()
    ce, fa = jl('b564_ceiling.json'), jl('b564_fieldappend.json')
    pb, dag, e0j = jl('b564_b.json'), jl('b564_dag.json'), jl('b564_e0.json')
    ta, conv = jl('b564_trailsup_after.json'), jl('b564_converse_price.json')
    tw = ['', FH_W, '',
          '*Filed at b564 on the author’s ruling `(R174)`(1). SIDE-explicit-formula v0.7 = `1e4a007`, `LiWeilSym.lean`, 65 '
          'declarations at the standard three (relay `data/b563_e0.txt`).*', '',
          'The symmetric family lies in EF_lit’s class; its transforms tend to the Li terms at each zero; the real part of the '
          'member’s transform is bounded by a constant free of δ over ‖ρ‖², the even cut cancelling the jump’s n/ρ term in the '
          'real part; convergence over the configuration discharges the symmetric exchange; and LiCoeff n is the δ → 0⁺ limit of '
          'the explicit formula’s prime and archimedean sides at the symmetric members -- the Bombieri–Lagarias formula in limit '
          'form, with no premise. H15a-H15d held; the per-n re-score from b562’s bank landed on the classical λ_n within floor at '
          'every n.', '',
          '**The ceiling entry of (R146)(2) gains the author’s sentence**, appended beside it at README.md :%s and REGISTRY.md :%s '
          '(the (R146)(2) lines at :115 and :950 standing unedited above): *%s* Not supportable, unchanged: *RH proved*; '
          '*h2_sign proved*; *Li’s criterion compiled* without the half named.'
          % (ce['files']['README.md']['new_line'], ce['files']['REGISTRY.md']['new_line'], ce['sentence']), '',
          '*Nothing deposits; nothing at Zenodo written; nothing here is a statement about RH beyond the compiled statements’ own words.*', '']
    recl = pb.get('reclassified', [])
    t = ['', FH, '',
         '*Filed at b564 on the author’s ruling `(R174)`. Lane two, act six. Banks: relay `data/b564_dag.txt`, `data/b564_a.txt`, '
         '`data/b564_b.txt`, `data/b564_c1.txt`, `data/b564_e0.txt`, `data/b564_generic_leanscan.txt`, `data/b564_generic_scan.txt`, '
         '`data/b564_held_search.txt`, `data/b564_v08_push.txt`; SIDE-explicit-formula v0.8 = `%s`. Nothing about the zeros of ζ or '
         'of any L(s, χ) is claimed beyond the compiled statements’ own words.*' % k['v08'][:7], '',
         '**The χ-instance compiles** (`Chi/ZeroConfig.lean`, at attempt 1). For a primitive Dirichlet character χ ≠ 1, the zeros '
         'of Mathlib’s `DirichletCharacter.LFunction χ` in the open strip, with multiplicity the analytic order, form a Zeta23 '
         '`ZeroConfig` (`chiZeroConfig`): the order is finite by the identity theorem on ℂ; the zeros are locally finite; and '
         'ρ ↦ 1 − conj ρ preserves them with their orders, from the functional equation applied to χ and to χ⁻¹ (two order '
         'inequalities, so no fact about the root number is consumed), the Gamma factor’s reciprocal being entire and nonzero on '
         'the strip, and b562’s pairing across (χ, χ⁻¹), which is attached (ρ in χ’s carrier iff conj ρ in χ⁻¹’s, with equal '
         'multiplicity). Every fact consumed is Mathlib’s at the rev or the kernel’s (relay `data/b564_a.txt`).', '',
         '**The generic modules consumed** (`Chi/Generic.lean`, at attempt 2). Every module the DAG classes generic is imported '
         'unedited, and each of the %d declarations of those modules whose type takes a `ZeroConfig` (a scan run in Lean over the '
         'environment) is applied to the χ-instance and compiles. %d of the resulting theorems carry a premise the vendored module '
         'names (TailHyp, EF_lit, PaperInputs, ...), passed through unchanged: they are statements about χ’s zeros conditional on '
         'those premises, which nothing here proves for χ. **The lexical scan re-classifies %d of the generic modules** -- %s -- '
         'which carry ζ’s explicit-formula constants under neutral names (ζ’s Γ bracket at 1/4 + iτ/2 with log π and no log N, '
         'the pole terms at ±i/2, the Λ(n) sum with no character). The count corrected: generic %d → %d, ζ-specific %d → %d. '
         'H16a is refuted on that clause while the build consumes the modules unedited.'
         % (len(jl('b564_generic_leanscan.json')['consumers']), e0j['counts']['INTERFACES'] if False else
            sum(1 for n, r in e0j['rows'].items() if r['grade'] == 'INTERFACES'), len(recl), ', '.join(recl),
            len(dag['generic']), pb['generic_corrected'], len(dag['specific']), pb['specific_corrected']), '',
         '**The frontier** (relay `data/b564_dag.txt`; the DAG read twice, no edge disagreeing). The ζ-specific modules with no '
         'ζ-specific import are two, Zeta23.Statement (the configuration instance) and Zeta23.FromPNTPlus.ZetaBounds (the growth '
         'side), at equal depth; the DAG leaves them unordered and the face’s tie rule puts the configuration instance first. Its '
         'χ-analogue is the instance above. **ZetaBounds’s χ-analogues** (`Chi/ZetaBounds.lean`, four attempts) compile in the '
         'module’s order to its Euler–Maclaurin form, re-made for χ by summation by parts, and the bound ‖S_χ(x)‖ ≤ N + 1 on the '
         'partial sums of χ, which the rev holds under no name. The module is **held at the analogue of HasDerivAtZeta0**: its '
         'next step would represent `LFunction χ` on 0 < Re s by those partial sums, and the rev holds that representation only '
         'where the Dirichlet series converges absolutely (`LFunction_eq_LSeries` at 1 < Re s; `LSeries_eq_mul_integral` under '
         'absolute summability). That is the growth side, not the archimedean or the Euler side.', '',
         '**122 declarations at the standard three** (relay `data/b564_e0.txt`): %d theorems graded DERIVES, %d INTERFACES, 40 '
         'definitions salt-checked. Merged by fast-forward; v0.8 pushed after main read back; the branch `%s` pushed by name and '
         'kept.' % (sum(1 for r in e0j['rows'].values() if r['grade'] == 'DERIVES'),
                    sum(1 for r in e0j['rows'].values() if r['grade'] == 'INTERFACES'), BR), '',
         '**Beside the build.** The trail-line supersession at OPEN_TRAILS :%s takes b562’s trail line :11577 off the table’s '
         'reading for li_identity_of_exchange: CONFLICT %d → %d, that terminal alone moving, to the grade of row 397. The author’s '
         'words on the line are T2-INTERFACES-on-false-premise; the table carries row 397’s SHELL cell, and the difference is '
         'left for the author. Prior art for the Li form is appended to the field entry at :%s. The converse is re-priced at the '
         'LI-WEIL-BRIDGE work-order (OPEN_TRAILS :%s): (V1) compiled, (V2) and (V3) one lemma each, (V4) the power-sum lemma '
         'absent from Mathlib by name.'
         % (jl('b564_supline.json').get('line'), len(ta['conflict_committed']), len(ta['conflict_regenerated']), fa.get('line'),
            conv['appends']['workorder']['line']), '',
         '**The scores.** H16a %s; H16b %s; H16c %s; H16d %s. (N1) %s, (N2) %s, (N3) %s, (N4) %s, (N5) %s, (N6) %s, (N7) %s.'
         % tuple(w_(s.get(x)) for x in ('h16a', 'h16b', 'h16c', 'h16d', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7')), '',
         '**Next** (`(R174)`(7)): the frontier is held at the growth side, not at an archimedean fact, so by the ruling’s words '
         'GRH-WEIL act three at the frontier -- ZetaBounds’s χ-analogue from HasDerivAtZeta0 -- the author ruling on the closing.', '',
         '*Nothing deposits; nothing at Zenodo written; no `sorry` on any `main`; nothing here is a statement about RH, GRH or any '
         'zero beyond the compiled statements’ own words.*', '']
    o1 = append_to(FIND, NL.join(tw))
    o1['heading_line'] = line_of(FIND, FH_W)
    o2 = append_to(FIND, NL.join(t))
    o2['heading_line'] = line_of(FIND, FH)
    put_json('b564_findings.json', dict(weight=o1, entry=o2))
    print('  FINDINGS.md:%s (weight) :%s (entry)' % (o1['heading_line'], o2['heading_line']))


def rows():
    k = kstate()
    ej = jl('b564_e0.json')
    act = [ROW_ACT,
           '**GRH-WEIL ACT TWO: THE χ-INSTANCE OF THE ZERO CONFIGURATION, THE GENERIC MODULES CONSUMED, THE FRONTIER HELD AT '
           'ZetaBounds** (b564, under (R174)(5)). SIDE-explicit-formula v0.8 = %s (Chi/ZeroConfig.lean, Chi/Generic.lean, '
           'Chi/ZetaBounds.lean): the nontrivial zeros of Mathlib’s LFunction χ, primitive χ ≠ 1, with multiplicity, as a Zeta23 '
           'ZeroConfig -- reflection-stable by the functional equation for χ and χ⁻¹ with no root-number fact; the generic Zeta23 '
           'modules imported unedited and their ZeroConfig-taking declarations applied to it; ZetaBounds’s χ-analogues to its '
           'Euler–Maclaurin form and the bound on χ’s partial sums, held at the analogue of HasDerivAtZeta0. Nothing here proves '
           'GRH or RH.' % k['v08'][:7],
           '`SIDE-explicit-formula/SIDEExplicitFormula/Chi/ZeroConfig.lean` (v0.8) : ' + ', '.join('`%s%s`' % (NSG, n) for n in ROW),
           '%d of %d declarations: [propext, Classical.choice, Quot.sound], no sorryAx (relay data/b564_e0.txt)'
           % (sum(1 for r2 in ej['rows'].values() if r2['std3']), len(ej['rows'])),
           ' ; '.join('`%s` %s' % (n, ej['rows'][NSG + n]['grade']) for n in ROW),
           'LANDED on main by fast-forward, v0.8 pushed after main read back (tools/push_gated.sh); the branch grh-weil-b564 pushed '
           'by name and kept; h2 where the deposit left it; nothing deposits; nothing at Zenodo written.']
    r2 = subprocess.run([sys.executable, os.path.join(T, 'corr_row.py'), CORR] + act, capture_output=True, text=True, encoding='utf-8')
    print(r2.stdout[-300:], r2.stderr[-300:])
    put_json('b564_rows.json', dict(act=act, exit_act=r2.returncode))


WO_H = ('*Appended 2026-09-29 by b564, under the author’s ruling `(R174)`(5), to the W-ORD-GRH-WEIL entry (:11373; b562’s line at '
        ':11565) -- ACT TWO’S LINE:*')
HEADING = ('### b564 — lane two, act six under (R174): GRH-WEIL act two -- the χ-instance compiled, the generic modules consumed, '
           'the frontier held at ZetaBounds (v0.8); the ceiling sentence; the conflict cleared; prior art for the Li form; the '
           'converse re-priced')


def workorder():
    guard_absent(OT, WO_H)
    k = kstate()
    pb, dag = jl('b564_b.json'), jl('b564_dag.json')
    t = (NL + WO_H + ' at SIDE-explicit-formula v0.8 = `%s`: **THE χ-INSTANCE COMPILED** (`Chi/ZeroConfig.lean`, chiZeroConfig '
         'for primitive χ ≠ 1, from the rev’s LFunction facts); **THE GENERIC MODULES CONSUMED UNEDITED** (`Chi/Generic.lean`, '
         'their ZeroConfig-taking declarations applied to it), with %d of the %d generic modules re-classified ζ-specific by the '
         'constants they carry (the count now generic %d, ζ-specific %d); **THE FRONTIER** of two modules, the configuration '
         'instance (answered by the instance) and ZetaBounds, **HELD at ZetaBounds’s analogue of HasDerivAtZeta0** -- the '
         'representation of LFunction χ on 0 < Re s by its partial sums, which the rev lacks. The critical path’s price at '
         ':11425 stands beside this. Next, by `(R174)`(7): GRH-WEIL act three at the frontier, the author ruling on the closing.'
         % (k['v08'][:7], len(pb['reclassified']), len(dag['generic']), pb['generic_corrected'], pb['specific_corrected']) + NL)
    o = append_to(OT, t)
    o['line'] = line_of(OT, WO_H)
    put_json('b564_workorder.json', o)
    print('  OPEN_TRAILS.md:%(line)d (%(added)d bytes, prefix %(prefix)s)' % o)


def trail():
    guard_absent(OT, HEADING)
    s = jl('b564_scores.json')
    f, wo, sup, fa = jl('b564_findings.json'), jl('b564_workorder.json'), jl('b564_supline.json'), jl('b564_fieldappend.json')
    ce, conv, ta = jl('b564_ceiling.json'), jl('b564_converse_price.json'), jl('b564_trailsup_after.json')
    k = kstate()
    t = ['', HEADING, '',
         '**(R174) ratified.** (1) b563 at its weight; the ceiling gains the author’s sentence. (2) The conflict, by the trail-line '
         'supersession. (3) Prior art for Li’s criterion and the Bombieri–Lagarias formula. (4) The converse re-priced on the '
         'reflection map. (5) GRH-WEIL act two. (6) The hypotheses. (7) The gates; the next act.', '',
         '**Entered:** FINDINGS.md:%s (the field-entry append), :%s (b563 at its weight), :%s (the entry); OPEN_TRAILS.md:%s (the '
         'supersession line), :%s (the converse’s price at the LI-WEIL-BRIDGE work-order), :%s (the residue chain’s pointer), :%s '
         '(the W-ORD-GRH-WEIL line); README.md :%s and REGISTRY.md :%s (the ceiling sentence); SIDE-global-section '
         'CORRESPONDENCE.md row %s; SIDE-explicit-formula v0.8 = `%s`, the branch `%s` pushed by name and kept.'
         % (fa.get('line'), f['weight']['heading_line'], f['entry']['heading_line'], sup.get('line'),
            conv['appends']['workorder']['line'], conv['appends']['pointer']['line'], wo.get('line'),
            ce['files']['README.md']['new_line'], ce['files']['REGISTRY.md']['new_line'], ROW_ACT, k['v08'][:7], BR), '',
         '**H16a %s · H16b %s · H16c %s · H16d %s.** The χ-instance compiles with no root-number fact; the generic modules are '
         'consumed unedited, eight of them re-classified by the constants they carry; the frontier is two modules, held at '
         'ZetaBounds’s analogue of HasDerivAtZeta0, on the growth side.' % tuple(w_(s.get(x)) for x in ('h16a', 'h16b', 'h16c', 'h16d')), '',
         '**The table:** li_identity_of_exchange reads the grade of row 397 alone after the line; CONFLICT %d → %d; no other '
         'grade moved. The author’s words on the line, T2-INTERFACES-on-false-premise, are not a table cell, and the table’s '
         'SHELL beside them is left for the author.' % (len(ta['conflict_committed']), len(ta['conflict_regenerated'])), '',
         '**Next:** GRH-WEIL act three at the frontier (`(R174)`(7)), the author ruling on the closing.', '',
         '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s · (N6) %s · (N7) %s.** The seat’s own: (S1) %s, (S2) %s, (S3) %s.'
         % tuple(w_(s.get(x)) for x in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 's1', 's2', 's3')),
         '**One fast-forward onto `main`, one tag pushed after main read back, no `sorry` on any `main`.** Nothing deposits; '
         'nothing at Zenodo written; no existing statement changed; no existing `.lean` file edited; no Zeta23 file edited or '
         'added; no monograph byte changed; no keystone body edited; ERRATA untouched; the ceiling gains one sentence as ruled; '
         'row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN; nothing here is a statement about RH, GRH '
         'or any zero beyond the compiled statements’ own words.', '']
    o = append_to(OT, NL.join(t))
    o['line'] = line_of(OT, HEADING)
    put_json('b564_trail.json', o)
    print('  OPEN_TRAILS.md:%(line)d (%(added)d bytes appended, prefix kept %(prefix)s)' % o)


def rowgen_diff():
    sys.path.insert(0, os.path.join(T, 'rowgen'))
    import rowgen as RG
    recs = jl('b564_e0.json').get('rowgen', [])
    for r in recs:
        r['exists'] = bool(r.get('check'))
        r['axioms'] = "'%s' depends on axioms: [%s]" % (r['name'], ', '.join(r['axioms'] or [])) if isinstance(r.get('axioms'), list) else (r.get('axioms') or '')
    rowtxt = [l for l in rd(CORR).split(NL) if l.startswith('| %s |' % ROW_ACT)]
    out = RG.diff(recs, NL.join(rowtxt))
    L = ['b564 -- READING (7): THE ROWGEN DIFF (rowgen.diff IMPORTED) OF THE MERGED RECORDS AGAINST CORRESPONDENCE ROW %s' % ROW_ACT, '',
         '### records: %d ; row found: %s' % (len(recs), bool(rowtxt))] + ['    ' + str(x) for x in out]
    put_txt('b564_rowgen.txt', L)
    print(NL.join(L))


def defects():
    src = os.path.join(D, 'b564_defects_src.txt')
    L = ['### b564 -- THIS ACT`S OWN DEFECTS (the desk).'] + ['    ' + l for l in rd(src).strip().split(NL)]
    put_txt('b564_defects.txt', L)
    print(NL.join(L))


def desk():
    s = jl('b564_scores.json')
    pa, pb, pc, dag, conv, pr = (jl(x) for x in ('b564_a.json', 'b564_b.json', 'b564_c1.json', 'b564_dag.json',
                                                 'b564_converse_price.json', 'b564_prior_art.json'))
    ta, ej = jl('b564_trailsup_after.json'), jl('b564_e0.json')
    k = s['kstate']
    L = ['=' * 104, 'b564 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### (R174)`S FOUR.', '-' * 104,
         '  **(H16a)** ### **%s.** -- the consumption build compiles with every generic module imported unedited (data/b564_b.txt, '
         'attempt b_2); the scan re-classifies %d generic modules that carry ζ-specific constants (%s): the count corrected to '
         'generic %d, ζ-specific %d.' % (w_(s['h16a']), len(pb['reclassified']), ', '.join(pb['reclassified']),
                                         pb['generic_corrected'], pb['specific_corrected']),
         '  **(H16b)** ### **%s.** -- chiZeroConfig compiles from the rev`s LFunction facts at the standard three (data/b564_a.txt, '
         'attempt a_1).' % w_(s['h16b']),
         '  **(H16c)** ### **%s.** -- the frontier has %d modules, %s; the earliest under the face`s order is %s (a tie at equal '
         'depth, broken by the face`s rule); no archimedean module at the frontier (data/b564_dag.txt).'
         % (w_(s['h16c']), len(dag['frontier']), ', '.join('%s (%s)' % (f['module'], f['kind']) for f in dag['frontier']), dag['order'][0]),
         '  **(H16d)** ### **%s.** -- no Turán-type power-sum inequality by name in Mathlib at 51e6992e (data/b564_converse_price.txt).'
         % w_(s['h16d']), '',
         '### THE NAVIGATOR`S SEVEN.', '-' * 104,
         '  **(N1)** ### **%s.** -- CONFLICT %d -> %d; the terminals whose grade changed: %s (data/b564_trailsup_after.txt).'
         % (w_(s['n1']), len(ta['conflict_committed']), len(ta['conflict_regenerated']), ta['changed']),
         '  **(N2)** ### **%s.** -- none in Mathlib or Zeta23; two public Lean developments formalize the objects: %s (Li`s '
         'criterion, both directions) and %s (the Bombieri–Lagarias explicit formula), read, not built (data/b564_prior_art.txt).'
         % (w_(s['n2']), BULKA, ARDA),
         '  **(N3)** ### **%s.** -- H16d HELD.' % w_(s['n3']),
         '  **(N4)** ### **%s.** -- H16c HELD.' % w_(s['n4']),
         '  **(N5)** ### **%s.** -- H16b HELD; H16a REFUTED on its constants clause.' % w_(s['n5']),
         '  **(N6)** ### **%s.** -- v0.8 = %s tagged with the χ-instance (its first clause holds); the frontier is held at %s, %s, '
         'not archimedean or Euler-side (its second clause fails).' % (w_(s['n6']), k['v08'][:7], pc['held_at'], pc['kind']),
         '  **(N7)** ### **%s.** -- main against v0.7 %s, a fast-forward %s; other kernel mains unchanged; the kept branches at '
         'their tips; nothing deposits; nothing at Zenodo.' % (w_(s['n7']), k['ns'], k['ff']), '',
         '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- li_identity_of_exchange reads one cell after the line, CORRESPONDENCE :470 (row 397); no other '
         'grade moved.' % w_(s['s1']),
         '  **(S2)** ### **%s.** -- no root-number fact consumed (data/b564_a.txt).' % w_(s['s2']),
         '  **(S3)** ### **%s.** -- H16a refuted on its second clause while the consumption build compiles.' % w_(s['s3']), '',
         '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE 0.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % (sum(1 for x in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7') if s[x]), sum(1 for x in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7') if not s[x]),
            sum(1 for x in ('s1', 's2', 's3') if s[x]), sum(1 for x in ('s1', 's2', 's3') if not s[x])),
         '### ### **(R174) : H16a %s ; H16b %s ; H16c %s ; H16d %s.**' % tuple(w_(s[x]) for x in ('h16a', 'h16b', 'h16c', 'h16d')), '']
    L += rd(os.path.join(D, 'b564_defects.txt')).rstrip().split(NL)
    put_txt('b564_desk_notes.txt', L)
    print(NL.join(L[:40]))


def components():
    L = ['=' * 132, 'b564 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '']
    for n in ('b564_reads.txt', 'b564_trailsup_before.txt', 'b564_trailsup_after.txt', 'b564_ceiling.txt', 'b564_prior_art.txt',
              'b564_converse_price.txt', 'b564_dag.txt', 'b564_a.txt', 'b564_b.txt', 'b564_c1.txt', 'b564_e0.txt',
              'b564_v08_push.txt', 'b564_rowgen.txt', 'b564_branches.txt', 'b564_scores.txt'):
        L.append('### relay data/%s' % n)
        L.extend('  ' + x for x in rd(os.path.join(D, n)).rstrip().split(NL))
        L.append('')
    for n, key in (('b564_supline.json', 'line'), ('b564_fieldappend.json', 'line'), ('b564_rows.json', 'exit_act'),
                   ('b564_workorder.json', 'line'), ('b564_trail.json', 'line')):
        L.append('### relay data/%s -- %s %s' % (n, key, jl(n).get(key)))
    put_txt('b564_components.txt', L)
    print('  written: b564_components.txt (%d lines)' % len(L))


def main(argv):
    cmd = argv[0] if argv else ''
    if cmd in ('scores', 'findings', 'rows', 'workorder', 'trail', 'rowgen_diff', 'defects', 'desk', 'components'):
        return globals()[cmd]()
    if cmd == 'e0':
        return e0()
    if cmd == 'part':
        return part(argv[1])
    if cmd == 'dag':
        return dag()
    if cmd == 'converse':
        return converse()
    if cmd == 'priorart':
        return priorart()
    if cmd == 'fieldappend':
        return fieldappend()
    if cmd == 'reads':
        return reads()
    if cmd == 'ceiling':
        return ceiling()
    if cmd == 'trailsup':
        return trailsup(argv[1])
    if cmd == 'supline':
        return supline()
    sys.exit('usage: b564_record.py reads | ...')


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
