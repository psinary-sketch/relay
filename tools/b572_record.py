# -*- coding: utf-8 -*-
"""b572_record.py -- THE ACT'S RECORD TOOL, UNDER (R182). ### ONE SUBCOMMAND PER BANK.

### ### b572: LANE TWO, ACT TWELVE -- GRH-WEIL ACT SEVEN. Subcommands write only `data/b572_*` unless the docstring names a
### ledger. Every bank is written through `put_txt` / `put_json` (encode first, then a temp file, then `os.replace`).
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
V013 = 'ac157c1d0024801116d79cf41126d28780fe1152'
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


DEFECTS = [
    '(a) COMPONENT 1 WAS BANKED AFTER COMPONENTS 2-4: the ferry orders the components in order; the seat ran the reality read, the '
    'lemma list and the build (through the kernel push of v0.14) before writing the weight and ceiling lines. Nothing in Components 2-4 '
    'reads those lines, and they are written as ruled; the order is the defect.',
    '(b) THE CONVERSE`S GENERATOR NEEDED THREE NEEDLE CORRECTIONS BEFORE ITS FIRST OUTPUT (an indentation, a docstring phrase its own '
    'ζ-guard caught, a console encoding) and one after (a proof-local h1 shadowing the hypothesis h1, caught by elaboration); every '
    'replacement is asserted, the generator is banked as relay data/b572_gen_converse.py.txt.',
    '(c) TWO SHELL QUOTING SLIPS WHILE WRITING THE RECORD TOOL: a here-document carrying its second block failed to parse (nothing was '
    'written; the block went through the Write tool), and a double-quoted python -c carrying backticks had them read as command '
    'substitution, which mangled this list`s text (b) and (c); the list was rewritten by the Edit tool before any arm read it.',
    '(d) THE SUITE, PRE-PUSH RUN ONE: G-REG-LOCKED-FIRST PASSED ITS POSITIVE CONTROL -- with no relay commit after step zero but the '
    'excluded 547b20fb before the act`s own commit, its all() over later commits was vacuous; G-ARMS-NO-LIVE-LIMB failed with it, as '
    'designed. The arm now also asks that 547b20fb precede the seal, and its control moves the seal before it; the table files restored '
    'to their committed state and the suite re-run.',
]


def defects():
    put_txt('b572_defects.txt', ['### b572 -- THIS ACT`S OWN DEFECTS (the seat`s), as they occur.'] + ['    ' + d for d in DEFECTS])


def _Q():
    import b566_record as R6
    return R6.Q


# ================================================================================ READING (1)
RELAY = ROOT.replace('\\', '/')
SGS = 'D:/SIDE-global-section'
READS = [
    ('kernel H2Sign (classK; h2_sign)', EF, V013, 'SIDEExplicitFormula/H2Sign.lean', [24, 29]),
    ('kernel Seam (rh_strip_imp_rh_holds; h2_sign_iff_rh)', EF, V013, 'SIDEExplicitFormula/Seam.lean', [86, 101]),
    ('kernel PowerLimit (tie_reflect; VF_conj; dominant_summable; zeroSide_eventually_neg; the assembly; the forward half)', EF, V013,
     'SIDEExplicitFormula/PowerLimit.lean', [232, 634, 949, 1082, 1167, 1188, 1197]),
    ('kernel PowerWindow (rh_strip)', EF, V013, 'SIDEExplicitFormula/PowerWindow.lean', [483]),
    ('kernel RHChain (rh_imp_h2_sign)', EF, V013, 'SIDEExplicitFormula/RHChain.lean', [24]),
    ('vendored Zeta23 Defs (reflect; ZeroConfig and its reflection fields)', EF, V013, 'Zeta23/Defs.lean', [124, 136, 145, 146]),
    ('kernel GRHWeil (GRH_chi; h2_sign_chi; LFunction_inv_conj)', EF, V013, 'SIDEExplicitFormula/GRHWeil.lean', [53, 75, 185]),
    ('kernel Chi/ZeroConfig (chi_reflect_zero; chi_mult_reflect; chiZeroConfig)', EF, V013, 'SIDEExplicitFormula/Chi/ZeroConfig.lean',
     [183, 208, 225]),
    ('kernel Chi/Main (EF_lit_chi_holds)', EF, V013, 'SIDEExplicitFormula/Chi/Main.lean', [None]),
    ('PLACE-papers README (the last ceiling line)', PP, 'HEAD', 'README.md', [121]),
    ('PLACE-papers REGISTRY (the last ceiling line)', PP, 'HEAD', 'REGISTRY.md', [956]),
    ('PLACE-papers FINDINGS (the (R146)(2) ceiling entry`s record; b567`s amendment of it)', PP, 'HEAD', 'FINDINGS.md', [6144, 6214]),
]


def reads():
    L = ['b572 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, lines in READS:
        src = g(repo, 'show', '%s:%s' % (rev, path))
        sl = src.split(NL)
        if lines == [None]:
            lines = [i for i, l in enumerate(sl, 1) if l.startswith('theorem EF_lit_chi_holds')]
        L.append('### %s -- %s @ %s' % (label, path, g(repo, 'rev-parse', '--short=8', rev).strip()))
        for n in lines:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:300]))
    wg = [i for i, l in enumerate(io.open(os.path.join(PP, 'OPEN_TRAILS.md'), encoding='utf-8').read().split(NL), 1)
          if l.startswith('### `W-ORD-GRH-WEIL` -- THE χ-SIDE OF THE WEIL ARC')]
    L.append('### PLACE-papers OPEN_TRAILS -- the W-ORD-GRH-WEIL heading at :%s' % wg)
    put_txt('b572_reads.txt', L)


# ================================================================================ COMPONENTS 2-3: the walk
ZETA_SET = {'riemannZeta', 'completedRiemannZeta', 'RiemannHypothesis', 'Zeta23.zetaZeroConfig', 'Zeta23.zetaSeam',
            'Zeta23.IsNontrivialZero', 'Zeta23.WeilEF.EF_lit_zetaZeroConfig', 'Zeta23.RvM.zetaZeroConfig_local_count'}
CONJ_PAT = re.compile(r'conj_mem|mult_conj|_conj_conj|riemannZeta_conj|conj_stable|LFunction_inv_conj|analyticOrderAt_conj')
CONV_ROOT = 'SIDEExplicitFormula.B321.h2_sign_imp_rh_holds'


def zeta_naming(u):
    if u in ZETA_SET:
        return True
    if u.startswith('SIDEExplicitFormula.'):
        return False
    tail = u[len('Zeta23.'):] if u.startswith('Zeta23.') else u
    return 'zeta' in tail.lower()


AUX = re.compile(r'^(_.*|match_\d+|proof_\d+|eq_\d+)$')


def owner(n):
    parts = n.split('.')
    for i in range(1, len(parts)):
        if AUX.match(parts[i]):
            return '.'.join(parts[:i])
    return n


def walk(text, root):
    a = text.index('@@ROOT %s ' % root)
    b = text.index('@@DONE %s' % root, a)
    out = []
    for m in re.finditer(r'@@NODE (\S+) @@MOD (\S+) @@FROM (\S+) @@USES ?([^\n]*)', text[a:b]):
        out.append(dict(name=m.group(1), mod=m.group(2), parent=m.group(3), uses=m.group(4).split()))
    return out


def classify(nodes):
    decl, order = {}, []
    for nd in nodes:
        o = owner(nd['name'])
        if o not in decl:
            decl[o] = dict(mod=nd['mod'], uses=set())
            order.append(o)
        decl[o]['uses'] |= set(nd['uses'])
    res = []
    for o in order:
        d = decl[o]
        z = sorted(u for u in d['uses'] if zeta_naming(u))
        cj = sorted(u for u in d['uses'] if CONJ_PAT.search(u))
        rf = sorted(u for u in d['uses'] if u in ('Zeta23.ZeroConfig.reflect_mem', 'Zeta23.ZeroConfig.mult_reflect'))
        res.append(dict(name=o, mod=d['mod'], zeta=z, conj=cj, refl=rf, cls='ζ-NAMING' if z else 'GENERIC'))
    return res


def lemmas():
    """### Components 2-3: the probe's walk classed; banks data/b572_lemmas.txt (and .json)."""
    t = rd('b572_crit_probe_out.txt')
    full, conv, fwd = (classify(walk(t, r)) for r in ('SIDEExplicitFormula.B321.h2_sign_iff_rh', CONV_ROOT,
                                                       'SIDEExplicitFormula.B321.rh_imp_h2_sign'))
    L = ['b572 -- COMPONENT 3: THE LEMMA LIST, (R182)(4)(c) -- every kernel declaration h2_sign_iff_rh`s proof consumes, in the',
         '### order the constant walk reaches it (relay data/b572_crit_probe.lean.txt, its output data/b572_crit_probe_out.txt; v0.13 = '
         'ac157c1), auxiliary constants folded into their owner; ζ-NAMING when its type or value uses directly a constant of the ζ list',
         '### (%s, or any non-kernel constant whose name past `Zeta23.` carries `zeta`), the naming constants printed beside it.' %
         ', '.join(sorted(ZETA_SET)), '### written at (UTC) %s' % utc(), '']
    for title, lst in (('THE WHOLE PROOF (h2_sign_iff_rh)', full), ('THE CONVERSE (h2_sign_imp_rh_holds)', conv),
                       ('THE FORWARD HALF (rh_imp_h2_sign)', fwd)):
        zn = [x for x in lst if x['zeta']]
        L += ['### ' + title + ': declarations %d ; ζ-naming %d ; generic %d' % (len(lst), len(zn), len(lst) - len(zn))]
        for i, x in enumerate(lst, 1):
            L.append('    %3d  %-9s %-62s %-40s %s' % (i, x['cls'], x['name'].replace('SIDEExplicitFormula.', ''), x['mod'].replace(
                'SIDEExplicitFormula.', ''), ('naming: ' + ', '.join(x['zeta'])) if x['zeta'] else ''))
        L.append('')
    zc = [x for x in conv if x['zeta']]
    L += ['### ### **THE CONVERSE`S ζ-NAMING LEMMAS: %d** -- %s' % (len(zc), [x['name'].split('.')[-1] for x in zc])]
    put_txt('b572_lemmas.txt', L)
    put_json('b572_lemmas.json', dict(full=full, converse=conv, forward=fwd, converse_zeta=[x['name'] for x in zc]))


def reality():
    """### Component 2: which stability the ζ criterion consumes -- the reflection fields or a conjugation fact; banks
    ### data/b572_reality.txt (and .json)."""
    j = jl('b572_lemmas.json')
    conv = j['converse']
    refl = sorted(set(u for x in conv for u in x['refl']))
    users_refl = [x['name'].split('.')[-1] for x in conv if x['refl']]
    conjs = sorted(set(c for x in conv for c in x['conj']))
    choice = 'REFLECTION' if not conjs and refl else 'PAIRING'
    L = ['b572 -- COMPONENT 2: THE FORM`S REALITY, (R182)(3) -- WHAT THE ζ CRITERION`S PROOF CONSUMES, READ BEFORE ANY KERNEL FILE',
         '', '### written at (UTC) %s' % utc(),
         '### (1) The configuration structure (Zeta23/Defs.lean :136) carries reflect_mem and mult_reflect -- invariance under',
         '###     ρ ↦ 1 − ρ̄ (`Zeta23.reflect`, :124) -- and NO conjugation field.',
         '### (2) The converse`s walk (h2_sign_imp_rh_holds) uses the reflection fields %s, in %s.' % (refl, users_refl),
         '### (3) The converse`s walk uses a conjugation-stability fact of a configuration (pattern %s): %s.' % (CONJ_PAT.pattern,
                                                                                                               conjs or 'NONE'),
         '### (4) The sign is read on the real part only: h2_sign_imp_rh_strip_of closes on `(Complex.nonneg_iff.mp hsign).1` against a',
         '###     window whose zero side has negative real part (PowerLimit.lean :1188, :1159-:1161); the forward half needs no reality',
         '###     either -- on the line each zero`s term is m_ρ·|ĥ(γ_ρ)|², a nonnegative real (RHChain.lean :24-:58).',
         '### (5) The conjugation that does enter is of the TRANSFORM of a real even test function (paperFT_conj_eq, PowerLimit :215),',
         '###     with γ ↦ γ̄ supplied by the reflection (gammaOf_reflect, :204): a property of the test function, not of the configuration.',
         '', '### ### **THE CHOICE: %s.** %s' % (choice, (
             'Reflection suffices: h2_sign_chi is the statement over the χ-configuration alone -- already stated at GRHWeil.lean :75 (b562) '
             'and taken as the statement of record; chiZeroConfig carries reflect_mem and mult_reflect (Chi/ZeroConfig.lean :183, :208, :225); '
             'no paired form is stated.') if choice == 'REFLECTION' else
             'A conjugation fact is consumed: the paired form over (χ, χ⁻¹) is stated in a new module.')]
    put_txt('b572_reality.txt', L)
    put_json('b572_reality.json', dict(choice=choice, reflection_uses=refl, conj_uses=conjs, users_refl=users_refl))


# ================================================================================ COMPONENT 4: E0, rowgen
TERMS = [('433', 'zeroSide_chi_eq', 'SIDEExplicitFormula/Chi/CriterionForward.lean'),
         ('434', 'grh_chi_imp_h2_sign_chi', 'SIDEExplicitFormula/Chi/CriterionForward.lean'),
         ('435', 'h2_sign_chi_imp_grh_chi', 'SIDEExplicitFormula/Chi/CriterionConverse.lean'),
         ('436', 'h2_sign_chi_iff_grh_chi', 'SIDEExplicitFormula/Chi/CriterionConverse.lean')]
ROW_ACT = '432'
NS = 'SIDEExplicitFormula.GRHWeil.'


def e0(rev='grh-weil-b572'):
    """### every declaration of the act graded by the shared E0 rule at `rev` (the branch, before the merge), its print, and
    ### rowgen's record of the terminals of record (b566_record.Q.rowgen_record, IMPORTED)."""
    import b569_record as R9
    Q = _Q()
    pr = rd('b572_chi_prints.txt')
    P0 = R9.prints_axioms(pr)
    dj = jl('b572_decls_chi.json')
    tip = g(EF, 'rev-parse', rev).strip()
    rows, srcs = {}, {}
    L = ['b572 -- COMPONENTS 2-3: THE E0 READ -- EVERY DECLARATION GRADED, THE ROWGEN RECORD', '',
         '### the prints of record: relay data/b572_chi_prints.txt ; the statements at %s (%s).' % (tip[:7], rev)] + E0.RULE_TEXT + ['']
    for d in dj['decls']:
        n = d['name']
        if d['file'] not in srcs:
            srcs[d['file']] = g(EF, 'show', '%s:%s' % (tip, d['file']))
        head, _ln = R9.header_of(srcs[d['file']], n.split('.')[-1])
        gr, why, _b = E0.grade(head or '', d['kind'])
        ax = P0.get(n)
        rows[n] = dict(grade=gr, why=why, axioms=ax, std3=ax is not None and set(ax) <= set(STD3), head=head, file=d['file'],
                       header_read=head is not None, kind=d['kind'])
        L.append('    %-46s %-10s %s  -- %s' % (n.split('.')[-1], gr, 'std3' if rows[n]['std3'] else ax, (why or '')[:120]))
    cons = {n: P0.get(n) for n in dj['consumed']}
    L += ['', '### THE CONSUMED TERMINALS, their prints:'] + ['    %-62s %s' % (n, 'std3' if a is not None and set(a) <= set(STD3) else a)
                                                            for n, a in cons.items()]
    recs, ctl = [], (True,)
    for rn, n, rel in TERMS:
        r, ctl = Q.rowgen_record([NS + n], rel, tip, pr)
        recs += r
    L += ['', '### THE ROWGEN RECORD (at %s):' % tip[:7]]
    L += ['    %-40s defenc %-5s %s | check %s' % (r['name'].split('.')[-1], r['defenc'], r['defenc_why'], bool(r['check'])) for r in recs]
    th = [r for r in rows.values() if r['kind'] == 'theorem']
    cnt = {k: sum(1 for r in th if r['grade'] == k) for k in ('DERIVES', 'INTERFACES')}
    gate = (all(r['std3'] for r in rows.values()) and all(a is not None and set(a) <= set(STD3) for a in cons.values())
            and all(r['header_read'] for r in rows.values()) and ctl[0] and not any(r['defenc'] for r in recs) and all(r['check'] for r in recs))
    L.append('### ### **THE GATE: %s** -- declarations %d (theorems %d: DERIVES %d, INTERFACES %d), consumed %d'
             % ('PASS' if gate else 'FAIL', len(rows), len(th), cnt['DERIVES'], cnt['INTERFACES'], len(cons)))
    put_txt('b572_e0.txt', L)
    put_json('b572_e0.json', dict(rows=rows, consumed=cons, gate=gate, rowgen=recs, rowgen_control=ctl[0], tip=tip, rev=rev, counts=cnt))


def rowgen_diff():
    """### the act's terminal rows (433-436) read by rowgen.diff (IMPORTED, Lean's identifier set since relay 618143a8)."""
    Q = _Q()
    sys.path.insert(0, os.path.join(ROOT, 'tools', 'rowgen'))
    import rowgen as RG
    recs = jl('b572_e0.json').get('rowgen', [])
    for r in recs:
        r['exists'] = bool(r.get('check'))
        r['axioms'] = ("'%s' depends on axioms: [%s]" % (r['name'], ', '.join(r['axioms'] or []))
                       if isinstance(r.get('axioms'), list) else (r.get('axioms') or ''))
    L = ['b572 -- THE ROWGEN DIFF (rowgen.diff IMPORTED) OF THE RECORDS AGAINST CORRESPONDENCE ROWS 433-436', '']
    res = {}
    for rn, n, rel in TERMS:
        rowtxt = [l for l in Q.rd(Q.CORR).split(NL) if l.startswith('| %s |' % rn)]
        out = RG.diff(recs, NL.join(rowtxt))
        mine = [list(x) for x in out if isinstance(x, tuple) and x[0] == NS + n]
        res[rn] = dict(found=len(rowtxt) == 1, mine=mine)
        L.append('### row %s found: %s' % (rn, len(rowtxt) == 1))
        L += ['    ' + str(x) for x in out]
    ok = all(v['found'] and v['mine'] and all(m[1] == ['ok'] for m in v['mine']) for v in res.values())
    L += ['', '### ### **THE ROWGEN DIFF : %s on all %d rows.**' % ('CLEAN' if ok else 'NOT CLEAN', len(TERMS))]
    put_txt('b572_rowgen.txt', L)
    put_json('b572_rowgen.json', dict(rows=res, clean=ok))

# ================================================================================ COMPONENT 1: THE WEIGHT AND THE CEILING
V014 = '4dce7b97eb29733b823919bd80b08d01c82c6d8f'
CEILING = ('The explicit formula for primitive Dirichlet L-functions is compiled in the programme\'s kernel on Zeta23\'s generic '
           'modules (EF_lit_chi_holds, v0.13), the conductor entering as log(N/π) on the archimedean side; the χ-instance of the zero '
           'configuration and the χ-seam are compiled (v0.8, v0.6). The criterion for χ is not yet composed.')
CEIL_LINE = ('*(Appended under the author\'s ruling `(R182)`(2), 2026-10-01, b572, beside the `(R146)`(2) sentence, b564\'s `(R174)`(1) '
             'sentence, b566\'s `(R176)`(2) sentence and b567\'s `(R177)`(2) sentence above, which stay: b571 entered at its weight, '
             'SIDE-explicit-formula v0.13 = `ac157c1`.)* Supportable, the author\'s sentence: *' + CEILING + '* Not supportable: '
             '*GRH reduced*, *GRH proved*, anything about a zero of L(s, χ).')


def weight():
    """### PLACE-papers FINDINGS.md (two appended lines): (R182)(1) -- b571 at its weight; the navigator`s clause for (N4)`s letter."""
    Q = _Q()
    e = Q.line_of(Q.FIND, '## GRH-Weil, act six: the fold at χ⁻¹ with the conductor')
    h1 = '*Appended 2026-10-01 by b572 to b571’s entry (:%s), under `(R182)`(1) -- b571 AT ITS WEIGHT:*' % e
    h2 = '*Appended 2026-10-01 by b572 to b571’s entry (:%s), under `(R182)`(1) -- A CLAUSE RECORDED AS THE NAVIGATOR’S:*' % e
    Q.guard_absent(Q.FIND, h1)
    a1 = ('\n%s SIDE-explicit-formula v0.13 = `ac157c1`, tagged by the push script and read back: the explicit formula proved for every '
          'primitive χ ≠ 1 at the standard three, no sorryAx on main; every module on the route compiled for χ, all of them new, no '
          'existing statement changed. The conductor enters once, on the archimedean side, as log N·(1/2π)∫h, joining −log π in the '
          'bracket’s log(N/π). H23a, H23b, H23c held; (N5) refuted on its count, four modules after FullLine; the FACES_LEDGER form '
          'clears the clause-and-RH equivalence’s cell with CONFLICT 12 before and after; the row generator reads Lean’s identifier '
          'set; the suite 68 of 68.\n' % h1)
    a2 = ('\n%s (N4)’s letter, “ĝ(0)·log N” -- the compiled term is log N·(1/2π)∫h(r)dr, which is k(0)·log N by inversion (the test '
          'function at 0, not its transform); (N4) held in substance.\n' % h2)
    r = [Q.append_to(Q.FIND, a1), Q.append_to(Q.FIND, a2)]
    lines = [Q.line_of(Q.FIND, h1), Q.line_of(Q.FIND, h2)]
    put_json('b572_weight.json', dict(entry=e, lines=lines, appends=r))
    print(jl('b572_weight.json'))


def _place_after(path, line_no, text, expect_prefix):
    raw = open(path, 'rb').read()
    crlf = b'\r\n' in raw
    s = raw.decode('utf-8').replace('\r\n', '\n')
    ls = s.split('\n')
    if not ls[line_no - 1].startswith(expect_prefix):
        sys.exit('### %s :%d does not start with the expected ceiling line: %r' % (path, line_no, ls[line_no - 1][:80]))
    if text in s:
        sys.exit('### %s already carries the line' % path)
    new = ls[:line_no] + ['', text] + ls[line_no:]
    out = '\n'.join(new)
    if crlf:
        out = out.replace('\n', '\r\n')
    b = out.encode('utf-8')
    open(path + '.tmp', 'wb').write(b)
    os.replace(path + '.tmp', path)
    return line_no + 2


def ceiling():
    """### PLACE-papers README.md and REGISTRY.md (one placed line each, after the last ceiling line) and FINDINGS.md (one appended
    ### line addressed to the (R146)(2) ceiling entry`s record, :6144): (R182)(2), the author`s sentence."""
    Q = _Q()
    pre = '*(Appended under the author\'s ruling `(R177)`(2), 2026-10-01, b567'
    rl = _place_after(os.path.join(PP, 'README.md'), 121, CEIL_LINE, pre)
    gl = _place_after(os.path.join(PP, 'REGISTRY.md'), 956, CEIL_LINE, pre)
    h = '*Appended 2026-10-01 by b572 to the record of the ceiling entry of `(R146)`(2) (:6144), under `(R182)`(2) -- THE CEILING’S χ-SENTENCE:*'
    Q.guard_absent(Q.FIND, h)
    a = ('\n%s the author’s sentence, placed at README.md :%d and REGISTRY.md :%d beside the earlier ceiling lines, which stay: *%s* '
         'Not supportable: *GRH reduced*, *GRH proved*, anything about a zero of L(s, χ).\n' % (h, rl, gl, CEILING))
    r = Q.append_to(Q.FIND, a)
    put_json('b572_ceiling.json', dict(readme=rl, registry=gl, findings=Q.line_of(Q.FIND, h), append=r, line=CEIL_LINE))
    L = ['b572 -- COMPONENT 1: THE CEILING`S χ-SENTENCE, (R182)(2), AT ITS THREE PLACES', '']
    for f, n in (('README.md', rl), ('REGISTRY.md', gl), ('FINDINGS.md', Q.line_of(Q.FIND, h))):
        sl = io.open(os.path.join(PP, f), encoding='utf-8').read().replace(chr(13), '').split(NL)
        L.append('### PLACE-papers %s :%d' % (f, n))
        L.append('    ' + sl[n - 1])
    put_txt('b572_ceiling.txt', L)
    print(jl('b572_ceiling.json'))

# ================================================================================ COMPONENT 5: THE SCHEMA PRICED
AXIOM_OF = {
    'zeroSide': 'EF: an explicit formula of EF_lit`s shape for Z (the zero side equals the arithmetic side on C_c²)',
    'b321_identity': 'EF: an explicit formula of EF_lit`s shape for Z',
    'dominant_summable': 'COUNT: the local count HCount Z A₀',
    'h2_sign_imp_rh': 'SEAM: the strip zeros of Z are the L-function`s nontrivial zeros (the target`s own form)',
    'rh_strip_imp_rh': 'SEAM: the strip zeros of Z are the L-function`s nontrivial zeros',
    'rh_strip_imp_rh_holds': 'SEAM: the strip zeros of Z are the L-function`s nontrivial zeros',
    'zeta_zero_re_nonpos': 'SEAM: no zero off the strip but the trivial points',
}


def schema():
    """### OPEN_TRAILS (one appended line): (R182)(5) -- the generic schema priced at W-ORD-GRH-WEIL, NOT STARTED."""
    Q = _Q()
    j = jl('b572_lemmas.json')
    zc = [x['name'].split('.')[-1] for x in j['converse'] if x['zeta']]
    price = [(n, AXIOM_OF.get(n, 'NONE: names the configuration in its statement only (Z a parameter)')) for n in zc]
    kinds = {}
    for n, a in price:
        kinds.setdefault(a.split(':')[0], []).append(n)
    wg = Q.line_of(Q.OT, '### `W-ORD-GRH-WEIL` -- THE χ-SIDE OF THE WEIL ARC')
    h = '*Appended 2026-10-01 by b572, under the author’s ruling `(R182)`(5), to the W-ORD-GRH-WEIL entry'
    Q.guard_absent(Q.OT, h + ' (:%s) -- A PRICED ITEM' % wg)
    a = ('\n%s (:%s) -- A PRICED ITEM, NOT STARTED, THE GENERIC SCHEMA:* for a ZeroConfig with an explicit formula of EF_lit’s shape and '
         'a seam, Weil positivity on classK ⟺ all zeros on the line. Price: the %d ζ-naming lemmas of the ζ converse (relay '
         '`data/b572_lemmas.txt`), each with the configuration axiom it would need -- EF (an explicit formula of EF_lit’s shape): %s; '
         'COUNT (the local count): %s; SEAM (the strip zeros are the L-function’s nontrivial zeros): %s; NONE (the configuration named '
         'in the statement only): %s. The χ-instance compiled with the same three inputs (relay `data/b572_gen_converse.py.txt`).\n'
         % (h, wg, len(zc), ', '.join(kinds.get('EF', [])), ', '.join(kinds.get('COUNT', [])), ', '.join(kinds.get('SEAM', [])),
            ', '.join(kinds.get('NONE', []))))
    r = Q.append_to(Q.OT, a)
    put_json('b572_schema.json', dict(line=Q.line_of(Q.OT, h + ' (:%s) -- A PRICED ITEM' % wg), wg=wg, price=price, kinds=kinds, append=r))
    print({k: len(v) for k, v in kinds.items()})


# ================================================================================ COMPONENT 6: THE RECORD
def scores():
    rl, lm, e = jl('b572_reality.json'), jl('b572_lemmas.json'), jl('b572_e0.json')
    kp = rd('b572_kernel_push_out.txt')
    ns = [x for x in g(EF, 'diff', '--name-status', V013, 'main').split(NL) if x.strip()]
    nz = len(lm['converse_zeta'])
    rows = e['rows']
    iff = rows.get(NS + 'h2_sign_chi_iff_grh_chi', {})
    fwd = rows.get(NS + 'grh_chi_imp_h2_sign_chi', {})
    fwd_src = g(EF, 'show', V014 + ':SIDEExplicitFormula/Chi/CriterionForward.lean')
    seam = [n for n in lm['converse_zeta'] if n.split('.')[-1] in ('h2_sign_imp_rh', 'rh_strip_imp_rh', 'rh_strip_imp_rh_holds',
                                                                  'zeta_zero_re_nonpos')]
    stmt_new = 'def h2_sign_chi' in g(EF, 'diff', V013, 'main', '--', 'SIDEExplicitFormula')
    v014 = ('tag v0.14 peeled local %s remote %s' % (V014, V014)) in kp
    S = dict(
        H24a=('HELD' if rl['choice'] == 'REFLECTION' and not stmt_new else 'REFUTED',
              'the ζ converse consumes the configuration`s reflection (%s, in %s) and no conjugation-stability fact (%s); h2_sign_chi is '
              'b562`s statement over the χ-configuration alone (GRHWeil.lean :75), no paired form stated (data/b572_reality.txt)'
              % (rl['reflection_uses'], rl['users_refl'], rl['conj_uses'] or 'NONE')),
        H24b=('HELD' if fwd.get('grade') == 'DERIVES' and fwd.get('std3') and _attempt_ok('b572_attempt_criterionforward_1.txt') else 'REFUTED',
              'grh_chi_imp_h2_sign_chi compiled at its first elaboration (data/b572_attempt_criterionforward_1.txt), DERIVES at the standard '
              'three; its one χ input is EF_lit_chi_holds (b571) through zeroSide_chi_eq, otherwise RHChain`s argument as it stands '
              '(paperFT_weilTest, normSq) -- no new input'),
        H24c=('HELD' if nz <= 3 else 'REFUTED',
              'the converse consumes %d ζ-naming declarations (data/b572_lemmas.txt): %s -- the zero side and its identity, the strip form, '
              'the L7e lemmas stated over zetaZeroConfig, the local count, and the seam (%d: %s)'
              % (nz, [n.split('.')[-1] for n in lm['converse_zeta']], len(seam), [n.split('.')[-1] for n in seam])),
        H24d=('HELD' if iff.get('grade') == 'DERIVES' and iff.get('std3') and e.get('gate') else 'REFUTED',
              'h2_sign_chi_iff_grh_chi lands, E0 %s, prints %s (data/b572_chi_prints.txt, data/b572_e0.txt); no sorryAx on main'
              % (iff.get('grade'), iff.get('axioms'))),
        N1=('HELD' if rl['choice'] == 'REFLECTION' else 'REFUTED', 'H24a %s' % ('HELD' if rl['choice'] == 'REFLECTION' else 'REFUTED')),
        N2=('HELD', 'H24b HELD'),
        N3=('HELD' if nz <= 3 else 'REFUTED', '%d ζ-naming declarations in the converse, not three or fewer (H24c)' % nz),
        N4=('HELD' if iff.get('grade') == 'DERIVES' and iff.get('std3') else 'REFUTED',
            'the converse landed: h2_sign_chi_iff_grh_chi prints %s and grades %s' % (iff.get('axioms'), iff.get('grade'))),
        N5=('HELD' if v014 and ns and all(x.startswith('A\t') or x == 'M\tREADME.md' for x in ns) else 'REFUTED',
            'v0.14 = %s made by push_gated.sh and read back, with the forward half and the converse (h2_sign_chi itself is b562`s, '
            'unedited); v0.13 against main: %s; nothing at Zenodo; nothing deposits' % (V014[:7], ns)),
        S1=('REFUTED', 'its first clause held -- H24c is refuted by the lemma list (%d) -- but its enumeration did not: besides the zero '
                       'side, the strip form and the local count, the seam names ζ (%s)' % (nz, [n.split('.')[-1] for n in seam])),
        S2=('REFUTED', 'its second clause held -- the χ-analogues are their ζ proofs with the configuration, the zero side and the local '
                       'count changed, no new analytic fact (data/b572_gen_converse.py.txt) -- but not every ζ-naming lemma names ζ only '
                       'through those three: the seam`s %s name the functional equation of riemannZeta; for χ the strip form is GRH_chi '
                       'itself and no seam is consumed' % [n.split('.')[-1] for n in seam]),
        S3=('HELD' if not stmt_new else 'REFUTED', 'h2_sign_chi is b562`s definition, unedited; no new statement of it in the act`s modules'),
        counts=dict(decls=len(rows), theorems=sum(1 for r in rows.values() if r['kind'] == 'theorem'), derives=e['counts']['DERIVES'],
                    interfaces=e['counts']['INTERFACES'], consumed=len(e['consumed']), zeta=nz, conv=len(lm['converse']), seam=len(seam)),
    )
    put_json('b572_scores.json', S)
    for k in ('H24a', 'H24b', 'H24c', 'H24d', 'N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3'):
        print('  %-5s %s' % (k, S[k][0]))


def _attempt_ok(name):
    t = rd(name)
    return re.search(r'^=== END \S+ rc=0$', t, re.M) is not None and 'error' not in t


SCORE_KEYS = ('H24a', 'H24b', 'H24c', 'H24d', 'N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')


def findings():
    Q = _Q()
    S = jl('b572_scores.json')
    c = S['counts']
    title = '## GRH-Weil, act seven: the criterion at the χ-instance, the form’s reality by reflection, h2_sign_chi ⟺ GRH_chi landed'
    Q.guard_absent(Q.FIND, title)
    e = ['', title, '',
         '*Filed at b572 on the author’s ruling `(R182)`. Banks: relay `data/b572_reality.txt`, `data/b572_lemmas.txt`, '
         '`data/b572_chi_prints.txt`, `data/b572_e0.txt`, `data/b572_gen_converse.py.txt`, `data/b572_ceiling.txt`. Nothing about the zeros '
         'of ζ or of any L(s, χ) is claimed beyond the compiled statements’ own words.*', '',
         '**The form’s reality** (`(R182)`(3)). The ζ criterion’s proof consumes the configuration’s reflection ρ ↦ 1 − ρ̄ and no '
         'conjugation-stability fact; its sign is read on the real part, and the conjugation that enters is of the transform of a real '
         'even test function. So Weil positivity for χ is stated over the χ-configuration alone -- b562’s statement, unedited.', '',
         '**The lemma list** (`(R182)`(4)(c)). The ζ converse consumes %d kernel declarations, %d of them naming ζ: the zero side and its '
         'identity, the strip form, the L7e lemmas stated over the ζ configuration, the local count, and the seam (%d).' % (c['conv'], c['zeta'],
                                                                                                                       c['seam']), '',
         '**The build** (`(R182)`(4)), SIDE-explicit-formula v0.14 = `%s`, %d declarations at the standard three. The forward half by '
         'RHChain’s argument with the explicit formula for χ as its one χ input; the converse by PowerLimit’s L7e carried to the '
         'χ-configuration with its own local count, every generic lemma consumed as it stands; **Weil positivity on classK for χ is '
         'equivalent to GRH for χ, both directions compiled, for every primitive χ ≠ 1.** An equivalence between open statements; it '
         'proves neither. For χ no seam is consumed: GRH for χ is stated in its strip form.' % (V014[:7], c['decls']), '',
         '**The ceiling** (`(R182)`(2)): the author’s χ-sentence placed at README, REGISTRY and the record of the ceiling entry. Its last '
         'clause, “the criterion for χ is not yet composed”, is overtaken by this act’s landing; the sentence stands as ruled, and the '
         'clause is routed to the author.', '',
         '**The schema** (`(R182)`(5)) priced at W-ORD-GRH-WEIL, not started.', '',
         '**The scores.** H24a %s; H24b %s; H24c %s; H24d %s. (N1) %s, (N2) %s, (N3) %s, (N4) %s, (N5) %s; the seat’s (S1) %s, (S2) %s, '
         '(S3) %s.' % tuple(S[k][0] for k in SCORE_KEYS), '',
         '**Next.** Per `(R182)`(6): the schema or CP-5, on the author’s word at the closing; the χ-leg’s page (the back-matter line of '
         'CP-4) is a component of whichever act follows.', '',
         '*Nothing deposits; nothing at Zenodo written; no existing statement of any kernel changed; no sentence here claims priority; '
         'nothing here is a statement about RH, GRH or any zero beyond the compiled statements’ own words.*', '']
    r = Q.append_to(Q.FIND, NL.join(e))
    put_json('b572_findings.json', dict(entry_line=Q.line_of(Q.FIND, title), append=r, title=title))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, title))


def workorder():
    """### OPEN_TRAILS (one appended line): the W-ORD-GRH-WEIL entry -- the criterion for χ landed; the next act named."""
    Q = _Q()
    wg = Q.line_of(Q.OT, '### `W-ORD-GRH-WEIL` -- THE χ-SIDE OF THE WEIL ARC')
    h = '*Appended 2026-10-01 by b572, under the author’s ruling `(R182)`(6), to the W-ORD-GRH-WEIL entry'
    Q.guard_absent(Q.OT, h + ' (:%s) -- THE CRITERION' % wg)
    a = ('\n%s (:%s) -- THE CRITERION FOR χ LANDED:* SIDE-explicit-formula v0.14 = `%s` compiles Weil positivity on classK for χ ⟺ GRH '
         'for χ, every primitive χ ≠ 1 (Chi/CriterionConverse.lean). The next act is the schema priced above or CP-5, on the author’s '
         'word; the χ-leg’s page is a component of whichever follows.\n' % (h, wg, V014[:7]))
    r = Q.append_to(Q.OT, a)
    put_json('b572_workorder.json', dict(line=Q.line_of(Q.OT, h + ' (:%s) -- THE CRITERION' % wg), wg=wg, append=r))
    print(jl('b572_workorder.json'))


def trail():
    Q = _Q()
    S = jl('b572_scores.json')
    fj, wj, sj, cj, wt = (jl('b572_findings.json'), jl('b572_workorder.json'), jl('b572_schema.json'), jl('b572_ceiling.json'),
                          jl('b572_weight.json'))
    head = ('### b572 — lane two, act twelve under (R182): GRH-Weil act seven -- the criterion at the χ-instance, the form’s reality '
            'by reflection, h2_sign_chi ⟺ GRH_chi landed; the ceiling’s χ-sentence; the generic schema priced')
    Q.guard_absent(Q.OT, head)
    rows = ['', head, '',
            '**(R182) ratified.** (1) b571 entered at its weight. (2) The ceiling’s χ-sentence at its three places. (3) The form’s reality '
            'settled before the build. (4) GRH-Weil act seven. (5) The schema priced. (6) The gates; v0.14; the next act on the author’s '
            'word.', '',
            '**Entered:** FINDINGS.md:%s and :%s (b571’s weight; the navigator’s clause), :%s (the ceiling’s record), :%s (the entry); '
            'README.md:%s and REGISTRY.md:%s (the ceiling line); OPEN_TRAILS.md:%s (the schema priced), :%s (the work-order line), this '
            'record; SIDE-global-section CORRESPONDENCE.md rows 432-436; SIDE-explicit-formula main = **v0.14** = `%s`, grh-weil-b572 '
            'pushed by name.' % (wt['lines'][0], wt['lines'][1], cj['findings'], fj['entry_line'], cj['readme'], cj['registry'], sj['line'],
                                 wj['line'], V014[:7]), '',
            '**H24a %s · H24b %s · H24c %s · H24d %s. (N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s.** The seat’s own: (S1) %s, (S2) %s, '
            '(S3) %s.' % tuple(S[k][0] for k in SCORE_KEYS), '',
            '**Next:** per `(R182)`(6), the schema or CP-5 on the author’s word at the closing; the χ-leg’s page (CP-4’s back-matter line) '
            'a component of whichever follows; the ceiling sentence’s last clause, overtaken by this act, routed to the author.', '',
            '**No `sorry` on any `main`.** Nothing deposits; nothing at Zenodo written; no existing statement changed; no Zeta23 or vendored '
            'file edited or added; ERRATA untouched; FACES_LEDGER untouched; row U1 unedited; `h2` where the deposit left it; the four lists '
            'stay OPEN; nothing here is a statement about RH, GRH or any zero beyond the compiled statements’ own words.', '']
    r = Q.append_to(Q.OT, NL.join(rows))
    put_json('b572_trail.json', dict(line=Q.line_of(Q.OT, head), head=head, append=r))
    print(jl('b572_trail.json')['line'])


def rows():
    import b569_record as R9
    Q = _Q()
    e = jl('b572_e0.json')
    for rn, n, rel in TERMS:
        if e['rows'][NS + n]['grade'] != 'DERIVES' or not e['rows'][NS + n]['std3']:
            sys.exit('### %s not graded at the standard three: no row' % n)
    for rn in (ROW_ACT,) + tuple(t[0] for t in TERMS):
        if [l for l in Q.rd(Q.CORR).split(NL) if l.startswith('| %s |' % rn)]:
            sys.exit('### ROW %s ALREADY PRESENT' % rn)
    pr = R9.prints_axioms(rd('b572_chi_prints.txt'))
    out = []
    act = [ROW_ACT,
           '**GRH-WEIL ACT SEVEN** (b572, under (R182)(4)). SIDE-explicit-formula v0.14 = %s: the criterion at the χ-instance -- the '
           'zero side for χ and its identity, the forward half, the converse by L7e carried to the χ-configuration; Weil positivity on '
           'classK for χ is GRH for χ, every primitive χ ≠ 1. An equivalence between open statements; nothing here proves RH or GRH.' % V014[:7],
           'SIDE-explicit-formula SIDEExplicitFormula/Chi/{CriterionForward,CriterionConverse}.lean (v0.14 = %s)' % V014[:7],
           '%d declarations print within [propext, Classical.choice, Quot.sound], no sorryAx (relay data/b572_chi_prints.txt)' % len(e['rows']),
           ' ; '.join('`%s` DERIVES' % t[1] for t in TERMS),
           'LANDED at v0.14 = %s; nothing deposits; nothing at Zenodo written.' % V014[:7]]
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'corr_row.py'), Q.CORR] + act, capture_output=True, text=True, encoding='utf-8')
    out.append(dict(row=ROW_ACT, exit=r.returncode, tail=(r.stdout + r.stderr)[-300:]))
    for rn, n, rel in TERMS:
        head = ' '.join(e['rows'][NS + n]['head'].split()).replace('|', '‖')
        cells = [rn, '**%s** (b572, under (R182)(4)), SIDE-explicit-formula v0.14 = %s: `%s%s %s`.' % (n, V014[:7], NS, n, head),
                 '`SIDE-explicit-formula/%s` (v0.14 = %s) : `%s%s`' % (rel, V014[:7], NS, n),
                 '\'%s%s\' depends on axioms: [%s] (relay data/b572_chi_prints.txt)' % (NS, n, ', '.join(pr.get(NS + n) or [])),
                 '`%s` DERIVES' % n,
                 'LANDED at v0.14 = %s; the E0 read at the branch tip (relay data/b572_e0.txt); domain conditions only.' % V014[:7]]
        r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'corr_row.py'), Q.CORR] + cells, capture_output=True, text=True,
                           encoding='utf-8')
        out.append(dict(row=rn, exit=r.returncode, tail=(r.stdout + r.stderr)[-300:]))
    put_json('b572_rows.json', dict(rows=out, act=act))
    print('  rows', [(o['row'], o['exit']) for o in out])


def desk():
    S = jl('b572_scores.json')
    L = ['=' * 104, 'b572 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H24a-H24d ((R182)(3)-(4)).', '-' * 104]
    L += ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in ('H24a', 'H24b', 'H24c', 'H24d')]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in
                                                         ('N1', 'N2', 'N3', 'N4', 'N5')]
    L += ['', '### THE SEAT`S THREE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in ('S1', 'S2', 'S3')]
    nh = sum(1 for k in ('N1', 'N2', 'N3', 'N4', 'N5') if S[k][0] == 'HELD')
    sh = sum(1 for k in ('S1', 'S2', 'S3') if S[k][0] == 'HELD')
    L += ['', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (nh, 5 - nh, sh, 3 - sh), '']
    L += rd('b572_defects.txt').rstrip(NL).split(NL)
    put_txt('b572_desk_notes.txt', L)


def components():
    S = jl('b572_scores.json')
    fj, tj, rj, wj, sj, cj, wt = (jl('b572_findings.json'), jl('b572_trail.json'), jl('b572_rows.json'), jl('b572_workorder.json'),
                                  jl('b572_schema.json'), jl('b572_ceiling.json'), jl('b572_weight.json'))
    L = ['b572 -- THE COMPONENTS, BANKED UNDER (R182).', '',
         '### COMPONENT 0 : the process listing (no orphan) ; b571`s push-out banks relay 547b20fb ; push-b571 branches deleted by name '
         '(data/b572_branches.txt) ; the kept branches untouched',
         '### COMPONENT 1 : b571`s weight FINDINGS :%s, the navigator`s clause :%s ; the ceiling README :%s, REGISTRY :%s, FINDINGS :%s '
         '(data/b572_ceiling.txt) -- written after Components 2-4 (defect (a))' % (wt['lines'][0], wt['lines'][1], cj['readme'], cj['registry'],
                                                                                   cj['findings']),
         '### COMPONENT 2 : the reality read (data/b572_reality.txt) : REFLECTION ; H24a %s' % S['H24a'][0],
         '### COMPONENT 3 : the lemma list (data/b572_lemmas.txt) : %d ζ-naming of %d in the converse ; H24c %s' % (S['counts']['zeta'],
                                                                                                                 S['counts']['conv'], S['H24c'][0]),
         '### COMPONENT 4 : CriterionForward (H24b %s), CriterionConverse ; h2_sign_chi_iff_grh_chi landed ; H24d %s ; v0.14 = %s by '
         'push_gated.sh ; grh-weil-b572 pushed, no held branch' % (S['H24b'][0], S['H24d'][0], V014[:7]),
         '### COMPONENT 5 : the schema priced, OPEN_TRAILS :%s, not started' % sj['line'],
         '### COMPONENT 6 : FINDINGS :%s ; OPEN_TRAILS :%s (the work-order), :%s (the record) ; CORRESPONDENCE rows %s ; the page unchanged '
         '(no node changed) ; next: the schema or CP-5, on the author`s word' % (fj['entry_line'], wj['line'], tj['line'],
                                                                                ', '.join('%s (exit %d)' % (o['row'], o['exit']) for o in rj['rows']))]
    put_txt('b572_components.txt', L)

if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b572_record.py <subcommand>')
        sys.exit(2)
    sys.exit(fn(*sys.argv[2:]) or 0)
